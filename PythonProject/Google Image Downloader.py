
#pip install google_images_download


from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {"keywords": "cat",
              "limit": 5,
              "print_urls": True}

paths = response.download(arguments)
print(paths)





# keywors: The item we want to search
# limit: The max number we download
# print_urls: print the website link or not

# And we use “downlaod()” function to start it. The output of program will show you the picture is download success or damage.

# The pictures we download will put in the a new folder (The name is your “keyword”) it created automatically in current folder.