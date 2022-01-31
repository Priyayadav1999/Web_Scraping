import json
import requests
from task1 import scrap_top_list
import os


top_movies=scrap_top_list()

def text_file(a):
    for i in a:
        url="/home/admin123/Desktop/task8/task8(1)"+i["Movie_name"]+".txt"
        if os.path.exists(url)==True:
            pass
        else:
            k=open(url,"w+")
            data = requests.get(i["Link"])
            k.write(data.text)



text_file(top_movies)


