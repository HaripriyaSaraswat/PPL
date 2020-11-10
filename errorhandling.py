#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(n1,n2):
    print(n1+n2)


# In[2]:


add(10,20)


# In[3]:


num1=10


# In[6]:


num2=int(input("Please enter a num   "))


# In[7]:


result=add(num1,num2)


# In[12]:


try:
    result=10+a
    print(result)
except:
    print("u r not adding correctly")

result 
# In[ ]:





# In[9]:


try:
    f=open('testfile','r')
    f.write("Write a test line")
except TypeError:
    print("There was a type error")
except OSError:
    print("Hey you have an OS error")
finally:
    print("I always run")
    


# In[10]:


def ask_for_int():
    while True:
        try:
            result=int(input("Please provide a number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("End of try/except/finally")


# In[11]:


ask_for_int()


# In[ ]:




