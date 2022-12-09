import os


from tool.files import *
from tool.videos import *
def runCodeformer(weight, background =0):
    inputPath = "./extractedFrames"


    videos = onlyfolders(inputPath)
    print(videos)
    wd= os.getcwd()
    os.chdir("codeformer")
    for video in videos:
        if(background==0):
        	command = "python inference_codeformer.py --face_upsample -w "+ str(weight) + " --input_path ."  +video
        else:
            command = "python inference_codeformer.py --face_upsample -w "+ str(weight) + " --input_path ."  +video + " --bg_upsampler realesrgan "
        print(command)
        os.system(command)
    os.chdir(wd)
if __name__ == '__main__':
    w= 0.8
    runCodeformer(w)
