import os
from azure.cognitiveservices.search.imagesearch import ImageSearchAPI
from msrest.authentication import CognitiveServicesCredentials

#next(os.walk('.'))[1]

path = '/home/eben/Python/MovieIconsForFolders/Movies'

folders = []



#Lists items in given directory
for item in os.listdir(path):
	if (os.path.isfile(os.path.join(path, item)) == False): #Filters to only capture Folders
		folders.append(item)


#CODE FROM
#https://google-images-download.readthedocs.io/en/latest/examples.html

from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

for file in folders:
	arguments = {"keywords": file + " Movie Poster","limit":1,"print_urls":True, "output_directory": path, "image_directory": file}   #creating list of arguments
	paths = response.download(arguments)   #passing the arguments to the function
	print(paths)   #printing absolute paths of the downloaded images