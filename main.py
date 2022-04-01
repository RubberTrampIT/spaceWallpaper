# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# import modules
import requests
import shutil
from bs4 import BeautifulSoup
import os
import ctypes

# Identify daily image URL for download and download locally
def get_image():
    base_url = 'https://apod.nasa.gov/apod/'
    req = requests.get(base_url + 'astropix.html')
    soup = BeautifulSoup(req.content, 'html.parser')
    # html = list(soup.children)[2]
    # body = list(html.children)[3]
    # print(list(body.children)[1])
    imgtag = soup.find('img')
    # print(imgtag['src'])
    img = base_url + imgtag['src']

    res = requests.get(img, stream=True)
    file_name = 'wallpaper.jpg'
    if res.status_code == 200:
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image successfully downloaded: ', file_name)
    else:
        print('Image couldn\'t be retrieved')


# Set downloaded image as Windows wallpaper
def set_wallpaper():
    path = os.getcwd() + '\\wallpaper.jpg'
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

get_image()
set_wallpaper()