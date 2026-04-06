#Control Flow Assignment Question

#Assignment 1

"""age = int(input("Enter your age:"))

if age < 18:
    print("Your gym membership is ₹500")
elif age >= 18 and age < 40:
    print("Your gym membership is ₹1000")
else:
    print("Your gym membership is ₹700")"""

#Assignment 2 
#Method 1

"""mode_of_travel = input ("Enter the Mode of Travel: bus/flight/train:")
if mode_of_travel =="bus":
    print(f"Mode of Travel: {mode_of_travel}")
elif mode_of_travel == "train":
    print(f"Mode of Travel: {mode_of_travel}")
elif mode_of_travel == "flight":
    print(f"Mode of Travel: {mode_of_travel}")
else:
    print("Invalid Mode")"""


#method 2

"""match mode_of_travel:
    case "bus":
        print(f"Mode of Tavel: {mode_of_travel}")
    case "train":
        print(f"Mode of Tavel: {mode_of_travel}")
    case "flight":
        print(f"Mode of Tavel: {mode_of_travel}")
    case _ :
        print("Invalid choice.")

n = int(input("Enter the value:"))"""

#Simple task 1

"""for i in range(1, 11):
    print(f"{n}*{i} = {n*i} ")

i = 1
while i<=10:
    print(f"{n}*{i} = {n*i} ")
    i +=1"""


#Simple task 1

while True:
    name = input("Enter the name:")
    if name == "Prem":
        print("Not Access you!")
        break
    else:
        continue

while True:
    answer = input("Will you be my Valentine:")
    if answer == "yes":
        print("I knew it")
        break
    else:
        print("You don't have an option, Darling")
        continue