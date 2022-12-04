numbers=[1,2,3,4,5,6]
print(
    max(numbers),min(numbers)
)

#################

names=['karan','Kailash','Mohit']

def max_LenName(name):
    return len(name)

print(
    #max length of any name in names[]
max(names,key=max_LenName)
)


# with lambda function
print(
    #min length of any name in names[]
min(names,key= lambda name: len(name))
)

# get max and min from the list of dictionaries

students=[
    {'name':'Kailash','score':65},
    {'name':'Kalas','score':55},
    {'name':'Karan','score':95}
]

print(
    max(
        students,
        key= lambda student: student['score']
    ).get('name')
)
