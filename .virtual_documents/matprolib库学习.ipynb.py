import matplotlib.pyplot as plt


plt.plot([3,1,4,5,2])
# 输入的一维数组是Y轴，X轴是元素的索引，【0，1，2，3，4】
plt.ylabel('grade')
plt.show()
plt.savefig('/home/www/jupyter_lab/素材/test',dpi=600) #默认是png格式



import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.size']=20

#两个参数，一个x，一个y
plt.plot([0,2,4,6,8],[3,1,4,5,2])
plt.ylabel('成绩',fontpro)
#axis设定横纵坐标尺度：-1,10表示x轴坐标从-1到10，0,6表示y轴从0-6
plt.axis([-1,10,0,6])
plt.show()





import numpy as np
import matplotlib.pyplot as plt

a=np.arange(10)
plt.plot(a,a*1.5,a,a*2.5,a,a*5.5)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

a=np.arange(0.0,5.0,0.02)

plt.subplot(211)
plt.plot(a,np.sin(a))
plt.subplot(2,1,2)
plt.plot(a,np.cos(a),'r--')
plt.show()


import numpy as np
import matplotlib.pyplot as plt

a=np.arange(0.0,5.0,0.02)
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.xlabel('横轴：时间',fontproperties='SimHei',fontsize=15,color='green')
plt.ylabel('纵轴：振幅',fontproperties='SimHei',fontsize=15)
plt.title(r'郑泫渤')
plt.show()


import matplotlib.pyplot as plt
labels='frog','dog','log','hog'
size=[15,30,45,10] #比例
explode=(0,0.1,0,0) #那一块要吐出来

plt.pie(size,explode=explode,labels=labels,autopct='get_ipython().run_line_magic("1.1f%%',shadow=False,startangle=90)", "")
plt.axis('equal') # 饼图变成正圆形
plt.show()


import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
mu,sigma=100,20 #均值、标准差
a=np.random.normal(mu,sigma,size=100)

plt.hist(a,40) # bin,直方的个数，越多越细
plt.title('test gram')

plt.show()



