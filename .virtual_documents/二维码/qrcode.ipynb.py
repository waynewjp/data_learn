import qrcode


# 方法1
def qr_code_1():
    #调用qrcode的make()方法传入url或者想要展示的内容
    img = qrcode.make('hello,world')
    print(img)
    #保存
    with open(r'test1.png', 'wb') as f:
        img.save(f)


if __name__ == '__main__':
    qr_code_1()



