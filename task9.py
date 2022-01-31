import json
import os
import time
import random


k=open("task5.json","r")
k1=json.loads(k.read())

def json_file():
    t=random.randint(1,3)
    for j in k1:
        url="/home/admin123/Desktop/task9/task9(1)"+j["movie_name"]+".json"
        if os.path.exists(url)==True:
            pass
        else:
            d=open(url,"w+")
            data = j
            json.dump(data, d, indent=4)
        time.sleep(t)

json_file()

