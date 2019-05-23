
# coding: utf-8

# In[48]:



def fx(x):
    return 2*x**3+x-3
# ileri sonlu
x0=2
h=float(input("h kac olsun:"))

sonuc=(fx(x0+h)-fx(x0))/h
sonuc


# In[47]:


# gsf
x=2
h1=0.01
sonuc1=(fx(x)-(fx(x-h)))/h1
sonuc1


# In[42]:


#msf
x1=2
h2=0.00001
sonuc2=(fx(x1+h2) - fx(x1-h2))/(2*h2)
sonuc2

