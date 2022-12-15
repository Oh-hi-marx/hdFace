import os

from multiprocessing import Process,  Value
from tqdm.auto import tqdm
from tool.files import *
from tool.videos import *


inputPath = "./downloads"
outputPath = "extractedFrames"
numThreads = 16
processes = []


def extractVideoFrames(file, outputPath, y):
    outDir = outputPath + "/" + file.split(os.sep)[-1].split(".")[0]
    try:
        os.mkdir(outDir)
    except:
        pass
    extractFrames(file, outDir, resolution=(1080, 1920), letterBox=1)
    y.value -= 1
def remove_non_ascii(string):
    return ''.join(char for char in string if ord(char) < 128)

if __name__ == '__main__':
    try:
        os.mkdir(outputPath)
    except:
        pass
    ########################## remove non english #########
    filesToExtract = onlyfiles(inputPath)

    for file in filesToExtract:
        print(file)
        result = re.sub(r'[^\x00-\x7f]',r'', file)
        os.rename(file,result)

    ################## skip already extracted
    filesToExtract = onlyfiles(inputPath)
    alreadyExtractedRaw = onlyfolders("extractedFrames")
    alreadyExtracted = []
    for f in alreadyExtractedRaw:
        alreadyExtracted.append(f.split("extractedFrames/")[-1])
    files =[]
    skip =[]
    for f in filesToExtract:
        name = f.split(os.sep)[-1].split(".")[0]
        print(name, alreadyExtracted)
        if(name not in alreadyExtracted):
            files.append(f)
        else:
            skip.append(f)
    print("to extract: ",files)
    print("skipping already extract: ", skip)
    ##########################################
    if(len(files)>0):
        y = Value('i', 0)
        for i in tqdm(range(len(files)), desc=f'Extracting frames'):
            while(1):
                if(y.value < numThreads):
                    y.value += 1
                    file = files.pop()
                    p = Process(target=extractVideoFrames, args=(file, outputPath, y,))
                    p.start()
                    processes.append(p)
                    break
        for p in processes:
            p.join()
