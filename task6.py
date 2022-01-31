import requests
import json
from bs4 import BeautifulSoup

a=open("task5.json","r")
b=json.loads(a.read())

def movies_language(k):
    dic= { }
    for i in k:
        if "language" in i:
            m=i["language"]
            for j in m:
                if j in dic:
                    dic[j]=dic[j]+1
                elif j not in dic:
                    dic[j]=1
    
    with open("task6.json","w+") as file:
        json.dump(dic , file, indent=4)
    return dic

movies_language(b)




