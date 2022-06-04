from functools import wraps
import requests 
import os
import bs4
import shutil
from jarvis import speak

url = input(" Enter a Url")
response = requests.get(url)

bs = bs4.BeautifulSoup(response.text, "html.parser")
formated_txt = bs.prettify()
# print(formated_txt)

count_images = bs.find_all('img')
# save the all images of the browser in the list ...
print(len(count_images))
# print(count_images)

# with open(".//Apple/lists.py", "w") as files:
#     files.write(count_images)

def download_images(function):
    @wraps(function)
    def wrapper_function(*args):
        new_lists = function(*args) # calling the function ..
        for images in range(len(new_lists)): 
            # check if the image sis endswith .png then downnload continue ..
            extension = new_lists[images]
            if extension is None:
                continue   
            else : extension = '.png'
            filename = str(images)+extension # get the file name t save the file ...
            get_images_dow = requests.get(new_lists[images], stream=True)
            with open(os.getcwd()+"\\Apple\\"+filename, "wb") as files:
                shutil.copyfileobj(get_images_dow.raw,files)
        else: speak(" All file are Suceffuly Downloaded ")   
    return wrapper_function 
@download_images
def find_url_images(images_lists: set): # this function is which imagrs has contains data-src with string link ...
    new_lists = [] 
    for i in images_lists:
        new_lists.append(i.get('data-src'.strip()))
   
    return new_lists



# download_images(set(count_images), os.getcwd()+"\\Apple\\")
find_url_images(count_images)
# print(" List if Url is : ")
