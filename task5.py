import requests
import json
from bs4 import BeautifulSoup
from task4 import movie_details
from task1 import scrap_top_list

top_movies = scrap_top_list()
list=[]

def get_movie_list_details(a):
    for i in a:
        url=i["Link"]
        details=movie_details(url)
        list.append(details)
    
    with open("task5.json","w+") as file:
        json.dump(list, file, indent=4)
    return list

movies_detail_list=get_movie_list_details(top_movies)
   