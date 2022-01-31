import json
import requests
from bs4 import BeautifulSoup

with open("task1.json","r") as file:
    a = json.loads(file.read())

list=[]
for i in range(len(a)):
    k=a[i]["Year"]
    mod = int(k)%10
    decade=int(k)-mod
    if decade not in list:
        list.append(decade)
# print(list)

dict={ }
for j in range(len(list)):
    list1=[]
    for x in range(list[j],list[j]+9):
        for y in a:
            if y["Year"]==x:
                list1.append(y)
    dict[list[j]]=list1

with open("task3.json","w+") as file_1:
    json.dump(dict,file_1, indent=4)
