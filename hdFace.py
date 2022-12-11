import os


from tool.files import *
from tool.videos import *
def runCodeformer(weight, background =0, overwrite = 0 ):
    inputPath = "./extractedFrames"


    videosRaw = onlyfolders(inputPath)
    print("Found input videos: ",videosRaw)
    #########################################################
    if(overwrite==0):
        codeformerResults = onlyfolders("./codeformer/results/")
        originalVideos = onlyfiles("./downloads")
        originalVideosFiltered = []
        for folder in codeformerResults:
            originalVideoSplit = folder.split("/")[-1].split("_")
            originalVideoName =""
            for i in range(len(originalVideoSplit)-1):
                originalVideoName+=originalVideoSplit[i]
            originalVideosFiltered.append(originalVideoName)
        print("already upscaled: ", originalVideosFiltered)

        videos = []
        for v in videosRaw:
            videoPath =v.split("./extractedFrames"+os.sep)[-1]
            if(videoPath not in originalVideosFiltered):
                videos.append(v)
    else:
        videos = videosRaw
    print("upscaleding: ", videos)
    ############################################################

    wd= os.getcwd()
    os.chdir("codeformer")
    for video in videos:
        if(background==0):
        	command = "python inference_codeformer.py --face_upsample -w "+ str(weight) + " --input_path '."  +video+"'"
        else:
            command = "python inference_codeformer.py --face_upsample -w "+ str(weight) + " --input_path '."  +video + "' --bg_upsampler realesrgan "
        print(command)
        os.system(command)
    os.chdir(wd)

if __name__ == '__main__':
    w= 1
    runCodeformer(w, background = 0, overwrite = 1)
