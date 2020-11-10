#!/usr/bin/env python
# coding: utf-8

# In[12]:


class Animal:#parent class
    def __init__(self, name, legs=4, eyes=2):
        self.legs=legs
        self.eyes=eyes
        self.name=name

class Pet(Animal):
    def lives(self):
        return 'lives with humans'

class Wild(Animal):
    def lives(self):
        print("Jungle")

class Herbivores(Wild):
    def eat(self):
        print("Plants")
        
class Carnivores(Wild):
    def eat(self):
        print("Other smaller animals")
        
class Dog(Pet):
    def speak(self):
        return self.name+' says Woof!'
    def breed(self):
        self.breed=breed
    
class Cat(Pet):
    def speak(self):
        return self.name+' says Meow!'
    def loves(self):
        print("Milk")
    
class Lion(Carnivores):
    def speak(self):
        print("Roars!!")
        
class Elephant(Herbivores):
    def speak(self):
        print("Trumpets")
    def colour(self):
        print("Gray")

class Zebra(Herbivores):
    def colour(self):
        print("Black and White stripes")
        
class Monkey(Herbivores):
    def speak(self):
        print("Chatters")
    def colour(self):
        print("Brown")
    def loves(self):
        print("Imitating others")

class Leopard(Carnivores):
    def loves(self):
        print("Runs fast")
    def colour(self):
        print("Has spots")
        
class Deer(Herbivores):
    def colour(self):
        print("Brown with white spots")
    def loves(self):
        print("Fruits and nuts")

class Cow(Pet):
    def colour(self):
        print("Brown, Black, White and others")
    def eats(self, Herbivores):
        self.eats=eats
    
class Horse(Herbivores):
    def colour(self):
        print("Brown, Black, White and others")
    def loves(self):
        print("grams")


# In[13]:


d = Dog("Bruno","Huskie")


# In[3]:


d.speak()


# In[14]:


d.lives()


# In[15]:


e = Elephant("Jumbo")


# In[16]:


e.speak()
e.lives()
e.colour()
e.eat()


# In[ ]:





# In[17]:


c = Cow("Cow")


# In[9]:


c.lives()
c.colour()


# In[10]:


c.lives()


# In[ ]:





# In[ ]:





# In[ ]:




