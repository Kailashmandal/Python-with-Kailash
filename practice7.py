# Write a Python program to check a triangle is 
# equilateral, isosceles or scalene

first_side , second_side , third_side = input("enter the side saprated by commas ").split(",")
first_side = int(first_side)
second_side=int(second_side)
third_side=int(third_side)

if first_side==second_side== third_side:
    print("equilateral")
elif( (first_side==second_side and first_side != third_side) or (first_side== third_side and second_side!= third_side) or (second_side==third_side and first_side!= second_side)):
    print("isosceles")
else:
    print("scalene")