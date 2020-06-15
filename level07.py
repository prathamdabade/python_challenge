from PIL import Image

img = Image.open("oxygen.png")
size = w, h = 629, 95

y=48
end = 607
step = 7
string = []
for x in range(0,end,step):
	string.append(chr(img.getpixel((x,y))[0]))

string = "".join(string)
print(string)

new_list = [105, 110, 116, 101, 103, 114, 105, 116, 121]

new_string = ""
for item in new_list:
	new_string += chr(item)

print(new_string)