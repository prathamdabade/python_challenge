from PIL import Image

images={}
for i in range(5):
	images[i] = open("image"+str(i)+".jpg","wb")
file = open("evil2.gfx","rb")
content = file.read()
file.close()
print(content)