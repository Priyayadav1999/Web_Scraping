import json

with open("task1.json","r") as file:
    k = json.loads(file.read())

dic={}
for i in range(len(k)):
    list=[]

    for j in range(len(k)):
        if k[i]["Year"] == k[j]["Year"]:
            list.append(k[j])
            
    dic[k[i]["Year"]]=list

with open("task2.json","w+") as file_1:
    json.dump(dic, file_1, indent=4)
    