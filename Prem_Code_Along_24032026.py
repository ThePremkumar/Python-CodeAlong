#Control Flow Assignment

#Question 1
"""
ticket_price = int(input("Enter your ticket price:"))

if ticket_price > 300:
    print("Boom! Enjoy your free popcorn!")
else:
    print("Sorry, the free popcorn offer isn't available for you.")
"""

#Question 2

"""score = int(input("Enter your score, students:"))

if score < 40:
    print("Really sorry you didn't pass.")
else:
    print("You did it! Congrats on passing!")
"""

#Question 3

"""vehicle = input("Enter your vehicle type(car/bike):").lower()
if "car" == vehicle:
    print(f"Parking fee for {vehicle}: ₹50.")
else:
    print(f"Parking fee for {vehicle}: ₹20.")
"""

#Question 4
"""
card = input("Invitation card available? ").lower()

if "yes" == card:
    print("Welcome! Please enter the party.")
else:
    print("Sorry, you do not have access to this event.")
"""

#Question 5
"""
bill_amount = int(input("Enter your bill amount:"))
day = input("Enter today day:").lower()

if "monday" == day:
    discount_amount = bill_amount*0.10
    print(f"Total Bill (After Discount): ₹{bill_amount - discount_amount}")
elif "wednesday" == day:
    discount_amount = bill_amount*0.20
    print(f"Total Bill (After Discount): ₹{bill_amount - discount_amount}")
elif "friday" == day:
    discount_amount = bill_amount*0.30
    print(f"Total Bill (After Discount): ₹{bill_amount - discount_amount}")
else:
    print("Soory! there is no Discount today.")
"""

#Question 6
"""
age = int(input("Enter your age:"))

if age < 18:
    print("Your gym membership is ₹500")
elif age >= 18 and age < 40:
    print("Your gym membership is ₹1000")
else:
    print("Your gym membership is ₹700")
"""

#Question 7
"""
custmoer_order = input ("Order Please (Espresso, Latte, Cappuccino): ")

match  custmoer_order:
    case "Espresso":
        print(f"Your {custmoer_order} is being prepared. Please wait.")
    case "Latte":
        print(f"Your {custmoer_order} is being prepared. Please wait.")
    case "Cappuccino":
        print(f"Your {custmoer_order} is being prepared. Please wait.")
"""

#Question 8
"""
mode_of_travel = input ("Enter the Mode of Travel: bus/flight/train:")

match mode_of_travel:
    case "bus":
        print(f"Mode of Tavel: {mode_of_travel}")
    case "train":
        print(f"Mode of Tavel: {mode_of_travel}")
    case "flight":
        print(f"Mode of Tavel: {mode_of_travel}")
    case _ :
        print("Invalid choice.")
"""

"""#Question 9

price = 50

for quantity in range(1, 11):
    total_price = quantity * price
    print(f"Quantity: {quantity} | Total Price: ₹{total_price}")
"""

#Question 10
"""
game = True
guessing_number = 7

while game:
    guess = int(input("Guess the number: "))

    if guessing_number == guess:
        print("Your guess is correct.")
        game = False
    else:
        print("Better luck next time!, Try Again")
"""
#--------------------------------------------------------
# Addition's 30 Questions
#11. IF Statement
"""
apple_count = int(input("Enter the apples count:"))

if apple_count > 5:
    print("Thank you for buying an apple. A 5% discount has been applied.")

"""

#12. IF Statement
"""
books_kept = int(input("Enter the number of days the book was kept: "))

if books_kept > 7:
    print("You must pay fine amount ₹10.")
"""    

#13. IF Statement
"""
attendance = int(input("Enter your attendance precentage (eg.: 75): "))

if attendance > 75:
    print("Congratulations! You are eligible to participate in sports.")

"""

#14. IF-ELSE Statement
"""
total_cost = int(input("Enter your total bill amount: "))

if total_cost > 1000:
    print("Your order qualifies for free home delivery")
else:
    print("Add just a little more to qualify for free home delivery.")
"""

#15. IF-ELSE Statement
"""
num = int(input("Enter a random number: "))

if (num % 2 == 0):
    print(f"The given number {num} is even")
else:
    print(f"The given number {num} is odd")
"""

#16. IF-ELSE Statement
"""
age = int(input("Enter your age: "))

if age >= 21:
    print("Your eligible for this job.")
else:
    print("Sorry!, Your not eligible for this job.")
"""

#17. IF-ELIDF-ELSE Statement
"""
purchase_amount = int(input("Enter your purchase  amount:"))

if 500 <= purchase_amount <= 1000:
    discount_amount = purchase_amount*0.10
    print(f"Total Bill (After Discount): ₹{purchase_amount - discount_amount}")
elif purchase_amount > 1000:
    discount_amount = purchase_amount*0.20
    print(f"Total Bill (After Discount): ₹{purchase_amount - discount_amount}")
else:
    discount_amount = purchase_amount*0.05
    print(f"Total Bill (After Discount): ₹{purchase_amount - discount_amount}")
"""

#18. IF-ELIDF-ELSE Statement
"""
day = input("Enter today day (Morning, Afternoon, Evening):").lower()

if "morning" == day:
    print("Bread is fresh")
elif "afternoon" == day:
    print("Bread is good")
elif "evening" == day:
    print("Bread is stale")
else:
    print("Soory! there is no bread")

"""

#19. IF-ELIDF-ELSE Statement
"""
mark = int(input("Enter your Mark's: "))
if mark >= 90:
    print("Your Grade is A")
elif 75 <= mark <= 89:
    print("Your Grade is B")
elif 50 <= mark <= 74:
    print("Your Grade is C")
else:
    print("Your fail")
"""

#10. MATCH Case Statements
"""
order = input("Enter your order(Orange, Mango, Pineapple): ").lower()

match order:

    case "orange":
        print(f"Your {order} juice is preparing.")
    case "mango":
        print(f"Your {order} juice is preparing.")
    case "pineapple":
        print(f"Your {order} juice is preparing.")
    case __:
        print("Order the following items: Orange, Mango, and Pineapple.")
"""

#11. MATCH Case Statements
"""
category = input("Enter the book category (Fiction, Non-Fiction, Comics): ")

match category:
    case "Fiction":
        print("You can find Fiction books in Section A.")
    case "Non-Fiction":
        print("You can find Non-Fiction books in Section B.")
    case "Comics":
        print("You can find Comics in Section C.")
    case _:
        print("Category not found. Please ask the front desk.")
"""

#12. MATCH Case Statements
"""
number = int(input("Enter the number 1 to 7: "))

match number:
    case 1:
        print(f"Represent {number} as Monday.")
    case 2:
        print(f"Represent {number} as Tuesday.")
    case 3:
        print(f"Represent {number} as Wednesday.")
    case 4:
        print(f"Represent {number} as Thursday.")
    case 5:
        print(f"Represent {number} as Friday.")
    case 6:
        print(f"Represent {number} as Satday.")
    case 7:
        print(f"Represent {number} as Sunday.")
    case _:
        print("Kindly choose the number 1 to 7.")
"""

#13. For loop
"""
for i in range(1, 21):
    print(f"Roll no.: {i}")
"""

#14. For loop
"""
for i in range(1, 11):
    print(f"Square of {i}*{i}={i*i}")
"""

#15. For loop
"""
for i in range(1, 6):
    print(f"Table {i}")
"""

#16. WHILE loop
"""
i = 1
while i <=5:
    print(i)
    i+=1
"""

#17. WHILE loop
"""
amount = 0
while amount <= 500:
    print(f"₹{amount}")
    amount += 100
"""

#18. WHILE loop
"""
gameOn = True

while gameOn:
    user_choice = input("Enter anything: ")
    if user_choice == "quit":
        gameOn = False
        print("Game is over")
    else:
        print("If you end the game enter the 'quit'")
"""

#19. List
"""
fruits = ["apple", "banana", "mango"]

for item in fruits:
    print(item)
"""

#20. List
"""
number = [12, 45, 23, 67]
number.sort()
print(number[-1])
"""

#21. List
"""
student_name= ["Prem", "kumar", "Hari"]
student_name.append("Rahul")
print(student_name)
"""

#22. Tuples
"""
marks = (78, 85, 90)

for mark in marks:
    print(mark)
"""

#23. Tuples
"""
check_tuple = (10, 20, 30, 40, 50)

x = check_tuple.count(50)

if x > 0:
    print("50 is exists.")
else:
    print("50 is not exists.")
"""

#24. Tuples
"""
employee_id = (101, 102, 103, 104)
print(len(employee_id))
"""

#25. Sets
"""
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)
"""

#26. Sets
"""
subjects = {"Maths", "Science", "English"}
subjects.remove("Science")
print(subjects)
"""

#27. Sets
"""
A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B))
"""

#28. Dictionaries
"""
student = {"name": "Ravi", "age": 20}
print(student["name"])
"""

#29. Dictionaries
"""
prices = {"pen": 10, "pencil": 5, "eraser": 3}
print(prices)
"""

#30. Dictionaries
"""
student = {"name": "Asha", "age": 18}
student.update({"age": 19})
print(student)
"""