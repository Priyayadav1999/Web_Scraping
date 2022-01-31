import requests
import json
from bs4 import BeautifulSoup

# URL = "https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/"
def scrap_top_list( ):
    url = "https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/"
    sample = requests.get(url)
    soup = BeautifulSoup(sample.text,"html.parser") # iss object ke throw hum kahi bhi khel sakte hai

    main_div=soup.find("div", class_="body_main container")
    tbody=main_div.find("table", class_="table")

    trs=tbody.find_all("tr")

    list=[]
    for tr in trs:
        dic={}
        td=tr.find_all("td")
        for i in td:
            rank=tr.find("td", class_="bold").get_text()[:-1]
            dic["Rank"]=int(rank)

            rating=tr.find("span",class_="tMeterScore").get_text()[1:3]
            dic["Rating"]=int(rating)

            review=tr.find("td", class_="right hidden-xs").get_text()
            dic["Review"]=int(review)

            movie_name=tr.find("a", class_="unstyled articleLink")["href"][3:]
            dic["Movie_name"]=movie_name

            Year=tr.find("a", class_="unstyled articleLink").get_text()
            year = Year.strip()
            dic["Year"] = int(year[-5:-1])

            url = tr.find("a", class_="unstyled articleLink")["href"]
            link = "https://www.rottentomatoes.com" + url
            dic["Link"] = link
        list.append(dic)

        if {} in list:
            list.remove({})
        

    with open("task1.json" , "w+") as file:
        json.dump( list , file , indent=4)
    
    return list

scrap_top_list(  )