import numpy as np

L=[1,2,3]
A=np.array([1,2,3])

#--------------------------------------------------
#Vector multiplication
#--------------------------------------------------
A=2*A
#--------------------------------------------------
#List augmentation.  
#--------------------------------------------------
L=2*L

#--------------------------------------------------
#Dot product.  Good idea to look at the books at
#the house and find out what it represents.
#--------------------------------------------------

#-------------------------------------------------
#Inefficient way of doing dot product.
#The following exercise made me realize to 
#press the "return" key after the last line
#of a for block when writing the following
#code in the Python "playground."
#-------------------------------------------------
a=np.array([1,2])
b=np.array([2,1])
dot=0

print "Dot product of vector [1,2] and vector [2,]"
for e, f in zip(a, b):
	dot+=e*f
print dot

#-------------------------------------------------
#Look at the linear algebra and calculus books.
#The books will talk about matrices.  
#
#The following is an example of matrix multi-
#plication.
#-------------------------------------------------
c=a*b
print c

#-------------------------------------------------
#For testing
#-------------------------------------------------
print a

