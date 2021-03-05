from PIL import Image
# image是PIL中代表一个图像的类
import numpy as np


a=np.array(Image.open("/home/www/jupyter_lab/素材/图片1.jpg"))
print(a.shape,a.dtype)


b=[255,255,255]-a
im=Image.fromarray(b.astype('uint8'))
im.save('/home/www/jupyter_lab/素材/图片2.jpg')


a=np.array(Image.open('/home/www/jupyter_lab/素材/图片1.jpg').convert('L')

