# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

for i in range(1,5):
    print(i*" *")
for i in range(5,0,-1):
    print(i*" *")


str = input("enter your string")
i= len(str)-1
while i >=0:
    print(str[i])
    i-=1