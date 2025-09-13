# set = {1,2,4,5,7,6,8,9,3,1,}
# print(set)
# for x in enumerate(set):
#     print(x)
# enumarate - indekslab beradi
# pythonni ozi bilan ornatilgan kutubxonalar yani methodlar bular builtinga methods deyiladi.
# lst = [2, 1, 4, 3, 5, 6, 9, 7, 8, 10]
# print(lst)
# m = sorted(lst)
# print(m)
# tartiblangan royxatni teskari qilish
# n = sorted(lst, reverse=True)
# print(n)

# x mode faylni ochsak 1marta run bersa xato bermidi keyingi martasida xato beradi va ichiga malumot yozib bermidi
# file = open("my_first_file.txt", "x")


# w mode faylni ochsak run bersak keyinchalik hato bermidi va ichida malumot yozsak boladi
# file = open("my_first_file", "w")
# file.write("Hello world")


# a mode ochadi yozadi qoshadi orqasidan keyin run bersak hato bermidi
# file1 = open("my_first_file1.txt", mode="a")
# file1.write("Sayyodbek aqlli bola")


# r mode fileni oqiydi
# read = open("my_first_file1.txt", "r")
# m = read.read()
# print(m)


# file ochishni 2xil usuli bor
# 1. file1 = open("my_first_file2.txt", mode="a")
# 2. with open ("Ziyobek.docs", "a") as Ziyobek:
# with open("document.txt", "a") as sayyodbek:
#      sayyodbek.write("Salom Python")
#      sayyodbek.close()
# with open("students.txt", "a") as sayyodbek:
#      sayyodbek.write("Ziyobek Ziyoberk2 sayodbek sayodbek 2 ozodbek")
#      sayyodbek.close()
#
# read = open("students.txt", "r")
# m = read.read()
# # d = read.readline()
# a = [m]
# # a.append(d)
# # h = read.len()
# d = read.read()
# with open("backup.txt", "a") as sayyodbek:
#      sayyodbek.write(f"malulmotlar {a}")
#      sayyodbek.close()
# print(a)
# print(len(m))
#frotedga bekend harrdoyim json farmatda ma,lumot uzatadi
#jison fayil hardoyim dict class da boladi
import json
#jsonga otkazish uchun 2 qil turib borbular
#dumps - shunchaki dictni ogiradi
#dump - dictni jsonga otkazadi va alaohida ga  yozish beradi
#json dict ga orgirishni 2 xil usuli bor
#loads - shunchaki dict ogriadi
#load  - dict ogirrib aolahiadi ga yoziberadi
# infe = {
#      "ozodbeek" : "yashi oqidi",
#      "sayod" : "yomooon oqidi",
#      "ziyoberk":"yomon oqid "
# }
# info = {
#      "names":["ozoddbek","ziyober","sayodbek"],
#      "age":[16,12,12],
#      "holat":["holati zor","holati hyomaon","holati yomaon"]
# }
#
# m = json.dumps(infe)
# print(m)
# print(type(m))
#
# new_dict = json.loads(m)
# print(new_dict)
# print(type(new_dict))
#
# with open('infe.json', 'w') as my_json:
#      my_json.write = json.load(my_json)
#      new_dict["sayod"] = "sayod"
#      print(new_dict)

import json
info = {
     "ustozim":["janatim ustozim juda  ajoyib juda mmehribon"],
     "Nmae": ["ozodbek","sayodeb","ziyoberk",],
     "agae": [16,12,12],
     "holati":["juda yashi",["ortacha"],["juda yoamon"]]
}
with open('infe.json', 'w') as my_json:
     json.dump(info, my_json, indent=5)
a,b=list(map(int,input("nimadir  kritng").split("nimadir")))
