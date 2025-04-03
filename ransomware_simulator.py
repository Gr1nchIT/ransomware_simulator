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
parentPath=r""
folderName=r""
# /\    /\      /\      /\      /\      /\
# |     |       |       |       |       |


if (folderName=="" or parentPath==""):
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
        
        #Create random text based on sample text
        textLength=random.randint(200,5000)
        textCounter=0
        text=""
        while textCounter<textLength:
            with open("text.txt", "r") as file: 
                allText = file.read() 
                words = list(map(str, allText.split())) 
            randomText+=random.choice(words) + " "
            textCounter+=1

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
        #Exception if file extension already modified
        try:
            os.rename(fileFullPath, newFileFullPath)
            fileCounter=fileCounter+1
        except:
            print (f"File {fileName} renamed already! Skipping...")
    print(f"Total files extension changed: {fileCounter}")
#END renameFileExtension
#_________________________________________________________________________________________________


#START encryptFiles
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

#END encryptFiles
#_________________________________________________________________________________________________


#******************************************************
print("\n\n")
# CREATE RANDOM FILES
askUser=""
askUser=input("Do you want to create random files? (Y/N): ")
if (askUser.lower()=="y" or askUser.lower()=="yes"):
    try:
        numberOfFiles_DOC=int(input("How many doc files? "))
        numberOfFiles_TXT=int(input("How many txt files? "))
        numberOfFiles_JPG=int(input("How many JPG files? "))
        numberOfFiles_PNG=int(input("How many PNG files? "))
    except:
        print ("An error occured. Enter only integer as answers. Exiting....")
        exit()
    print(f"I am going to create: \n\t- {numberOfFiles_DOC} doc files, \n\t- {numberOfFiles_TXT} txt files, \n\t- {numberOfFiles_JPG} jpg files, \n\t- {numberOfFiles_PNG} png files")
    input("Press any button to continue....")
    print(">> Creating files....")
    #randomTextFiles(10,"docx")
    randomTextFiles(numberOfFiles_DOC,"doc")
    randomTextFiles(numberOfFiles_TXT,"txt")
    randomPicFiles(numberOfFiles_JPG,"jpg")
    randomPicFiles(numberOfFiles_PNG,"png")
    print(">> Files created!") 
else:
    print (f"You answered: {askUser}. Skipping this step....")        

print("\n\n")

# ENCRYPT FILES
askUser=""
askUser=input("Do you want to encrypt the files? (Y/N): ")
if (askUser.lower()=="y" or askUser.lower()=="yes"):
    encryptFiles()
    print(">> Files ecnrypted!")
else:
    print (f"You answered: {askUser}. Skipping this step....")    

print("\n\n")

# MODIFY FILE EXTENSION
askUser=""
askUser=input("Do you want to modify the extension of the files? (Y/N): ")
if (askUser.lower()=="y" or askUser.lower()=="yes"):
    renameFileExtension()
    print(">> Files extension changed!")  
else:
    print (f"You answered: {askUser}. Skipping this step....")   

print("\n\n")

#******************************************************
