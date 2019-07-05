import os	#List Directories
import platform		#Identify OS (Similar to 'os' above)
import re 	#Split String
from google_images_download import google_images_download   #Importing Image Search Library
from PIL import Image 	#Conver To Ico


path = os.getcwd()

folders = []


#Lists items in given directory
for item in os.listdir(path):
	if (os.path.isfile(os.path.join(path, item)) == False): #Filters to only capture Folders
		folders.append(re.split('\.|\(',item)[0]) #Filter "(" and "." from folder name

#for name in folders:
	#print (name)


#CODE FROM
#https://google-images-download.readthedocs.io/en/latest/examples.html

response = google_images_download.googleimagesdownload()   #class instantiation

for file in folders:
	arguments = {"keywords": file + " Movie Poster","limit":1,"print_urls":True, "output_directory": path, "image_directory": file}   # "format": 'ico's
	paths = response.download(arguments)   #passing the arguments to the function
	print(paths)   #printing absolute paths of the downloaded images

#Change images to ICO
#original = Image.open('/home/eben/Python/MovieIconsForFolders/Movies/Avatar/1.61OUGpUfAyL._SY679_.jpg') # you can try with whatever format
#original.save('/home/eben/Python/MovieIconsForFolders/Movies/Avatar/newfavicon.ico') # not recognized on XP

#Set icons based on OS
def linuxIcons():
    print ("Linux Wins.\n")

def windowsIcons():
    print ("Windows Wins.\n")


options = {'Linux' : linuxIcons,
           'Windows' : windowsIcons,
}

options[platform.system()]() #Identify OS and run code based on result