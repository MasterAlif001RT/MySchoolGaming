meme_dict = {"CRINGE": "Sesuatu yang sangat aneh atau memalukan",
             "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
             "WOAW": "Buat yang sangat terkejutkan"
            }
            
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('kata yang dicari tidak tersedia')
