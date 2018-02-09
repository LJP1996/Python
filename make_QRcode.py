import qrcode

def make_code(text):
    image = qrcode.make(text)
    image.save(r"C:\Users\鹏COMPUTER\Desktop\s.png")
    image.show()
    print("image already save: \鹏COMPUTER\Desktop\s.png")

if __name__ == '__main__':
    text = input("请输入你想说的话:")
    make_code(text)
