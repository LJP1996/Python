# 判断敏感词汇：
# 北京
# 程序员
# 公务员
# 领导
# 牛比
# 牛逼
# 你娘
# 你妈
# love
# sex
# jiangge

def CheckWords(txt,word):
    l = txt.split(" ")
    x=[]
    for i in word.split():
        x.append(i)
    for i in l:
        m = i.strip()
        if x[0] in m or x[1] in m or x[2] in m:
            print("请注意用词")
        else:
            print("说的挺好")

if __name__ == '__main__':
    txt = input("请输入您的文件内容：")
    word = input("请输入您要判断的词语:")
    CheckWords(txt,word)

# txt= "北京 程序员 公务员 领导 牛比 牛逼 你娘 你妈 love sex jiangge"
# word ="逼 娘 妈"
