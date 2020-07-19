from PIL import Image

wire = Image.open("wire.png",'r')

img = Image.new('RGB', (100,100))

xmin,xmax = 0,99
ymin,ymax = 0,99

pos_new = [0,0]
pos_wire = 0

while not ((xmax - 1 == xmin) or (ymax-1 == ymin)):
  for x in range(xmin,xmax+1):
    print("x:",pos_new[0],"y:",pos_new[1])
    pos_new[0] = x
    pos_wire += 1
    img.putpixel(pos_new,wire.getpixel((pos_wire,0)))

  ymin += 1

  for y in range(ymin,ymax+1):
    print("x:",pos_new[0],"y:",pos_new[1])
    pos_new[1] = y
    pos_wire += 1
    img.putpixel(pos_new,wire.getpixel((pos_wire,0)))
  
  xmax -= 1

  for x in range(xmax,xmin - 1, -1):
    print("x:",pos_new[0],"y:",pos_new[1])
    pos_new[0] = x
    pos_wire += 1
    img.putpixel(pos_new,wire.getpixel((pos_wire,0)))

  ymax -= 1

  for y in range(ymax,ymin - 1, -1):
    print("x:",pos_new[0],"y:",pos_new[1])
    pos_new[1] = y
    pos_wire += 1
    img.putpixel(pos_new,wire.getpixel((pos_wire,0)))

  xmin += 1

img.save("spiral.png")
