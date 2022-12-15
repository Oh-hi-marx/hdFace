import os
from hdFace import runCodeformer
from render import render

os.system("python extractFrames.py")
runCodeformer(0.8,1)
render()
