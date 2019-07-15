import os	#List Directories
import platform		#Identify OS (Similar to 'os' above)
import re 	#Split String
#Pip install google_images_download
from google_images_download import google_images_download   #Importing Image Search Library
#Pip install image
from PIL import Image 	#Conver To Ico
import configparser 	#Edit INI Files


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
		folderCommand = "attrib +s " + "\"" + path.replace("\\", "/") + "/" + file + "\""
		os.system(folderCommand)

		return fileName


#Lists items in given directory
for item in os.listdir(path):
	if (os.path.isfile(os.path.join(path, item)) == False): #Filters to only capture Folders
		folders.append(re.split('\.|\(',item)[0]) #Filter "(" and "." from folder name


response = google_images_download.googleimagesdownload()   #class instantiation

for file in folders:
	fileName = create_ini_files(path, file)

	#Only Download if ini file does not exist
	if(fileName):
		#Download Image of Folder
		arguments = {"keywords": file + " Movie Poster","limit":1,"print_urls":True, "output_directory": path, "image_directory": file}   # "format": 'ico's
		paths = response.download(arguments)   #passing the arguments to the function
		print(paths)   #printing absolute paths of the downloaded images

		#Convert Image to ICO
		#original = Image.open('/home/eben/Python/MovieIconsForFolders/Movies/Avatar/1.61OUGpUfAyL._SY679_.jpg') # you can try with whatever format
		#original.save('/home/eben/Python/MovieIconsForFolders/Movies/Avatar/newfavicon.ico') 	# not recognized on XP


#Set icons based on OS
def linuxIcons():
    print ("Linux Wins.\n")

def windowsIcons():
    print ("Windows Wins.\n")


options = {'Linux' : linuxIcons,
           'Windows' : windowsIcons,
}

#options[platform.system()]() #Identify OS and run code based on result