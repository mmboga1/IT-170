import os

currentDir = os.getcwd()

workDir = os.path.join(currentDir, "UserLog")

totalSize = 0

for filename in os.listdir(workDir):
    pathFilename = os.path.join(workDir, filename)
    print(pathFilename)

    fileSize = os.path.getsize(pathFilename)
    totalSize += fileSize

print("The total size is " + str(totalSize))
