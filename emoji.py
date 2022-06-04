from hashlib import new
from traceback import format_tb
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
def find_url_images(images_lists: list): # this function is which imagrs has contains data-src with string link ...
    new_lists = [] 
    for i in images_lists:
        new_lists.append(i.get('data-src'))
   
    return new_lists



def download_images(images_lists:set, folder_name:str): # this function which data has src string in inspect ...
    j = 441 # fiile name .. starting ..
    for images in images_lists: # find and link of each src in string ... ad save in the new_lists 
        new_lists = images.get('data-src') # append ech src file link ..

        # get the src link extenstion 
        extension = new_lists[new_lists.rindex('.'): ] # or we can use new_lists[new_lists.rindex(new_lists.find('.)): ]
        if extension.startswith('.png'):
            extension = '.png' # chack the extension and save
        else: continue # if Extension no png then save another
        filename = str(j)+extension # example 1.png , 2.png ....
        res = requests.get(new_lists, stream=True)
        try:
            with open(folder_name+filename, "wb") as files:
                shutil.copyfileobj(res.raw, files)
        except Exception as e:
            print(e)
        j = j+1
    else: speak("Succefully Save all the images ...")
    return None



download_images(set(count_images), os.getcwd()+"\\Apple\\")
# print(" List if Url is : ")