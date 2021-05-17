import qrcode

# 方法1
def qr_code_1():
    #调用qrcode的make()方法传入url或者想要展示的内容
    img = qrcode.make('https://blog.csdn.net/xc_zhou')
    #保存
    img.save("./img/text1.png")
    # 或者
    with open('./img/test2.png', 'wb') as f:
        img.save(f)
        
qr_code_1()
————————————————
版权声明：本文为CSDN博主「周小董」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/xc_zhou/article/details/80952036