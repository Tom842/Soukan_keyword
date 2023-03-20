#https://your-3d.com/pytho-mecab-frequencywords/
#テキストファイルから頻出単語を抽出する

import MeCab
import csv

wordFreq_dic = {}
wordcount_output = []

#解析テキスト
#テキストファイルを読み込み

#対象のテキストファイルを指定
textfile = open('C:/Users/フォルダ名/Git/総監_過去問_H26-R04/H25.txt', 'r', encoding='UTF-8')
text = textfile.read()

#単語頻出度カウント
def WordFrequencyCount(word):
        if word in wordFreq_dic:
            wordFreq_dic[word] +=1
        else:
           wordFreq_dic.setdefault(word, 1)
        return wordFreq_dic

#特定の品詞の単語を抽出
mecab = MeCab.Tagger('-Owakati -d "C:/Program Files/MeCab/dic/ipadic" -u "C:/Program Files/MeCab/dic/ipadic/user.dic"')
mecab.parse('')
node = mecab.parseToNode(text)

#Mecab処理をファイルに保存(temp)
with open("Mecab_node.txt", "w", encoding="utf-8") as n:
    n.write(mecab.parse(text))

while node:
    if node.feature.split(",")[0] == "名詞":
        word = node.surface
        WordFrequencyCount(word)
    elif node.feature.split(",")[0] =="動詞":
        word = node.surface
        WordFrequencyCount(word)
    elif node.feature.split(",")[0] == "形容詞":
        word = node.surface
        WordFrequencyCount(word)
    elif node.feature.split(",")[0] == "形容動詞":
        word = node.surface
        WordFrequencyCount(word)
    else:pass
    node = node.next

#辞書リストを取り出し、降順に並び替え
for item in wordFreq_dic.items():
    wordcount_output.append(item)
wordcount_output = sorted(wordcount_output, key = lambda x:x[1], reverse=True)

#CSV出力
with open("wordcount_dic.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f, lineterminator="\n")
    writer.writerows(wordcount_output)
