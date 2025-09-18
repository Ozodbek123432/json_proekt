# import json
# infe = {"isim":"isim 1",
#         "yosh": 23,
#         "ish":"devolomper",
#         "isim":"sayod",
#         "yosh": 12,
#         "ish":"oquvchi"
#         }
# fuuydalanuchi2 ={}
# m = json.dumps(infe)
# print(m)
# print(type(m))
# new_dict = json.loads(m)
# print(new_dict)
# print(type(new_dict))
# with open('info.json', 'w') as my_json:
#      my_json.write = json.load(my_json)
#      new_dict["sayod"] = "sayod"
#      print(new_dict)
# TypeError: operatsiya noto'g'ri turdagi ob'ektga qo'llanilganda ko'tariladi.
#
# ValueError: Funktsiya to'g'ri turdagi, lekin noto'g'ri qiymatga ega argumentni qabul qilganda ko'tariladi.
#
# IndexError: ketma-ketlik indeksi diapazondan tashqarida bo'lganda ko'tariladi.
#
# KeyError: Kalit lug'atda topilmasa ko'tariladi.
#
# FileNotFoundError: Fayl yoki katalog topilmasa ko'tariladi.
#
# Import xatosi: modulni import qilib bo'lmaganda yoki modul nomi topilmaganda ko'tariladi.
#
# AttributeError: Ob'ektda atribut mavjud bo'lmaganda yoki undan foydalanish mumkin bo'lmaganda ko'tariladi.
#
# SyntaxError: Kodda sintaksis xatosi aniqlanganda ko'tariladi.
#
# IndentationError: Indentatsiya xatosi aniqlanganda ko'tariladi.
#
# OverflowError: arifmetik amal natijasi koʻrsatish uchun juda katta boʻlganda koʻtariladi.
#
# MemoryError: Operatsiyani bajarish uchun etarli xotira bo'lmaganda ko'tariladi.
#
# PermissionError: Fayl yoki katalogda amalni bajarish uchun ruxsatlar yetarli boʻlmaganda koʻtariladi.
#
# NameError: o'zgaruvchi nomi mahalliy yoki global miqyosda topilmasa ko'tariladi.
#
# init(self, ...): Yangi ob'ektni ishga tushiradi. Bu usul sinfning yangi nusxasi yaratilganda chaqiriladi.
#
# del(self): ob'ektni buzuvchi. Ob'ekt yo'q qilinganda chaqiriladi. U Python-da kamdan-kam qo'llaniladi, chunki axlat yig'ish avtomatikdir.
#
# str(self): Ob'ektning satr tasvirini qaytaradi. str() usuli bu usulni chaqiradi.
#
# repr(self): Ob'ektning satrli tasviri. Qaytish qiymati Python ob'ektni qayta yaratish uchun bajarishi mumkin bo'lgan satr bo'lishi kerak. repr() usuli bu usulni chaqiradi.
#
# eq(self, other): Ikki ob'ekt teng yoki yo'qligini aniqlaydi. == usuli bu usulni chaqiradi.
#
# ne(self, other): Ikki ob'ekt teng emasligini aniqlaydi. != usuli bu usulni chaqiradi.
#
# lt(self, other): Bir ob'ekt boshqasidan kichik yoki yo'qligini aniqlaydi. < usuli bu usulni chaqiradi.
#
# le(self, other): Bir ob'ekt boshqasidan kichik yoki teng ekanligini aniqlaydi. <= usuli bu usulni chaqiradi.
#
# gt(self, other): Bir ob'ekt ikkinchisidan katta yoki yo'qligini aniqlaydi. > usuli bu usulni chaqiradi.
#
# ge(self, other): Bir ob'ekt ikkinchisidan katta yoki teng ekanligini aniqlaydi. >= usuli bu usulni chaqiradi.
#
# len(self): Ob'ekt uzunligini qaytaradi. len() usuli bu usulni chaqiradi.
#
# getitem(self, key): Qiymatni kalit bo'yicha qaytaradi. obj[key] usuli bu usulni chaqiradi.
#
# setitem(self, key, value): Qiymatni kalit bo'yicha o'rnatadi. obj[key] = qiymat usuli bu usulni chaqiradi.
#
# delitem(self, key): Qiymatni kalit bo'yicha o'chiradi. Del obj[key] usuli bu usulni chaqiradi.
# chaqiradidef kmh_to_ms(kmh):
#     return kmh * 1000 / 3600
#
# # Misol
# kmh = float(input("km/h da tezlikni kiriting: "))
# ms = kmh_to_ms(kmh)
# print(f"{kmh} km/h = {ms:.2f} m/s")
