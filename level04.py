import requests


url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
number = str(12345)

while True:
	response = requests.get(url+number)
	content = response.text
	number = content.split(" ")[-1]
	print(number)

## gets peak.html
