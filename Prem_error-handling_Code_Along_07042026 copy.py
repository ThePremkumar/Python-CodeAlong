#Control Flow Assignment

#Question 1

def movie_ticket_price():
    try:
        ticket_price = int(input("Enter your ticket price: "))

        if ticket_price > 300:
            print("Boom! Enjoy your free popcorn!")
        else:
            print("Sorry, the free popcorn offer isn't available for you.")
    except Exception as error:
        print("Error:",error)

movie_ticket_price()

#Question 2
def student_score():
    try:
        score = int(input("Enter your score, students:"))
        if score > 100:
            raise ValueError("Kindly enter the score for 100.")

        if score < 40:
            print("Really sorry you didn't pass.")
        else:
            print("You did it! Congrats on passing!")
    except Exception as error:
        print("Error:",error)

student_score()

#Question 3
def check_vehicle():
    try:
        vehicle = input("Enter your vehicle type(car/bike):").lower()
        if "car" == vehicle:
            print(f"Parking fee for {vehicle}: ₹50.")
        else:
            print(f"Parking fee for {vehicle}: ₹20.")
    except Exception as error:
        print("Error:",error)

check_vehicle()


#Question 4

def guest_invitation_card():
    try:
        card = input("Invitation card available? ").lower()

        if "yes" == card:
            print("Welcome! Please enter the party.")
        else:
            print("Sorry, you do not have access to this event.")
    except Exception as error:
        print("Error:",error)

guest_invitation_card()

#Question 5

def offer_discount():
    try:
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
    except Exception as error:
        print("Error:",error)
    finally:
        print("Thank you visit agian...")

offer_discount()

#Question 6
def gym_membership_price():
    try:
        age = int(input("Enter your age:"))

        if age < 18:
            print("Your gym membership is ₹500")
        elif age >= 18 and age < 40:
            print("Your gym membership is ₹1000")
        else:
            print("Your gym membership is ₹700")
    except Exception as error:
        print("Error:",error)

gym_membership_price()

#Question 7
def coffee_shop_order():
    try:
        custmoer_order = input ("Order Please (Espresso, Latte, Cappuccino): ")

        match  custmoer_order:
            case "Espresso":
                print(f"Your {custmoer_order} is being prepared. Please wait.")
            case "Latte":
                print(f"Your {custmoer_order} is being prepared. Please wait.")
            case "Cappuccino":
                print(f"Your {custmoer_order} is being prepared. Please wait.")
    except Exception as error:
        print("Error:",error)

coffee_shop_order()

#Question 8

def travel_agency():
    try:
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
    except Exception as error:
        print("Error:",error)

travel_agency()

#Question 9

def price_list():
    try:
        price = 50

        for quantity in range(1, 11):
            total_price = quantity * price
            print(f"Quantity: {quantity} | Total Price: ₹{total_price}")
    except Exception as error:
        print("Error:",error)

price_list()

#Question 10

def guessing_game():
    try:
        game = True
        guessing_number = 7

        while game:
            guess = int(input("Guess the number: "))

            if guessing_number == guess:
                print("Your guess is correct.")
                game = False
            else:
                print("Better luck next time!, Try Again")
    except Exception as error:
        print("Error:",error)

guessing_game()