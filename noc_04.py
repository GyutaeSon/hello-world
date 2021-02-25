"""
“Hi He Lied Because Boron Could Not Oxidize Fluorine. 
New Nations Might Also Sign Peace Security Clause. 
Arthur King Can.”という文を単語に分解し，
1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ
"""

bun = """
Hi He Lied Because Boron Could Not Oxidize Fluorine. 
New Nations Might Also Sign Peace Security Clause. 
Arthur King Can.
"""
#文章の．を消す
bun = bun.replace(".", "")
#スペースを基準で分ける
kai = bun.split()
#１文字を取る番号のリスト
check = [1, 5, 6, 7, 8, 9, 15, 16, 19]
#辞書型変数
tori = {}
#順番を数える変数
num = 0
#１文字か２文字を取り番号を値として入れる
for i in kai :
    num = num + 1
    if num in check:
        tori[i[0]] = num
    else :
        tori[i[0]+i[1]] = num

print(kai)

print(tori)