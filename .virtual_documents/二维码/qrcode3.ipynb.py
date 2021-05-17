#-*- coding:utf-8 -*-
import qrcode
import time
from PIL import Image
import matplotlib.pyplot as plt


def qr_code():
    # 实例化QRCode生成qr对象
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
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1
    )
    qr.add_data("2021信通岗位新进员工技能强化班")# 添加数据
    qr.make(fit=True)# 填充数据
    
   # 生成图片
    img = qr.make_image(fill_color="green", back_color="white")
    img = img.convert("RGBA")
    # 添加logo，打开logo照片
    icon = Image.open(r"jupyter_lab/二维码/国网.jpg").convert("RGBA")
     # 获取图片的宽和搞
    img_w, img_h = img.size
    # 参数设置logo的大小
    factor = 3
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    # 重新设置logo的尺寸
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    # 得到画图的x，y坐标，居中显示
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    '''
    img.paste(path,where,mask=None)
    其中，img为image对象；path为所添加图片；where为tuple,如：(x,y)，表示图片所在二维码的横纵坐标
    '''
    # 黏贴logo照
    img.paste(icon, (w, h), icon)
    
    # img.show()# 自动打开图片
    # 终端显示图片
    img.save(r"jupyter_lab/二维码/培训绿码.png")
    plt.imshow(img)
    plt.show()



if __name__ == '__main__':
    qr_code()



