# In[4]:
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

# In[5]:
#0-D array
import numpy as np
arr = np.array(42)
print(arr)

# In[6]:
#1-D array
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)

# In[12]:
#2-D array
import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr)

# In[13]:
#3-D array
import numpy as np
arr = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr)

# In[14]:
#ndim attribute(defining dimension)

import numpy as np

a = np.array(42)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3,4,5],[6,7,8,9,10]])
d = np.array([[[1,2,3],[4,5,6],[7,8,9]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# In[17]:
#access array elements/array indexing

import numpy as np
arr = np.array([1,2,3,4,5])
print(arr[1])
print(arr[0])

# In[18]:
#add 3rd and 4th index

import numpy as np
arr = np.array([1,2,3,4])
print(arr[3]+arr[2])

# In[20]:
#access 2-D arrays

import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print("2nd element of 1st row:",arr[0,1])
print("3rd element of 2nd row:",arr[1,2])

# In[21]:
#slicing

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,])
print(arr[1:5])

# In[22]:
#slicing(w/o start index)

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,])
print(arr[:7])

# In[23]:
#slicing(both start and end not mentioned)

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,])
print(arr[:])

# In[24]:
#slicing(end not mentioned)

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,])
print(arr[2:])

# In[ ]:
#slicing

import numpy as np

# In[29]:
#slicing(negatice)

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[-3:-1])

# In[30]:
#slicing(bichke 2)

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[1:5:2])

# In[36]:
#slicing(every other element from entire array)

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[::2])
print(arr[::3])
print(arr[2::3])

# In[2]:
#slicing 2d array

import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1, 1:4])

# In[3]:
import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0, 1:4])

# In[10]:
import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
element = arr[1,2]
print(element)

# In[11]:
#slicing a row
import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
row_slice=arr[0:2,:]
print(row_slice)

# In[12]:
slicing a column
import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
col_slice=arr[:,1:3]
print(col_slice)
