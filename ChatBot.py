def chat_bot_system():
    print("Enter Your Name : ", end="")
    name = input()
    print("Hello", name, "Welcome to AASWAD-Restaurent\n")
    print("What would you like to order", name, "\n")

    menu_options = ["Rice-Plate", "Samosa", "Vada-Pav", "Chole-Bhature", "Pohe"]
    q_count = [0] * len(menu_options)
    
    while True:
        for i, option in enumerate(menu_options):
            print("Option", i + 1, ":", option)

        print("\nI would like to have option : ", end="")
        opt = int(input()) - 1
        if opt >= len(menu_options):
            print("Display relevant query")
            continue
        
        print("\nYou Confirm order :", menu_options[opt])
        q_count[opt] += 1
        if q_count[opt] >= 5:
            break

        order = input("Do you want anything else (yes/no): ").strip().upper()
        print()
        if order == "YES":
            continue
        else:
            break

    your_order(menu_options, q_count)
    print("\nYour total bill is", total_bill(q_count))
    print("\nThanks for your order!")

def total_bill(q_count):
    ans = 0
    prize = [50, 25, 25, 55, 25]
    for i in range(len(q_count)):
        ans += q_count[i] * prize[i]
    return ans

def your_order(menu_options, q_count):
    print("Your Order is : ")
    for i in range(len(q_count)):
        if q_count[i] > 0:
            print(menu_options[i], q_count[i])

def main():
    chat_bot_system()

if __name__ == "__main__":
    main()

# OUTPUT :

# Enter Your Name : Prathmesh
# Hello Prathmesh Welcome to AASWAD-Restaurent

# What would you like to order Prathmesh

# Option 1 : Rice-Plate
# Option 2 : Samosa
# Option 3 : Vada-Pav
# Option 4 : Chole-Bhature
# Option 5 : Pohe

# I would like to have option : 1

# You Confirm order : Rice-Plate
# Do you want anything else (yes/no): no

# Your Order is :
# Rice-Plate 1

# Your total bill is 50

# Thanks for your order!
