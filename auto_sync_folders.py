import sys, os, shutil, time, datetime
from pathlib import Path 

origin = sys.argv[1]
replica = sys.argv[2]
interval = int(sys.argv[3])


def getFiles(path): #Function to obtain the files and their respective sizes.
    files = os.listdir(path)
    dicFiles = {}
    for file in files:
        filePath = path+'\\'+file
        info = Path(filePath).stat()
        dicFiles[file] = datetime.datetime.fromtimestamp(info.st_mtime).strftime("%d/%m/%Y %H:%M:%S")
    return dicFiles

def moveFile(file, op): #Function to create the file in the replica folder or update it.
    match op:
        case 0:
            shutil.copy(origin+'\\'+file, replica+'\\'+file)
            resp = "File " + file + " created - " + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        case 1:
            shutil.copy(origin+'\\'+file, replica+'\\'+file)
            resp = "File " + file + " updated - " + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return resp

def delFile(file): #Function to delete the file in the replica folder.
    os.remove(replica+'\\'+file)
    resp = "File " + file + " deleted - " + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return resp

print("Automatic synchronization between folders running.")
while True:
    try:
        logFile = open(sys.argv[4], 'a+')
    except FileNotFoundError:
        logFile = open(sys.argv[4], 'w+')

    listFilesOrigin = getFiles(origin)
    listFilesReplica = getFiles(replica)

    for file in listFilesReplica.keys():
        if file not in listFilesOrigin.keys():
            msg = delFile(file)
            print(msg)
            logFile.write(msg + "\n")

    for file in listFilesOrigin.keys():
        if file not in listFilesReplica.keys():
            msg = moveFile(file,0)
            print(msg)
            logFile.write(msg + "\n")
        elif listFilesOrigin[file] > listFilesReplica[file]:
            msg = moveFile(file,1)
            print(msg)
            logFile.write(msg + "\n")  

    logFile.close()
    time.sleep(interval)
    