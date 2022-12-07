import os
def render(path, framerate):
    wd = os.getcwd()
    os.chdir(wd+ os.sep + path)
    os.system("ffmpeg -framerate %f -i %05d.png Project.mp4"%(framerate))
    os.chdir(wd)
