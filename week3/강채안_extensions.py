#!/usr/bin/env python
# coding: utf-8

# In[5]:


file_name = input("file name (check your file's extenstion): ")
name = file_name.lower().split('.')[0]
extension = file_name.lower().split('.')[-1]

extension_list = ['gif', 'jpg', 'jpeg', 'png', 'pdf', 'txt', 'zip']

if extension in extension_list:
    file_suffix = '.image/' + extension
    print("file's media type: " + name + file_suffix)
    
#     각각 미디어타입 결정해야 하는데.. 일단 하나로 통일했습니다..ㅎ(게으름 이슈)
#     print('.image/' + extenstion)

else:
    print('application/octet-stream')


# In[ ]:




