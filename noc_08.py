#与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#-英小文字ならば(219 - 文字コード)の文字に置換
#-その他の文字はそのまま出力
#この関数を用い，英語のメッセージを暗号化・復号化せよ．

import re

def cipher(moji):
    res = []
    for c in list(moji):
        if re.search(r"[a-z]", c):
            res.append(chr(219-ord(c)))
        else :
            res.append(c)

    bun = "".join(res)
    return bun

sentence = input("英文を入力")

c = cipher(sentence)
print("暗号化",c)
d = cipher(c)
print("復号化",d)