import os
try:
    os.mkdir("downloads")
except:
    pass
path = input("youtube url or txt file name? (dont include .txt): ")
if(len(path)>5 and "." in path ):
    print("detected url")
    urls = [path]
else:
    urls = []
    #read txt file
    with open(path+".txt") as f:
        contents = f.readlines()
    for line in contents:
        urls.append(line)
    #remove duplicates
    res = []
    [res.append(x) for x in urls if x not in res]
    urls = res
print(urls)
print("Found %i urls" %len(urls))

currentDir = os.getcwd()
os.chdir("downloads")
for url in urls:
	
	command = 'yt-dlp -o "%(id)s.%(ext)s"'  +' ' + url
	print(command)
	print("\nDownloading ", url)
	os.system(command)
	print("=============")
os.chdir(currentDir)
os.system("python main.py")
