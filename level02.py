import requests

url = "http://www.pythonchallenge.com/pc/def/ocr.html"

response = requests.get(url)

content = response.text



content = content.split("-->")[1].split("<!--\n")[1]

symbols = {}

for symbol in content:
	if symbol in symbols:
		symbols[symbol] += 1
	else:
		symbols[symbol] = 1

#print(symbols)
url = []
for symbol in symbols:
	if symbols[symbol] == 1:
		print(symbol)