import csv

dict_from_csv = {}

with open('C:/Users/tom84/Git/wordcount_dic.csv',encoding='utf-8', mode='r') as wc:
    rr = csv.reader(wc)
    dict_from_wc = {rows[0]:rows[1] for rows in rr}

#print(dict_from_wc)


with open('C:/Users/tom84/Git/csv_file.csv',encoding='utf-8', mode='r') as inp:
    reader = csv.reader(inp)
    dict_from_inp = {rows[0]:rows[1] for rows in reader}

#print(dict_from_inp)

dict_from_wc_copy = dict_from_wc.copy()

for key in dict_from_wc.keys():
    if key not in dict_from_inp:
        removed = dict_from_wc_copy.pop(key)

#辞書リストを取り出し、降順に並び替え
Keyword_Count = []
for item in dict_from_wc_copy.items():
    Keyword_Count.append(item)


#CSV出力
with open("Keyword_Count.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f, lineterminator="\n")
    writer.writerows(Keyword_Count)


