#!/usr/bin/env python
# coding: utf-8

# In[27]:


# 사이트별 비밀번호 만들기 !

site = 'http://gmail.com'
pass_1 = site[7:-4]
pass_2 = pass_1[:3] + str(len(pass_1)) + str(pass_1.count('e')) + '!'


# In[28]:


pass_2

