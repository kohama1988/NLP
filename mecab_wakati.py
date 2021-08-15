import MeCab

tagger = MeCab.Tagger('-Owakati')
print(tagger.parse('私は私のことが好きなあなたが好きです'))