param(
  [Parameter(Mandatory=$true)][string]$InDir,
  [Parameter(Mandatory=$true)][string]$OutDir
)
# capture_reports.mjs가 찍은 PNG를 JPEG로: *_thumb.png → 640px 폭, *_full.png → 하단 빈 여백 트림 후 1000px 폭.
Add-Type -AssemblyName System.Drawing
$jpegCodec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
function Save-Jpeg($bmp, $path, $quality) {
  $ep = New-Object System.Drawing.Imaging.EncoderParameters(1)
  $ep.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]$quality)
  $bmp.Save($path, $jpegCodec, $ep)
  $ep.Dispose()
}
function Resize-Bitmap($src, $w) {
  $h = [int][math]::Round($src.Height * $w / $src.Width)
  $dst = New-Object System.Drawing.Bitmap($w, $h)
  $g = [System.Drawing.Graphics]::FromImage($dst)
  $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
  $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
  $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
  $g.Clear([System.Drawing.Color]::White)
  $g.DrawImage($src, 0, 0, $w, $h)
  $g.Dispose()
  return $dst
}
# 맨 아래 행의 색과 같은 행이 이어지는 구간을 잘라낸다(최소 높이 1200은 남긴다).
function Trim-Bottom($src) {
  $w = $src.Width; $h = $src.Height
  $base = $src.GetPixel(4, $h - 1)
  $cut = $h
  for ($y = $h - 1; $y -ge 1200; $y -= 2) {
    $same = $true
    for ($x = 4; $x -lt $w; $x += 32) {
      $p = $src.GetPixel($x, $y)
      if ([math]::Abs($p.R - $base.R) -gt 6 -or [math]::Abs($p.G - $base.G) -gt 6 -or [math]::Abs($p.B - $base.B) -gt 6) { $same = $false; break }
    }
    if (-not $same) { $cut = [math]::Min($h, $y + 40); break }
  }
  if ($cut -ge $h) { return $src }
  $rect = New-Object System.Drawing.Rectangle(0, 0, $w, $cut)
  return $src.Clone($rect, $src.PixelFormat)
}
$count = 0
Get-ChildItem -Path $InDir -Filter '*.png' | ForEach-Object {
  $name = $_.BaseName
  $img = [System.Drawing.Bitmap]::FromFile($_.FullName)
  try {
    if ($name -like '*_thumb') {
      $r = Resize-Bitmap $img 640
      Save-Jpeg $r (Join-Path $OutDir ($name + '.jpg')) 84
      $r.Dispose()
    } else {
      $t = Trim-Bottom $img
      $r = Resize-Bitmap $t 1000
      Save-Jpeg $r (Join-Path $OutDir ($name + '.jpg')) 80
      $r.Dispose()
      if ($t -ne $img) { $t.Dispose() }
    }
    $count++
  } finally { $img.Dispose() }
}
"JPEG $count 장 → $OutDir"
