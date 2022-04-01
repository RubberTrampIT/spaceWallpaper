# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# import modules
import requests

r = requests.get('https://apod.nasa.gov/apod/astropix.html')

print(r.text)