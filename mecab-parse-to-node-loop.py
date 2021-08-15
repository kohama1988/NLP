import MeCab

tagger = MeCab.Tagger()
print('*'*20)

node = tagger.parseToNode('私は私のことが好きなあなたが好きです。')

while node:
    print(node.surface)
    node = node.next