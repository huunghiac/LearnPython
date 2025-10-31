"""import numpy as np
arr = np.array([10,20,30,40,50,60,90,100])

indices = np.array([1,3,5])
print(arr[indices])
print(arr[1])
cond = (arr % 3 == 0)
print (arr[cond])

x = np.array([1,2,3])
y = np.array([4,5,6])

print (np.add(x,y))"""

"""import numpy as np
dtypes = [("name", "S10"), ("year", int), ('gpa', float)]

values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7), 
           ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]

arr = np.array(values, dtype = dtypes)
print (np.sort(arr, order = 'name'))
print (np.sort(arr, order = ['year', 'gpa']))"""

"""import numpy as np

a = [1, 2, 3, 4]

arr = np.array(a)

print("List in python : ", a)

print("Numpy Array in python :",
      arr)"""""

"""import numpy as np

sample_array_1 = np.array([[0, 4, 2]])

sample_array_2 = np.array([0.2, 0.4, 2.4])

print("Data type of the array 1 :",
      sample_array_1.dtype)

print("Data type of array 2 :",
      sample_array_2.dtype)"""

"""import numpy as np

var = "Geekforgeeks"

arr = np.fromiter(var, dtype = 'U1')

print("fromiter() array :",
      arr)"""

"""import numpy as np

n_arr = np.array([[[10, 25, 70], [30, 45, 55], [20, 45, 7]], [[50, 65, 8], [70, 85, 10], [11, 22, 33]]])
print("Array:")
print(n_arr)

res_arr = n_arr[:,[1]]
print("Accessed Rows:")
print(res_arr)

print ("XQ dth")
arr2 = n_arr[:, [0]]
print(arr2)"""

"""import numpy as np
array = np.arange(0, 6)
re = np.split(array, 2)
print(re)"""
# Python program explaining
# numpy.random.randint() function

"""import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=0, scale=1, size=1000)

plt.hist(data, bins=30, edgecolor='black', density=True)
pdf = norm.pdf(x, loc=loc, scale=scale)  
plt.plot(x, pdf, color='red', label='Theoretical PDF')
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid(True)
plt.show()"""

