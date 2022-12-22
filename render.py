import os
from pathlib import Path
from tool.files import *
import moviepy.editor as mp




import glob
def pad(path):
    files =glob.glob(path+"*.png")
    for jpg in files:

        name = jpg.split("\\")[-1].split("/")[-1].zfill(11)
        root = jpg.split("final_results")[0]
        os.rename(jpg,root+"final_results/"+name)




def render():
    try:
        os.mkdir("outputs")
    except:
        pass
    try:
        os.mkdir("extractedAudio")
    except:
        pass
    codeformerResults = onlyfolders("./codeformer/results/")
    print("found codeformer results: ",codeformerResults)
    originalVideos = onlyfiles("./downloads")
    for folder in codeformerResults:
        originalVideoSplit = folder.split("/")[-1]
        
        originalVideoName = originalVideoSplit.rsplit("_",1)[0]

        for j in originalVideos:
            print(Path(j).stem.split(".")[0] ,originalVideoName)
            if(Path(j).stem.split(".")[0] == originalVideoName):
                originalVideo=  j
	
        print(originalVideo)

        my_clip = mp.VideoFileClip(originalVideo)
        audioNameList = originalVideo.split("\\")[-1].split("/")[-1].split(".")
        audioName ="".join(audioNameList[0])
        print(audioNameList , audioName)
        my_clip.audio.write_audiofile("extractedAudio"+ os.sep + audioName +".wav")


        frames = onlyfiles(folder+os.sep+"final_results")
        print(folder, " found frames: ", len(frames))
        framerate = my_clip.fps
        print(framerate)
        pad(folder.replace("./","")+ "/final_results/")
        cwd = os.getcwd()
        command = "ffmpeg -framerate "+ str(framerate)+' -thread_queue_size 512 -i "'+ folder.replace("./","")+ '/final_results/%07d.png" "'+cwd+'/outputs/'+originalVideoName+'.mp4" -i "' +cwd+"/extractedAudio/"+originalVideoName+'.wav"'
        print(command)
        os.system(command)
if __name__ == '__main__':
    render()
