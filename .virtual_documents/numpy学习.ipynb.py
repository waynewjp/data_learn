import numpy as np


a=np.array([[1,2,3,4],[11,22,33,44]])
print(a)


a.shape


a.size


a.dtype


a=[1,22,34,12,33]
x=np.array(a)
print(x)


x=np.array((4,5,6,7))
print(x)


x=np.array([[1,2],[9,3],[0.1,2.2]])
print(x)


np.arange(10)


np.ones((3,4))


x=np.zeros((2,3),dtype=np.int32)
print(x)


np.eye(5)


# 生成多维数组
x=np.ones((2,3,4))
print(x)


print(x.shape)


x=np.linspace(1,10,4)
# 1..10起止位置，4是生成4个元素,默认浮点数
print(x)


y=np.linspace(1,10,4,endpoint=False)
print(y)


# 合并两个一维数组，元素合并，还是个一维数组
c=np.concatenate((x,y))
print(c)


x=np.ones((2,3,4),dtype=np.int32)
print(x)
print('-----2,3,4和3，8总个数不变 ，都是24-----------------')
y=x.reshape((3,8))
print(y)


# 将任何数据降到一维，原来数组不变
z=x.flatten()
print(z)


y=x.astype(np.float)
print(y)


x=np.full((2,3,4),11,dtype=np.int)
print(x)
print('---------多维数组转list-----------')
print(x.tolist())


x=np.array([9,8,7,6,5,4])


x[2]


x[1:5:2] #从下标1到5 ，步长2，切片出来也是一个ndarray数组


x=np.arange(24).reshape((2,3,4))
print(x)


x[1,2,3] #从三维数组，从层按需要索引出元素23来


x[:,1,-3]  # 第一个 : 表示不关心第一个维度，  第二个表示第二个维度取1  ， 第三个表时第三个维度取倒数第三个


x[:,1:3,:]


x[:,:,::2] #仅第三个维度按步长2取值


x=np.arange(24).reshape((2,3,4))
y=np.square(x)
print(x)
print(y)


# 求两个数组的最大值
np.maximum(x,y)


# 数组的比较
x > y


x=np.arange(100).reshape(5,20)
np.savetxt('x.csv',x,fmt='get_ipython().run_line_magic(".1f',delimiter=',')", "")


# 读取csv文件，并显示
import pandas as pd
pd.read_csv("x.csv", encoding="GB2312")


y=np.loadtxt('x.csv',dtype=np.int32,delimiter=',')
print(y)


x=np.arange(100).reshape((2,5,10))
np.save('xx.npy',x)
y=np.load('xx.npy')
print(y)


import numpy as np
s1=np.random.rand(3,4,5)
print(s1)


s2=np.random.randn(3,4,5)
print(s2)


s3=np.random.randint(100,200,(3,4))
print(s3)


# 给定同一个随机数种子，可以再次生成相同的随机数数组，测试中很有用
np.random.seed(10)
s4=np.random.randint(100,200,(3,4))
print(s4)
np.random.seed(10)
s5=np.random.randint(100,200,(3,4))
print(s5)


np.randm
