import os	#List Directories
import platform		#Identify OS (Similar to 'os' above)
import re 	#Split String
#Pip install google_images_download
from google_images_download import google_images_download   #Importing Image Search Library
#Pip install image
from PIL import Image 	#Conver To Ico
import configparser 	#Edit INI Files
from pathlib import Path		#Find most recent file (jpg)


icoSize = 256, 256 #ICO Resolution

path = os.getcwd()

folders = []

def create_ini_files(path, name):
	fileName = path + "\\" + name + "\\desktop.ini"

	if(os.path.isfile(fileName)) or (name == ""):
		return False
	else:
		config = configparser.ConfigParser()
		config['.ShellClassInfo'] = {'ConfirmFileOp': '0','NoSharing': '1','IconFile': 'Folder.ico', 'IconIndex': '0'}
		with open(fileName, 'w') as configfile:
			config.write(configfile)

		#Change File attribute to Hide and System
		commandPrompt = "attrib +h +s " + "\"" + fileName.replace("\\", "/") + "\""
		os.system(commandPrompt)
		
		#Change folder attribute to System
		folderCommand = "attrib +s " + "\"" + path.replace("\\", "/") + "/" + name + "\""
		os.system(folderCommand)

		return True


#Lists items in given directory
for item in os.listdir(path):
	if (os.path.isfile(os.path.join(path, item)) == False): #Filters to only capture Folders
		folders.append(re.split('\.|\(',item)[0]) #Filter "(" and "." from folder name


response = google_images_download.googleimagesdownload()   #class instantiation

for movie in folders:
	fileExist = create_ini_files(path, movie)

	#Only Download if ini file does not exist
	if(fileExist):
		#Download Image of Folder
		arguments = {"keywords": movie + " Movie Poster","limit":1,"print_urls":True, "output_directory": path, "image_directory": movie, "prefix": "FolderIcon"}   # "format": 'ico's
		paths = response.download(arguments)   #passing the arguments to the function
		print(paths)   #printing absolute paths of the downloaded images
		for i in os.listdir(path + "\\" + movie):
			if (i.startswith("FolderIcon")):
				#Convert Image to ICO
				original = Image.open(path + "\\" + movie + "\\" + i) # you can try with whatever format
				im_resized = original.resize(icoSize, Image.ANTIALIAS)
				im_resized.save(path + "\\" + movie + "\\" + "Folder.ico", "ICO")

#Set icons based on OS
def linuxIcons():
    print ("Linux Wins.\n")

def windowsIcons():
    print ("Windows Wins.\n")


options = {'Linux' : linuxIcons,
           'Windows' : windowsIcons,
}

#options[platform.system()]() #Identify OS and run code based on result