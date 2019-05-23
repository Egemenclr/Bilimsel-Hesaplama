
# coding: utf-8

# In[ ]:


def f(x,y):
    return -y/x
h=float(input("h:"))
y4=3/4
sonuc=y4
iterasyon=int(input("kaca kadar"))
for i in range(4,iterasyon):
    sonuc+=f(i,sonuc)*h
sonuc


# In[9]:


def f(x,y):
    return -y/x
h=float(input("h:"))
y4=3/4
t=y4
sonuc3=y4
iterasyon=int(input("kaca kadar"))
for i in range(4,iterasyon):
    t+=f(i,t)*h
    sonuc3+=((f(i,sonuc3)+f(i+1,t))*h)/2
sonuc3

