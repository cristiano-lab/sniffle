meme_dict = {
    "char" : "karakter",
    "skin" : "kaplama",
    "skill" :"yetenek",
    "gg" : "iyi oyun",
    "drop" : "almak",
    "nt" : "iyi deneme"
}

kelimemiz = input("Öğrenmek istediğiniz kelimeyi yazın")

if kelimemiz in meme_dict.keys():
     print(meme_dict[kelimemiz])
else:
    print("Böyle bir kelime sözlükte yok")
