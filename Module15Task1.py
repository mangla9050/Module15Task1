#!/usr/bin/env python
# coding: utf-8

# In[36]:


'''Q1. Create a function which will take a list as an argument and return the product of all the numbers  after creating a flat list. 
Use the below-given list as an argument for your function. 
list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,  22, 61, 34)}, [56, 'data science'], 'Machine Learning'] 
'''
from functools import reduce
l= [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,  22, 61, 34)}, [56, 'data science'], 'Machine Learning'] 
l1=[]
def test(l):
    for i in l:
        if type(i)==list or type(i)==tuple or type(i)==set:
            for j in i:
                    l1.append(j)
        elif type(i)==dict:
            d=i
            l3=d.values()
            for k in l3:
                if type(k)==list or type(k)==tuple:
                    for m in k:
                        l1.append(m)
                else:
                    l1.append(k)
        else:
            l1.append(i)


    l2=[]
    for i in l1:
        if type(i)==int:
            l2.append(i)
    return reduce(lambda x,y:x*y,l2)
test(l)

        
    


# In[56]:


'''Q2. Write a python program for encrypting a message sent to you by your friend. The logic of encryption  should be such that, for a the output should be z. For b, the output should be y. For c, the output should  be x respectively. Also, the whitespace should be replaced with a dollar sign. Keep the punctuation  marks unchanged. 
Input Sentence: I want to become a Data Scientist. 
Encrypt the above input sentence using the program you just created. 
'''

s='I want to become a Data Scientist.'
s1=s.lower()
encrypt_text=''

dict={'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n','n':'m','o':'l','p':'k','q':'j','r':'i','s':'h','t':'g','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a',' ':'$'}
for c in s1:
    if c in 'abcdefghijklmnopqrstuvwxyz ':
         encrypt_text += dict[c]
    else:
        encrypt_text+=c
print(encrypt_text)
    


# In[ ]:




