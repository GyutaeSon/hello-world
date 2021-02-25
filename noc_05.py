
"""
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，
”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
"""

sentence = "I am an NLPer"

#n-gramを作る関数
def ngram(n, waketa):
    res= []
    for i in range(len(waketa)) :
        if i+n > len(waketa):
            return res
        res.append(waketa[i : i+n])


print("単語bi-gram")
print(ngram(2, sentence.split()))

print("文字bi-gram")
print(ngram(2, sentence))