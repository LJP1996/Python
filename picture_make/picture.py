'''
验证码的图片制作
'''
from PIL import Image,ImageFilter,ImageDraw,ImageFont
import random

def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60*4
height = 60
img = Image.new('RGB',(width,height),(255,255,255))
font = ImageFont.truetype("arial.ttf", 36)
# font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(img)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
l=[]
# 输出文字:
for t in range(4):
    m = rndChar()
    draw.text((60 * t + 10, 10), m, font=font, fill=rndColor2())
    l.append(m)
# 模糊:
image = img.filter(ImageFilter.BLUR)
image.show()
print(l)
# image.save('code.jpg', 'jpeg');