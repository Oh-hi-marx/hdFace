import os

from multiprocessing import Process,  Value
from tqdm.auto import tqdm
from tool.files import *
from tool.videos import *

inputPath = "./extractedFrames"


videos = onlyfolders(inputPath)
print(videos)
