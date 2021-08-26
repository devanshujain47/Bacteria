#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Bacteria:
    def __init__(self, category, shape, impactful, x, y):
        self.category = category
        self.shape = shape
        self.impactful = impactful
        self.x = x
        self.y = y
        
        
Bacteria_Game = Bacteria( [ "coccus", "bacillus", "spiral", "coryneform", "filamentous"], ["irregualar", "regular"], 
                          ["less", "moderate", "severe"], 5, 5 )


                         


# In[3]:



print(Bacteria_Game.category)
print(Bacteria_Game.shape)
print(Bacteria_Game.impactful)
print(Bacteria_Game.x)
print(Bacteria_Game.y)


# In[ ]:




