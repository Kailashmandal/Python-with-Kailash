# elif statement is used to check multiple condition alone with if-else statement

age = int(
    input("Enter your age : ")
)

if age >=1 and age <= 3:
    print("Free ticket")
elif 3<age<=10 :
    print("Ticket charge 100 ")
elif 10<age<=60:
    print("Ticket charge 150 ")
else :
    print("Ticket charge 50 ")    