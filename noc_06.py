"""
“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，
それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

a = "paraparaparadise"
b = "paragraph"

def ngram(n, bun) :
    res = []
    for it in range(len(bun)) :
        if it + n > len(bun) :
            return res
        res.append(bun[it : it + n])

X = set(ngram(2, a))
Y = set(ngram(2, b))

print("X:", X)
print("Y:", Y)

wa = X | Y
seki = X & Y
sa = X - Y

print("和集合:", wa)
print("積集合", seki)
print("差集合", sa)

qest="’se’というbi-gramがXおよびYに含まれるか:{0}".format('se' in wa)
print(qest)