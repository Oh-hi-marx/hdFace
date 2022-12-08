import os


from tool.files import *
from tool.videos import *
def runCodeformer(weight):
    inputPath = "./extractedFrames"


    videos = onlyfolders(inputPath)
    print(videos)
    wd= os.getcwd()
    os.chdir("codeformer")
    for video in videos:
        command = "python inference_codeformer.py --face_upsample -w "+ str(weight) + " --input_path ."  +video
        print(command)
        os.system(command)
    os.chdir(wd)
if __name__ == '__main__':
    w= 0.8
    runCodeformer(w)
