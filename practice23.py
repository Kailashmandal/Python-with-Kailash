# Write a Python program to sort a list of tuples using Lambda.

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

print("subjectmarks before sorting",subject_marks)

# sorting on bases of the marks 82,88...
subject_marks.sort(key= lambda x: x[1])

print("\nafter soring",subject_marks)


# Write a Python program to sort a list of dictionaries using Lambda.


dic= [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

dic.sort( key= lambda x:x['model'])

print(dic)