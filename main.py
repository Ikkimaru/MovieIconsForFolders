import os	#List Directories
import re 	#Split String
from google_images_download import google_images_download   #Importing Image Search Library
from PIL import Image 	#Conver To Ico


path = '/home/eben/Python/MovieIconsForFolders/Movies'

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
	arguments = {"keywords": file + " Movie Poster","limit":1,"print_urls":True, "output_directory": path, "image_directory": file}   #creating list of arguments
	paths = response.download(arguments)   #passing the arguments to the function
	print(paths)   #printing absolute paths of the downloaded images


#Code From: 
#https://github.com/python-pillow/Pillow/issues/1102#issuecomment-73298481

#original = Image.open('/home/eben/Python/MovieIconsForFolders/Movies/Avatar/1.61OUGpUfAyL._SY679_.jpg') # you can try with whatever format
#original.save('/home/eben/Python/MovieIconsForFolders/Movies/Avatar/newfavicon.ico') # not recognized on XP