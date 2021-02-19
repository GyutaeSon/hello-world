moji = input("文字列”stressed”を入力")

length = len(moji)

ijom = []

res = str()

for i in range(length):
    ijom.append(moji[-1-i])
    res += ijom[i]


print(moji)

print(ijom)

print(res)