import os
import random
import string
import base64
from cryptography.fernet import Fernet
import datetime

print("\n")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(f"\t\tTHIS SCRIPT IS FOR TESTING OR EDUCATIONAL PURPOSES ONLY")
print(f"\t\tDO NOT USE IT OR ADJUST IT WITH GOAL TO CAUSE ANY DAMAGE")
print(f"\t\tUSE THIS SCRIPT RESPONSIBLY AND AT YOUR OWN RISK")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("\n")

input("Press any button to continue....")
print("\n")


#-------------> ADJUST THIS DATA <-------------
# |      |       |       |       |       |
# \/     \/      \/      \/      \/      \/
parentPath=r"ADD_PATH_HERE"
folderName=r"GRINCHIT"
# /\    /\      /\      /\      /\      /\
# |     |       |       |       |       |


if folderName=="GRINCHIT":
    print(">> Review the parentPath and folderName attributes and try again.")
    print(">> Quiting the script....bye bye....")
    print("\n")
    quit()

#GLOLBAL VARIABLES
#__________________________________________________________
pictureList=["pic1.jpg","pic2.jpg","pic3.jpg"]
folderFullPath=os.path.join(parentPath,folderName)
fileExtension=".grinch"
todayDate = datetime.datetime.now()
timestamp=(str(todayDate.year) + str(todayDate.month) + str(todayDate.day) +
             str(todayDate.hour) + str(todayDate.minute) + str(todayDate.second))

print("\n")
print(f"Target folder path: {folderFullPath}")
print(f"File extension: {fileExtension}")
print(f"Timestamp: {timestamp}")
print("\n")

input("Press any button to continue....")
print("\n")

print("Creating the target folder....")
#Create Folder
try:
    os.mkdir(folderFullPath)
except OSError as error:
    print(error)
    print("Continuing....")



#START randomTextFiles
def randomTextFiles(numberoffiles, filetype):
    randomText=""
    filesCounter=0
    for numberTextFiles in range(1,numberoffiles+1):
        for textLength in range(20,100): #Create random words
            randomChrLen=random.randint(2,10)
            letters = string.ascii_letters
            randomWord=(''.join(random.choice(letters) for i in range(randomChrLen)) )
            #print("Random word:",randomWord)
            randomText=randomText + " " + randomWord #Create text of the random words

        n = 5 #Size of randomly created ID
        randomTextID=(''.join(["{}".format(random.randint(0, 9)) for num in range(0, n)]))
        fileName="SampleTextFile_" + str(randomTextID) + "." + filetype
        fileFullPath=os.path.join(folderFullPath,fileName)
        #print("Simulation File: {}". format(fileFullPath))

        f = open(fileFullPath, "a")
        f.write(randomText)
        f.close()
        filesCounter=filesCounter+1
    
    print(f"Total {filetype} files created: {filesCounter}")

#END randomTextFiles
#_________________________________________________________________________________________________

        
#START randomPicFiles
def randomPicFiles(numberoffiles, filetype):
    filesCounter=0
    for numberPicFiles in range(1,numberoffiles+1):
        sourceFileName=random.choice(pictureList) #choose randomly a picture from the list
        n = 5 #Size of randomly created ID
        randomTextID=(''.join(["{}".format(random.randint(0, 9)) for num in range(0, n)]))
        fileName="SamplePicFile_" + str(randomTextID) + "." + filetype
        fileFullPath=os.path.join(folderFullPath,fileName)

        with open(sourceFileName,'rb') as picfile1:   #Create a copy of the picture
            with open(fileFullPath,'wb') as picfile2:
                while True:
                    b=picfile1.read(1)
                    if b: 
                        # process b if this is your intent   
                        n=picfile2.write(b)
                    else: break
                filesCounter=filesCounter+1
        
    print(f"Total {filetype} files created: {filesCounter}")

#END randomPicFiles
#_________________________________________________________________________________________________


#START renameFileExtension
def renameFileExtension():
    fileList=os.listdir(folderFullPath)
    fileCounter=0
    print(f"Total files listed: {len(fileList)}")
    for x in range(0,len(fileList)):
        fileName=fileList[x]
        fileFullPath=os.path.join(folderFullPath,fileName)
        newFileName=fileName.split(".")[0] + fileExtension
        newFileFullPath=os.path.join(folderFullPath,newFileName)
        os.rename(fileFullPath, newFileFullPath)
        fileCounter=fileCounter+1
    print(f"Total files extension changed: {fileCounter}")
#END renameFileExtension
#_________________________________________________________________________________________________


#START renameFileExtension
def encryptFiles():
    # key generation
    key = Fernet.generate_key()
    # string the key in a file
    keyFileName="filekey_" + timestamp + ".key"
    with open(keyFileName, 'wb') as filekey:
        filekey.write(key)
    # opening the key
    with open(keyFileName, 'rb') as filekey:
        key = filekey.read()
    # using the generated key
    fernet = Fernet(key)

    

    fileList=os.listdir(folderFullPath)
    fileCounter=0
    print(f"Total files listed: {len(fileList)}")
    print (f"Key File Name: {keyFileName}")
    print (f"Key {key}")
    for x in range(0,len(fileList)):
        fileName=fileList[x]
        fileFullPath=os.path.join(folderFullPath,fileName)
        # opening the original file to encrypt
        with open(fileFullPath, 'rb') as file:
            original = file.read()
        # encrypting the file
        encrypted = fernet.encrypt(original)
        # opening the file in write mode and 
        # writing the encrypted data
        with open(fileFullPath, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
            fileCounter=fileCounter+1

    print(f"Total files encrypted: {fileCounter}")

#END renameFileExtension
#_________________________________________________________________________________________________


#******************************************************
#Adjust this if needed
print(">> Creating files....")
randomTextFiles(50,"docx")
randomTextFiles(50,"doc")
randomTextFiles(50,"txt")
randomPicFiles(50,"jpg")
randomPicFiles(50,"png")
print(">> Files created!")         
input("Click any button to encrypt all files....")
encryptFiles()
print(">> Files ecnrypted!")   
input("Click any button to change file extension....") 
renameFileExtension()
print(">> Files extension changed!")  


#******************************************************
