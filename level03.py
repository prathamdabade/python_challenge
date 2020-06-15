import requests
import re

url = "http://www.pythonchallenge.com/pc/def/equality.html"

response = requests.get(url)

content = response.text



content = content.split("-->")[0].split("<!--\n")[1]



print(re.findall(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', content))



 