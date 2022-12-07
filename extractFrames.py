import os

from multiprocessing import Process,  Value
from tqdm.auto import tqdm
from tool.files import *
from tool.videos import *

inputPath = "./downloads"
outputPath = "extractedFrames"
numThreads = 2
processes = []


def extractVideoFrames(file, outputPath, y):
    outDir = outputPath + "/" + file.split(os.sep)[-1].split(".")[0]
    try:
        os.mkdir(outDir)
    except:
        pass
    extractFrames(file, outDir, resolution=(1080, 1920), letterBox=1)
    y.value -= 1


if __name__ == '__main__':
    try:
        os.mkdir(outputPath)
    except:
        pass
    files = onlyfiles(inputPath)

    y = Value('i', 0)

    for i in tqdm(range(len(files)), desc=f'Extracting frames'):
        if(y.value < numThreads):
            y.value += 1
            file = files.pop()
            p = Process(target=extractVideoFrames, args=(file, outputPath, y,))
            p.start()
            processes.append(p)
        for p in processes:
            p.join()
