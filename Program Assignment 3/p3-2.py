import os, re, shelve

currentDir = os.getcwd()

workDir = os.path.join(currentDir, "UserLog")

userInfoDict = {}

for filename in os.listdir(workDir):
    pathFilename = os.path.join(workDir, filename)
    print(pathFilename)
    logFile = open(pathFilename)
    logInfo = logFile.read()

    nameFind = re.findall('^(\w+)\s+(\w+)', logInfo)
    ipFind = re.findall('25[0-5]|2[0-4][0-9]|[01]?[0-9]?\.', logInfo)
    emailFind = re.findall('[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+', logInfo)

    print(ipFind)

    userList = [nameFind, ipFind]

    userInfoDict[emailFind[0]] = userList

    logFile.close()

print(userInfoDict)

fh = open('mydata.txt', 'w')

fh.write(str(userInfoDict))

fh.close()
