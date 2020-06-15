import string

char = string.ascii_lowercase
separator = ''

encoded = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
#encoded = "map"
encoded = encoded.split()

decoded=[]

for word in encoded:
	w=[]
	for c in word:
		if not (c == "." or c == "(" or c == ")"):	
			data = "".join([char[(char.find(c)+2)%26]])
		else:
			data = "".join(c)
		w.append(data)
	w = separator.join(w)
	decoded.append(w)
separator =" "
decoded = separator.join(decoded)
print(decoded)

