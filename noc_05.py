
"""
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，
”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
"""

sentence = "I am an NLPer"

n_value = 2

#n-gramを作る関数
def ngram(n_value, bunsyo):
    waketa = bunsyo
    #文字列か判断
    if(type(waketa) == str) :
        waketa = waketa.replace(",", "")
        waketa = waketa.replace(".", "")
        waketa = waketa.replace(";", "")
        waketa = waketa.replace(" ", "")
        print(waketa)
    #文字列やリストの長さ
    check = len(waketa)

    res= []
    num = 0

    for i in range(check) :
        res.append([])
        num = i
        for s in range(n_value) :
            if i+s >= check:
                res[i].append(waketa[i - num])
                num = num - 1
            else :
                res[i].append(waketa[num+s])
    return res

print("単語bi-gram")
print(ngram(n_value, sentence.split()))

print("文字bi-gram")
print(ngram(n_value, sentence))