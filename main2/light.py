def createLight(rPower, gPower, bPower):
  side = 100
  center = side / 2.0
  img = createImage(side, side, RGB)
  
  for y in range(side):
    for x in range(side):
        try:
           #distance = sqrt(sq(center - x) + sq(center - y))
           distance = (sq(center - x) + sq(center - y)) / 50.0+1
           r = int( (255 * rPower) / distance )
           g = int( (255 * gPower) / distance )
           b = int( (255 * bPower) / distance )
           img.pixels[x + y * side] = color(r, g, b)
        except ValueError:
            print("ZeroZero")
  return img;