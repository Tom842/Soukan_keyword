import MeCab
tagger = MeCab.Tagger('-Owakati -d "C:/Program Files/MeCab/dic/ipadic" -u "C:/Program Files/MeCab/dic/ipadic/NEologd.dic"')
result = tagger.parse('私が最近見た映画は、約束のネバーランドでした。')
print(result)