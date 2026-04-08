#Control Flow Assignment

#Question 1

def movie_ticket_price():
    ticket_price = int(input("Enter your ticket price: "))

    if ticket_price > 300:
        print("Boom! Enjoy your free popcorn!")
    else:
        print("Sorry, the free popcorn offer isn't available for you.")

movie_ticket_price()

#Question 2
def student_score():
    score = int(input("Enter your score, students:"))

    if score < 40:
        print("Really sorry you didn't pass.")
    else:
        print("You did it! Congrats on passing!")

student_score()

#Question 3
def check_vehicle():
    vehicle = input("Enter your vehicle type(car/bike):").lower()
    if "car" == vehicle:
        print(f"Parking fee for {vehicle}: ₹50.")
    else:
        print(f"Parking fee for {vehicle}: ₹20.")

check_vehicle()


#Question 4

def guest_invitation_card():
    card = input("Invitation card available? ").lower()

    if "yes" == card:
        print("Welcome! Please enter the party.")
    else:
        print("Sorry, you do not have access to this event.")

guest_invitation_card()

#Question 5

def offer_discount():
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

offer_discount()

#Question 6
def gym_membership_price():
    age = int(input("Enter your age:"))

    if age < 18:
        print("Your gym membership is ₹500")
    elif age >= 18 and age < 40:
        print("Your gym membership is ₹1000")
    else:
        print("Your gym membership is ₹700")

gym_membership_price()

#Question 7
def coffee_shop_order():
    custmoer_order = input ("Order Please (Espresso, Latte, Cappuccino): ")

    match  custmoer_order:
        case "Espresso":
            print(f"Your {custmoer_order} is being prepared. Please wait.")
        case "Latte":
            print(f"Your {custmoer_order} is being prepared. Please wait.")
        case "Cappuccino":
            print(f"Your {custmoer_order} is being prepared. Please wait.")

coffee_shop_order()

#Question 8

def travel_agency():
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

travel_agency()

#Question 9

def price_list():
    price = 50

    for quantity in range(1, 11):
        total_price = quantity * price
        print(f"Quantity: {quantity} | Total Price: ₹{total_price}")
price_list()

#Question 10

def guessing_game():
    game = True
    guessing_number = 7

    while game:
        guess = int(input("Guess the number: "))

        if guessing_number == guess:
            print("Your guess is correct.")
            game = False
        else:
            print("Better luck next time!, Try Again")

guessing_game()