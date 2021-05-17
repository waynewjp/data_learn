import qrcode


def qr_code_2():
    '''
    参数 version 表示生成二维码的尺寸大小，取值范围是 1 至 40，最小尺寸 1 会生成 21 * 21 的二维码矩阵，
    version 每增加 1，生成的二维码就会添加 4 个单位大小，例如 version 是 2，则生成 25 * 25 尺寸大小的二维码。

    参数 error_correction 指定二维码的容错系数，分别有以下4个系数：
    ERROR_CORRECT_L: 7get_ipython().run_line_magic("的字码可被容错", "")
    ERROR_CORRECT_M: 15get_ipython().run_line_magic("的字码可被容错", "")
    ERROR_CORRECT_Q: 25get_ipython().run_line_magic("的字码可被容错", "")
    ERROR_CORRECT_H: 30get_ipython().run_line_magic("的字码可被容错", "")

    参数 box_size 表示二维码里每个格子的像素大小。
    参数 border 表示边框的格子宽度是多少（默认是4）
    '''
    # 实例化QRCode生成qr对象
    qr=qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1
    )
     # 调用qrcode的make()方法传入url或者想要展示的内容
    qr.add_data("2021信通岗位新进员工技能强化班")
    qr.make(fit=True)# 填充数据
    img = qr.make_image() # 生成图片
    img.save(r"jupyter_lab/二维码/test2.png")



if __name__ == '__main__':
    qr_code_2()






