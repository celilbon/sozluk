word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")


meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "like": "beğenilen şey"
            }


if word in meme_dict.keys():
    print (meme_dict[word])
else:
    print("sözcük yok.")
