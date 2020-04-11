#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1
L=[]
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        L.append(i)
print(L)


# In[5]:


#Q2
a=int(input())
b=1
for i in range(1,a+1):
    b=b*i
print(b)


# In[6]:


#Q3
n=int(input())
d={}
for i in range(1,n+1):
    d[i] = i*i
print(d)


# In[11]:


#Q4
from math import sqrt
a=input()
l=a.split(",")
for i in range(0,len(l)):
    l[i]=int(l[i])
    m=int(l[i])
    d=100*m
    b=sqrt(d/30)
    l[i]=int(b)
f=','.join([str(k) for k in l])
print(f)


# In[7]:


#Q5-0
def missing_char(a,n):
    b=''
    for i in range(0,len(a)):
        if i!=n:
            b += a[i]
    return b


# In[8]:


#Q5-1
missing_char('kitten',0)


# In[9]:


#Q5-2
missing_char('kitten',1)


# In[10]:


#Q5-3
missing_char('kitten',4)


# In[12]:


#Q6
a="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
b="abcdefghijklmnopqrstuvwxyz"
c=''
p=len(b)
a=list(a)
for i in range(0,len(a)):
    v=a[i]
    if (v!=' ') and (v!='.') and (v!='(') and (v!=')') and (v!="'") :
        n=b.find(v)
        a[i]=b[n+2-p]
for z in range(0,len(a)):
    c+=a[z]
print(c)


# In[3]:


#Q7
import numpy as np
x= np.array([[0,1],[2,3],[4,5]])
print("Original array elements:")
print(x)
y=x.tolist()
print("Array to list:",y)


# In[5]:


#Q8
import numpy as np
a=np.array([0,1,2])
print("array 1 :" , a)
b=np.array([2,1,0])
print("array 2 :" , b)
print("covarience matrix of array 1 and array 2 :")
covarience_matrix = np.cov(a,b)
print(covarience_matrix)

