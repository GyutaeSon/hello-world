#“Now I need a drink, alcoholic of course, 
# after the heavy lectures involving quantum mechanics.”
# という文を単語に分解し，
# 各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

bunsyo = """ 
Now I need a drink, alcoholic of course, 
after the heavy lectures involving quantum mechanics.
"""

bunsyo = bunsyo.replace(",", "")
bunsyo = bunsyo.replace(".", "")

waketa = bunsyo.split()

counter = []
for i in waketa:
    counter.append(len(i))

print(bunsyo)

print(waketa)

print(counter)