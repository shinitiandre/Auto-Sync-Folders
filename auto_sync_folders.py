import sys
import os
import shutil
import time
import datetime

origin = sys.argv[1]
replica = sys.argv[2]
interval = int(sys.argv[3])
try:
    logFile = open(sys.argv[4], 'r+')
except FileNotFoundError:
    logFile = open(sys.argv[4], 'w+')

def getFiles(path): #Function to obtain the files and their respective sizes.
    files = os.listdir(path)
    sizes = []
    for file in files:
        filePath = path+'\\'+file
        size = os.path.getsize(filePath)
        sizes.append(size)
    listFiles = list(zip(files,sizes))
    return listFiles

def moveFile(file): #Function to create the file in the replica folder
    shutil.copy(origin+'\\'+file, replica+'\\'+file)
    resp = "File "+file+" created - "+datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return resp



listFilesOrigin = getFiles(origin)
listFilesReplica = getFiles(replica)
print(listFilesOrigin)
print(listFilesReplica)

for file in listFilesOrigin:
    print(file[0])
    if file not in listFilesReplica:
        x = moveFile(file[0])
        print(x)
        logFile.write("\n"+x)

# while True:
#     time.sleep(2)
#     print(sys.argv[0])