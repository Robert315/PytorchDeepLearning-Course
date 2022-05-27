import numpy as np

# mylist = [1, 2, 3]
# np.array(mylist)
#
# arr = np.array(mylist)
# print(type(arr))

# mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# arr = np.array(mylist)
# print(arr) # to print the matrix
#
# lst = np.arange(0,10,2) # like: for i in range()
# print(lst)
#
# zero_list = np.zeros((4,10))
# print(zero_list)
#
# one_list = np.ones((5,5)) * 4
# print(one_list)
#
# lin_space = np.linspace(0,10,100) # a list with 100 numbers between 0 to 10
# print(lin_space)
#
# eye_list = np.eye(5)
# print(eye_list)
#
# random = np.random.rand(1) # random number between 0-1, if we have (5,5) will give us a 5 5 matrix
# print(random)
#
# random_int = np.random.randint(1,100,10)
# print(random_int)

# arr1 = np.arange(25)
# randarr = np.random.randint(0,50,10)
# # randarr.max()
# #
# # arr1.reshape(5,5)
# # print(arr1)
# print(randarr.dtype)

# arr = np.arange(0,11) # sliceing
# # print(arr[:5])
# new_arr = arr.copy() # create a distinct copy in memory of a array
# print(new_arr)

# arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]]) #create a 2d array with 3 x 3
# print(arr_2d,arr_2d.shape)
#
#                                         #   0  1  2  #
# print(arr_2d[1][1]) # print index 1,1   # [ 5 10 15] # 0
# print(arr_2d[:2,1:])                    # [20 25 30] # 1
#                                         # [35 40 45]]# 2


# arr = np.arange(0,11)
# print(arr>4) # returning a bool
# print(1/arr) # 1 divided by all elements of the array including 1/0. not crushing code, just warning you

# arr_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(arr_2d.sum()) # sum o all elements
# print(arr_2d.sum(axis=0)) # give the sum of all values of columns
# print(arr_2d.sum(axis=1)) # give the sum of all values of rows


########## EXERCISES ##########

# 2. Create an array of 10 zeros

# array = np.zeros(10)
# print(array)

# 3. Create an array of 10 ones

# one_array = np.ones(10)
# print(one_array)

# 4. Create an array of 10 fives

# arr = np.ones(10) + 4
# print(arr)

# 5. Create an array of the integers from 10 to 50

# arr = np.arange(10,51)
# print(arr)

# 6. Create an array of all the even integers from 10 to 50

# arr = np.arange(10,51,2)
# print(arr)

# # 7. Create a 3x3 matrix with values ranging from 0 to 8
#
# matrix = np.arange(9).reshape((3,3))
# print(matrix)

# # 8. Create a 3x3 identity matrix
#
# arr = np.eye(3)
# print(arr)

# # 9. Use NumPy to generate a random number between 0 and 1
#
# random = np.random.rand(1)
# print(random)

# # 10. Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
#
# arr = np.random.randn(25)
# print(arr)

# # 11.Create the following matrix:
# # array([[0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1 ],
# #        [0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2 ],
# #        [0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3 ],
# #        [0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4 ],
# #        [0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5 ],
# #        [0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6 ],
# #        [0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7 ],
# #        [0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8 ],
# #        [0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9 ],
# #        [0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.  ]])
#
# arr = np.arange(1,101) / 100
# print(arr.reshape(10,10)

# # 12. Create an array of 20 linearly spaced points between 0 and 1:
#
# arr = np.linspace(0,1,20)
# print(arr)

#  MATRIX
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]]

matrix = np.arange(1,26).reshape(5,5)

# # 13.
# print(matrix[2:,1:])
# # 14.
# print(matrix[3,4])
# # 15.
# print(matrix[:3,1:2])
# # 16.
# print(matrix[4])
# # 17.
# print(matrix[3:])
# # 18.
# print(matrix.sum())
# # 19.
# print(matrix.std()) # standard deviation of the valules in matrix
# # 20.
# print(matrix.sum(axis=0))
