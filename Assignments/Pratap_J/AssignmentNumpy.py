#!/usr/bin/env python
# coding: utf-8

# ## NUMPY
# - create a numpy array of 5 zeros.
#     - check datatype, itemsize and shape of above
# - create a numpy array of ones of shape (5,4)
# - create a matrix of shape 4,5 with numbers from 1-20
# - multiply all elements of above array by 10
# - print odd elements from array
# - replace all even elements by their negative
#   
#   
#   
# - create a linearly spaced matrix M1 of size 4x4 having values in range 1-16
# - create a transpose of above matrix call it M2
# - find sum of above matrix M3 = (M1 + M2)
# - Find Transpose of M3, Call it MT1. Check if M3 == MT1
# - find diffrence of M4 = (M1 - M2)
# - Find Transpose of M4, Call it MT2. Check if M4 == MT2. Also check if M4 == -MT2
#   
# 
# - create a matrix (3x4) R1 of random numbers between 10-40
# - find min and max column wise
# - replace the last column with sum of all the columns
# 
# 
# - create a matrix (3x4) R1 of random numbers between 10-40
# - replace all even elements with nan in R1
# - count number of nan in R1
# 
# 
# 
# - check output of this code  
# `a1 = np.arange(1,10).reshape(3,3)
# a2 = np.arange(11,20).reshape(3,3)
# a3 = np.append(a1,a2)
# print(a3)
# a3 = np.append(a1,a2, axis = 0)
# print(a3)
# a3 = np.append(a1,a2, axis = 1)
# print(a3)
# `
# 

# In[3]:


# create a numpy array of 5 zeros.
# check datatype, itemsize and shape of above

import numpy as np

a = np.zeros(5)
print(a)
print(a.dtype)
print(a.itemsize)
print(a.shape)


# In[27]:


# create a numpy array of ones of shape (5,4)

a = np.ones((5,4))
print(a)


# In[28]:


# create a matrix of shape 4,5 with numbers from 1-20

a = np.random.randint(1,20,(4,5))
print(a)


# In[29]:


# multiply all elements of above array by 10
print(a*10)


# In[40]:


# print odd elements from array

a = np.arange(1,20)

print(a)

odd_values = (a%2 == 1)



# In[59]:


# replace all even elements by their negative

a = np.arange(1,20)
# ans = a*(-1) if (a%2 == 0)
# print(ans)

a[a%2 == 0] *=(-1)
print(a)


# In[68]:


# create a linearly spaced matrix M1 of size 4x4 having values in range 1-16

M1 = np.linspace(1,16,16).reshape(4,4)
print(M1)


# In[69]:


# create a transpose of above matrix call it M2

M2 = M1.T
print(M2)


# In[71]:


# find sum of above matrix M3 = (M1 + M2)
M3 = M1+M2
print(M3)


# In[78]:


# Find Transpose of M3, Call it MT1. Check if M3 == MT1
# find diffrence of M4 = (M1 - M2)
# Find Transpose of M4, Call it MT2. Check if M4 == MT2. Also check if M4 == -MT2


MT1 = M3.T

print(MT1)
if MT1.all() == M3.all():
    print('True')

print()

M4 = M1-M2

print(M4)

MT2 = M4.T

print(MT2)

MT7 = MT2*(-1)

if MT2.all() == M4.all():
    print('True')

if M4.all() == MT7.all():
    print('True')









# In[51]:


# create a matrix (3x4) R1 of random numbers between 10-40
# find min and max column wise
# replace the last column with sum of all the columns


a = np.random.randint(10,40,12).reshape(3,4)

print(a)

print()

print(a.min(axis =1))
print()
print(a.max(axis =1))
print()
print(a[:,3])
print()
print(a.sum())

a[:,3]=a.sum()
print(a)

# b = a[:,3:]
# sum1  = a.sum(axis = 1)
# print(a.sum(axis = 1))
# print()            
# print(sum1+b)


# In[15]:


# create a matrix (3x4) R1 of random numbers between 10-40
# replace all even elements with nan in R1
# count number of nan in R1

R1 = np.random.randint(10,40,12).reshape(3,4)

# R1 = np.arange(10,40,2.5).reshape(3,4)
# R1c = np.array()
# print(R1)
# print()

R1 = R1.astype('float')

R1[R1%2 == 0] = np.nan

print(R1)

print(np.sum(np.isnan(R1)))


# In[140]:


a1 = np.arange(1,10).reshape(3,3)
a2 = np.arange(11,20).reshape(3,3)
a3 = np.append(a1,a2)
print(a3)
a3 = np.append(a1,a2, axis = 0)
print(a3)
a3 = np.append(a1,a2, axis = 1)
print(a3)


# In[8]:



print(dir(np))


# In[64]:


import numpy as np
a = np.arange(0,20).reshape(4,5)
print(a)
# b =a[0,1:3]
# print(b)
# print(a[2,:4])
print(a[:,3:4].shape)


# In[ ]:




