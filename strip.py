import os


from tool.files import *
from tool.videos import *
files = onlyfiles("codeformer/results/coni-006_1.0/final_results")
print(len(files))

for f in files:
	
	n = f.split("/")[-1]
	new = f.split("/")[0:-1]
	new.append( n.lstrip("0"))
	print(new)
	final = ""
	for a in new:
		final+= a + "/"
	final= final[0:-1]
	print(final)
	
	os.rename(f,final)
