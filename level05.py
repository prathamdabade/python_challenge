import pickle
from urllib.request import urlopen

data = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))

#print(data)

for thing in data:
		print("".join([symbol*times for symbol, times in thing]))