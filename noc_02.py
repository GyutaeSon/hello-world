#「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

pat = "パトカー"
taxi = "タクシー"

ketugo = [] 
res = str()

for i in range(4):
    ketugo.append(pat[i])
    ketugo.append(taxi[i])

length = len(ketugo)

for i in range(length):
    res += ketugo[i]

print(res)