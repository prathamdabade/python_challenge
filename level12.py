from PIL import Image

images={}
for i in range(5):
	images[i] = open("image"+str(i)+".jpg","wb")
file = open("evil2.gfx","rb")
content = file.read()
file.close()


for b in range(0,len(content),5):
	for i in range(5):
		images[i].write(bytes([content[b+i]]))

for i in range(5):
	images[i].close()
# Check for file type	
