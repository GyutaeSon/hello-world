#スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば”I couldn’t believe that I could actually 
# understand what I was reading : the phenomenal power of the human mind .”）を与え，
# その実行結果を確認せよ

#ランダム
import random

def narabi(bun) :
    #文字列をスペースで区切ってリスト化
    waketa = bun.split()
    res = []
    for i in waketa:
        t = len(i)
        moji = []
        #文字数が4以上か判別
        if t > 4 :
            s = list(i)
            moji.append(s[0])
            #先頭と末尾以外の文字をランダムで選択
            m = s[1:t-1]
            r = ''.join(random.sample(m, len(m)))
            moji.append(r)

            moji.append(s[t-1])
            moji = ''.join(moji)

            res.append(moji)
        else :
            res.append(i)
    #リストを文字列に変更
    out = ' '.join(res)
    return out

sen = """I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."""

kaeta = narabi(sen)

print("原文:",sen)
print("替え:",kaeta)