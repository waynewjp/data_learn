import matplotlib.pyplot as plt


plt.plot([3,1,4,5,2])
# 输入的一维数组是Y轴，X轴是元素的索引，【0，1，2，3，4】
plt.ylabel('grade')
plt.show()
plt.savefig('/home/www/jupyter_lab/素材/test',dpi=600) #默认是png格式



import matplotlib
import matplotlib.pyplot as plt
#设置字体为楷体
matplotlib.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
matplotlib.rcParams['axes.unicode_minus']=False   #这两行需要手动设置
#两个参数，一个x，一个y
plt.plot([0,2,4,6,8],[3,1,4,5,2])
plt.ylabel('成绩')
#axis设定横纵坐标尺度：-1,10表示x轴坐标从-1到10，0,6表示y轴从0-6
plt.axis([-1,10,0,6])
plt.show()


import numpy as np
import matplotlib.pyplot as plt

a=np.arange(10)
plt.plot(a,a*1.5,a,a*2.5,a,a*3.5)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

a=np.arange(0.0,5.0,0.02)

plt.subplot(211)
plt.plot(a,np.sin(a))
plt.subplot(2,1,2)
plt.plot(a,np.cos(a),'r--')
plt.show()



