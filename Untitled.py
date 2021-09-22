#!/usr/bin/env python
# coding: utf-8

# *rrrr*

# 

# In[31]:


type(1.0)


# In[32]:


int(1.0)


# In[35]:


x = int(input())


# In[36]:


type(x)


# In[37]:


import math


# In[39]:


math.ceil(3.5)


# In[43]:


x = int(input())
x2 = x//10
print(x2)


# In[49]:


x = input()
y = int(x * 100) * int(x * 100)

print(y)


# In[51]:


n = int(input())
k = int(input())

x = k % n

print(x)


# In[53]:


n = int(input())
x = 2 ** n

print(x)


# In[54]:


n = int(input())
x = n%10

print(x)


# In[56]:


n = int(input())
x = (n%100)//10

print(x)


# In[58]:


n = int(input())
x = (n//100) + (n%10) + (n%100)//10

print(x)


# In[79]:


n = int(input())
x = (n // 2)*2 + 2
print(x)


# In[64]:


x = "A"
y = x * 100
print(y)


# In[65]:


x = input()
print("Hello, %s!" % (x))


# In[113]:


x = input()
print("Hello, ", x, '!',  sep='')


# In[68]:


x = input()
y = int(x) + 1
z = int(x) - 1

print("The next number for the number %s is %i." % (x, y))
print("The previous number for the number %s is %i." %(x, z))


# In[76]:


v = int(input())
t = int(input())
m = 109
x = (v * t) % m
print(x)


# In[5]:


n = int(input())

print(int(n != 1))


# In[8]:


#X
a = int(input())
b = int(input())
x = (a % b)
print((x == 0)*"YES" + (x!=0)*"NO")


# In[37]:


#V
x = int(input())
a = str(x // 1000)
b = str((x // 100) % 10)
c = str((x % 100) // 10)
d = str(x % 10)

print(int(int(a + b) == int(d + c)))


# In[32]:


#S
a1 = int(input())
a2= int(input())
a3 = int(input())
b1 = int(input())
b2 = int(input())
b3 = int(input())
x = (b1*3600 + b2*60 + b3) - (a1*3600 + a2*60 + a3)
print(x)


# In[54]:


#Q
x = int(input())
ad = x // (3600*24)
a1 = (x // 3600) % 24
a2 = x // 60 -  a1*60 - ad*24*60
a3 = x % 60

c = str(a2 // 10)
d = str(a2 % 10)
e = str(a3 // 10)
f = str(a3 % 10)

print(str(a1) + ":" + c + d + ":" + e + f)


# In[57]:


#W
a = int(input())
b = int(input())
x = (a > b)
print((x == 1)*a + (x!=1)*b)


# In[61]:


#U
h = int(input())
a = int(input())
b = int(input())
d = (h - a) // (a - b)
x = (h - a) % (a - b)
print((d + 1)*(x==0) + (d+2)*(x!=0))


# In[66]:


#R
a = int(input())
b = int(input())
n = int(input())

r = n*a + (n*b)//100
k = (n*b)%100
print(r, k)


# In[111]:


#K
a = int(input())
print(("   _~_    ")*a) 
print(("  (o o)   ")*a)
print((" /  V  \\  ")*a)
print(("/(  _  )\\ ")*a)
print(("  ^^ ^^   ")*a)


# In[71]:


#P
a = int(input())

m = a%(24*60)
h = m//60
l = m%60

print(h, l)


# In[74]:


#T
n = int(input())
m = int(input())
import math
l = math.ceil(m/n)

print(l)


# In[117]:


x=input('smdfnjsn')


# In[116]:


math.pi


# In[118]:


'В ВШЭ стартовала новая программа по Data Science'.find('ВШЭ')


# In[119]:


'В ВШЭ стартовала новая программа по Data Science'.find('mhg')


# In[140]:


s=str(input())
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-1][::2])
print(len(s))


# In[172]:


#F
s=input()
print(s.replace("1", "one"))


# In[13]:


#G
s=input()
x = (s.find('h')) +1
y = (s[::-1].find('h'))*(-1)-1
# !!! y = s.rfind('h')
print(s[:x] + s.replace("h", "H")[x:y] + s[y:])


# In[11]:


#D
s=input()
print(s.replace("@", ""))


# In[166]:


#h
s = input()
s.split()
print(s.split[::2])


# In[205]:


#S2 H

list = input()
res = list.split()
print(' '.join(res[::2]))


# In[4]:


#S2 J

l = list(map(int, input().split()))
res = l[::-1]
#print(res)
print(*res)


# In[177]:


#HW-1 #E
n = int(input())
m = int(input())
print(n//m, n%m)


# In[176]:


#HW-1 #A
n = input()
print(list(map(str, n.split)))


# In[ ]:


#HW-1 #B
n = input()
print(list(map(str, n.split)))


# In[212]:


#S2 I

list = input()
res = set(list.split())

print(len(res))


# In[12]:


#S2 K

a = input()
b = input()

print(len(set(a.split()) & set(b.split())))


# In[14]:


#S2 L

a = input()
b = input()
c = list(set(a.split()) & set(b.split()))
c.sort()
print(' '.join(c))


# from pandas import read_csv, DataFrame
# import statsmodels.api as sm
# from statsmodels.iolib.table import SimpleTable
# from sklearn.metrics import r2_score
# import ml_metrics as metrics
# In [2]:
# dataset = read_csv('tovar_moving.csv',';', index_col=['date_oper'], parse_dates=['date_oper'], dayfirst=True)
# dataset.head()

# In[18]:


from pandas import read_csv, DataFrame
import statsmodels.api as sm
from statsmodels.iolib.table import SimpleTable
from sklearn.metrics import r2_score
import ml_metrics as metrics
#In [2]:
dataset = read_csv('tovar_moving.csv',';', index_col=['date_oper'], parse_dates=['date_oper'], dayfirst=True)
dataset.head()


# In[16]:


from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly import graph_objs as go
init_notebook_mode(connected = True)

def plotly_df(df, title = ''):
    data = []

    for column in df.columns:
        trace = go.Scatter(
            x = df.index,
            y = df[column],
            mode = 'lines',
            name = column
        )
        data.append(trace)

    layout = dict(title = title)
    fig = dict(data = data, layout = layout)
    iplot(fig, show_link=False)

dataset = pd.read_csv('hour_online.csv', index_col=['Time'], parse_dates=['Time'])
plotly_df(dataset, title = "Online users")


# In[19]:


# Import `os` 
import os

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()
cwd

# Change directory 
os.chdir("/path/to/your/folder")

# List all files and directories in current directory
os.listdir('.')


# In[ ]:




