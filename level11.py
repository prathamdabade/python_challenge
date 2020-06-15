from PIL import Image

img = Image.open("cave.jpg")

size = width,height = img.size
result = Image.new("RGB", size)

for y in range(height):
	for x in range(y%2,width,2):
		result.putpixel((x,y),img.getpixel((x,y)))

result.save("cave_res.jpg")
