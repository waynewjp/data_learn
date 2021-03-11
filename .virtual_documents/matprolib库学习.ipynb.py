import matplotlib.pyplot as plt


plt.plot([3,1,4,5,2])
# 输入的一维数组是Y轴，X轴是元素的索引，【0，1，2，3，4】
plt.ylabel('grade')
plt.show()
plt.savefig('/home/www/jupyter_lab/素材/test',dpi=600) #默认是png格式



#两个参数，一个x，一个y
plt.plot([0,2,4,6,8],[3,1,4,5,2])
plt.ylabel('成绩')
#axis设定横纵坐标尺度：-1,10表示x轴坐标从-1到10，0,6表示y轴从0-6
plt.axis([-1,10,0,6])
plt.show()



