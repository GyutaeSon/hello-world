#行数をカウントせよ．確認にはwcコマンドを用いよ．

c = 0
#ファイルを開いて行ごとに読み、処理する
with open("popular-names.txt", encoding="utf-8") as tf:
    for line in tf:
        c = c + 1 

#ファイルを閉じる
tf.close()

print("行数：", c)
