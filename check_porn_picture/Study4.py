import sys,PIL.Image as Image

# def Check(url):
img = Image.open(r"C:\Users\鹏COMPUTER\Pictures\Saved Pictures\m.jpg").convert('YCbCr')
w, h = img.size
data = img.getdata()
cnt = 0
for i, ycbcr in enumerate(data):
    y, cb, cr = ycbcr
    if 86 <= cb <= 117 and 140 <= cr <= 168:
        cnt += 1
print('%s %s a porn image.'%("nihao", 'is' if cnt > w * h * 0.3 else 'is not'))

# if __name__ == '__main__':
#     url = "C:\Users\鹏COMPUTER\Pictures\Saved Pictures\m.jpg"
#     Check(url)