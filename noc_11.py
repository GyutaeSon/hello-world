#タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ

with open("popular-names.txt", encoding="utf-8") as tf:
    bun = tf.read()
    tf.close()

bun = bun.replace("\t", " ")

print(bun)