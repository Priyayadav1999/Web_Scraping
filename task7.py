import json

a=open("task5.json","r")
b=json.loads(a.read())

def movies_director(k):
    dic= { }
    for i in k:
        if "director" in i:
            m=i["director"]
            for j in m:
                if j in dic:
                    dic[j]=dic[j]+1
                elif j not in dic:
                    dic[j]=1

    with open("task7.json","w+") as file:
        json.dump(dic , file, indent=4)
    return dic

movies_director(b)
