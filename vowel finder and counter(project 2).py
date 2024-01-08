#!/usr/bin/env python
# coding: utf-8

# In[4]:


#write a program to check whether a given word contains vowels or not also detail the number of vowels present.
word = input("enter the word=")
count = 0
for x in word:
    if x in ["a","e","i","o","u"]:
        print("yes your word contain vowel=",x)
        count = count + 1
print("total vowel in your word=",count)


# In[ ]:





# In[ ]:




