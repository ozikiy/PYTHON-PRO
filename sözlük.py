word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }
            
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Aradığınız kelime şuan sözlükte yok")
