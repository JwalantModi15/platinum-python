import os
import shutil
def createfolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
def move(folder_name,files):
    for file in files:
        shutil.move(file,f"{folder_name}/{file}")



if __name__=='__main__':
    s = r'' # Here path of Directory
    os.chdir(s)    
    files = os.listdir()
    files.remove("Arrange files in Appropriate Folder.py")
    
    createfolder("Docs")
    # createfolder("Imgs")
    docExt = ['.txt','.docx','.pdf']
    imgExt = ['.png','.ico','.jpg']
    docs = []
    # docs = [file for file in files if os.path.splitext(file)[1].lower() in docExt]
    for file in files:
        if os.path.splitext(file)[1].lower() in docExt:
            docs.append(file)       

    # imgs = [file for file in files if os.path.splitext(file)[1].lower() in imgExt]
    move("Docs",docs)
    # move("Imgs",imgs)


    
