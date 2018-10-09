import numpy as np

class Matrix(object):
  def __init__(self):
    pass
  #第一个循环遍历W矩阵的每一行，用W的每一行分别和x的每一列对应元素相乘，再相加，最后把值放在y列表里
  def mul(self,w,x):
    y = []
    for asix in range(w.shape[0]):
      w_num = w[asix,:]
      for ysix in range(x.shape[1]):
        x_num = x[:,ysix]
        w_x_sum = 0
        for i in range(w.shape[1]):
          w_x_sum += w_num[i]*x_num[i]
    y.append(w_x_sum)
		return y
w_input = np.array([[1,2,3],[4,5,6]],dtype = np.int)
x_input = np.array([[1,2],[4,5],[6,7]],dtype = np.int)

m = Matrix()
y_output = m.mul(w_input,x_input)
#最后将列表y转化为（w的行数，x的列数）尺寸的矩阵
y_output = np.array(y_output).reshape(w_input.shape[0],x_input.shape[1])
print(y_output)

