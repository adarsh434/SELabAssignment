import numpy as np

print(np.array([1,2,3,4,5]))

#Arange 
print(np.arange(1,20,2,dtype='float'))

#Zeroes
print(np.zeros(5))
print(np.zeros((3,2)))
print(np.zeros((3,2),dtype='int'))

#Ones
print(np.ones((2,3),dtype='int'))

#Linspace(start,stop,num)

print(np.linspace(2,7,num=4))
#print(np.linspace(2,7,num=4),dtype=int)
#np.linspace(2,7,num=4),endpoint=False

#Eye--> creates array with diagonal having 1 other side contains zero   
print(np.eye(4))
print(np.eye(2,3))
print(np.eye(4,k=-2))
print(np.eye(4,k=2,dtype='int'))

#Random-  rand(),randn(),ranf(),randint()
print('__________')
print(np.random.rand(6))
print(np.random.rand(4,5))
print()
print(np.random.randn(4,5))
print()
#print(np.random.ranf(4,5)) --> wrong 
#randn()
print(np.random.randn(6))
#ranf()
print(np.random.ranf(2))
print(np.random.ranf(size=(2,1)))
print(np.random.ranf((2,3,4)))
print(np.random.randint(5,size=10))
print(np.random.randint(5,size=(2,4)))
#Indexing 
print('----------------------------')
a=np.array([[1,2,3],[4,5,6]])
print(a[-1][-2])

#In 3D
b=np.array([[[1,2,3],[4,5,6,],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])

#Slicing 