#-*- coding:utf-8 -*-
import qrcode
import time
from PIL import Image
import matplotlib.pyplot as plt


def qr_code_3():
    # 实例化QRCode生成qr对象
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
    icon = Image.open("logo.jpg").convert("RGBA")
