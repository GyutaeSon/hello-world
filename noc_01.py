#「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

moji = "パタトクカシーー"

risuto = []

res = str()

for i in range(len(moji)):
    if i%2 == 0:
        risuto.append(moji[i])

for i in range(len(risuto)):
    res += risuto[i]

print(moji)

print(risuto)

print(res)