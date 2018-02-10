from PIL import Image

ascii_char = list("!~#$%^&**()_+`=][\{}|;':<>?/")

#字符与RGB的对应的映射关系
def get_char(r,g,b,alpha=256):
    if alpha == 0 :
        return ' '
    lenght = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/lenght
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    im = Image.open(r"C:\Users\鹏COMPUTER\Desktop\timg.jpg")
    #这里是转换图片的大小，然后第二个参数表示图片的质量，一共有4种，低质量Image.NEARSET,双线性Image.BILINEAR，三次样条插值Image.BICUBIC，高质量Image.ANTIALIAS
    im = im.resize((60,30),Image.NEAREST)
    txt = ""

    for i in range(30):
        for j in range(60):
            #im.getpixel:根据坐标取得RGB对应的r，g，b三个值,这里的getpixel((i,j))的两个括号非常重要
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    print(txt)
    with open(r"C:\Users\鹏COMPUTER\Desktop\m.txt",'w') as f:
        f.write(txt)


"""
txt += get_char(*im.getpixel((j,i)))

返回的是一个元组，这个元组有三个元素，分别对应三个颜色通道（RGB）的值。

* 是一个运算符，对元组使用 * 运算符即为元组拆封操作。元组拆封会返回元祖的所有元素。

所以表达式 *im.getpixel((j,i)) 返回 3 个值，正好对应 get_char() 函数的三个参数。

getpixel() 函数返回什么样的值由图片颜色模式决定：
RGB：3 元素元组
RGBA：4 元素元组
Gray （灰度图）：int 值
"""