import zipfile
import string

zip_file = zipfile.ZipFile("channel.zip")
#file = open("channel/90052.txt")

file = zip_file.open("90052.txt")
content = file.read().decode()
file.close()

next_num = content.split()[-1]
#print(next_num)
comments = []

while True:
	try:
		handel = zip_file.open(next_num+".txt")
		content = handel.read().decode()
		next_num = content.split()[-1]
		handel.close()
		comments.append(zip_file.getinfo(next_num+".txt").comment.decode())
		#print(next_num)
	except:
		#print(content)
		break
comments = "".join(comments)
print(comments)