#list inside list 2D lists

import numbers


matrix= [ [1,2,3] , [4,5,6],[7,8,9] ]
# iterating over the 2D list
for list in matrix:
    for x in list:
        print(x)


print( matrix[2][0]) # accessing individual ele

print( type(matrix))

# pop() method returns the last element of the list and pop it from the list

last_list = matrix.pop()

print( last_list)
