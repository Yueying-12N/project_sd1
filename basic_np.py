import numpy as np
import matplotlib
import matplotlib.pyplot as plt


out = np.asarray([1,0,1])
print('out is',out,'type is',out.dtype)

out1 = np.asarray([1.0,0.0,1.0])
print('out is',out1,'type is',out1.dtype)

'''Simple array creation'''
A_zeros = np.zeros([3,3])
print('A_zeros is',A_zeros,A_zeros.dtype)
A_ones = np.ones([3,3])
print('A_ones is',A_ones,A_ones.dtype)
a_ones = np.ones([3,1])
print('a_ones is',a_ones,a_ones.dtype)
sp = np.arange(0,9)
print('sp is',sp,sp.dtype)

'''Reshaping'''
print('the shape of A_ones is ',A_ones.shape)
print('the shape of sp is ',sp.shape)

new_sp = np.reshape(sp,[3,3])
print('new_sp is ',new_sp)
new_Aones = np.reshape(A_ones,[-1,1])
print(' new A_ones is ',new_Aones)
new_Aones1 = np.reshape(A_ones,[-1,3])
print(' new A_ones1 is ',new_Aones1)
new_Aones2 = np.reshape(A_ones,[-1,9])
print(' new A_ones2 is ',new_Aones2)
'''"-1" lets python deduce the dimension that makes sense.
If it does not make sense then an error is produced'''

'''Matrix Multiplication and element-wise multiplication'''
B=np.matmul(A_ones,A_ones)  #matric multiply
print('B is ',B)
C=np.multiply(A_ones,A_ones)  #Multiply corresponding elements
print('C is ',C)
D=A_ones.dot(A_ones)  #Calculate the real matrix product,
                      #the same as the definition of matrix
                      #multipliction in linear algebra
print('D is ',D)
E=A_ones*A_ones  #same as np.multiply
print('E is ',E)
F=np.power(A_ones, 2)  #Calculate the power


'''Broadcasting'''
data = np.random.rand(100,5)
mu = np.mean(data,axis=0)
print('the mean of data is',mu)
data_c = data - mu   #despite the difference in shape
                     #the substraction was correctly effectuated
print('the mean of data centerd is ',np.mean(data_c))

'''Matrix manipulation'''
A = np.random.rand(3,4)
print(A)
A_delete = np.delete(A,3,1)
print('delte the last column :',A_delete)

# flatten() returns a copy,will not affect the original matrix
# ravel() returns a view, will affect the original matrix when modified
A_vector = A.flatten()
print('translate A to vector :',A_vector)
Ar1 = A[0]
print('the max of row1 is:',Ar1.max())
Ac2 = A[:,1]
print('the min of column2 is:',Ac2.min())
B = A.copy()
B[0]=[0,0,0,0]
B[1]=[1,1,1,1]
B[2]=[1,1,1,1]
print('B is :',B)
print('A is :',A)


'''Visualization'''
A = np.random.rand(3,4)
plt.imshow(A,interpolation='nearest',cmap='gray')
plt.show()
