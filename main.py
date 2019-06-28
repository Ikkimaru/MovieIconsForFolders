import os
from azure.cognitiveservices.search.imagesearch import ImageSearchAPI
from msrest.authentication import CognitiveServicesCredentials

#next(os.walk('.'))[1]

path = '/home/eben/Python'

folders = []

#dirs = os.listdir(path)

#Lists items in given directory
for item in os.listdir(path):
	if (os.path.isfile(os.path.join(path, item)) == False): #Filters to only capture Folders
		folders.append(item)

#for file in folders:
 #  print (file)

#Code from: https://github.com/Azure-Samples/cognitive-services-python-sdk-samples/blob/master/samples/search/image-search-quickstart.py

subscription_key = "1f169e3799c04dea821b180437a86817"
search_term = "canadian rockies"

"""
This application will search images on the web with the Bing Image Search API and print out first image result.
"""
#create the image search client
client = ImageSearchAPI(CognitiveServicesCredentials(subscription_key))
# send a search query to the Bing Image Search API
image_results = client.images.search(query=search_term)
print("Searching the web for images of: {}".format(search_term))

# Image results
if image_results.value:
    first_image_result = image_results.value[0]
    print("Total number of images returned: {}".format(len(image_results.value)))
    print("First image thumbnail url: {}".format(first_image_result.thumbnail_url))
    print("First image content url: {}".format(first_image_result.content_url))
else:
    print("Couldn't find image results!")