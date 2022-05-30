from ast import And, While
import random
import time

def random_otp(n):
    otp = '0'
    for i in range(n):
        otp = otp+ str(random.choice(range(10)))
    return otp

data = {}
# data2 = {}

print("*"*31)
print("Welcome to Univelcity Bank.")
print("*"*31)

while True:
    print("What would you like to do?\n1. Login\n2. Create Account\n3. Quit")
    user_input = input("::>")

    

    if user_input == "2":
        print("Please enter your first name.")
        first_name = input("::>")
        print("Please enter your last name.")
        last_name = input("::>")
        print("Please create your 4-digit pin.")
        login_pin = input("::>")
        print("Please create your 4-digit transaction pin.")
        transaction_pin = input("::>")
        print('Please enter your initial balance.')
        balance = int(input("::>"))
        acct_no = random_otp(9)

        data2 = {"first_name": first_name,
                 "last_name": last_name,
                 "login_pin": login_pin,
                 "transaction_pin": transaction_pin,
                 "balance": balance}
        data[acct_no] = data2
        

        print("Creating account...")
        time.sleep(1)
        print("Completing setup...")
        time.sleep(1)
        print(f"\nWelcome {first_name}!\nYour account has been created and activated. \nYour Account number is {acct_no}\nCheers\nUnivelcity Bank.\n")

    elif user_input == "1":
        print("\nPlease enter your Account number.")
        accti_no = input("::>")
        print("\nPlease enter your 4-digit login pin.")
        pin = (input("::>"))
        data2[login_pin] = pin
        
        user_acct_no = data.get(accti_no, False)
        user_login_pin = data2.get(pin, False)

        while user_acct_no and user_login_pin:
            print(f'Welcome {first_name}.')
            print("*************************************")
            print("Press 1 to Deposit ")
            print("Press 2 to Withdraw ")
            print("Press 3 to Transfer ")
            print("Press 4 to Check Balance ")
            print("Press 5 to Exit/Quit ")
            print("*************************************")
            choice = input('::>')
            if choice == "1":
                print('Enter deposit amount')
                amount = int(input('::>'))
                data2["balance"] = data2["balance"] + amount
                print(f'You have succesfully deposited {amount}')
                print(f'Your new balance is {data2["balance"]}')
            elif choice == "2":
                print('Enter withdrawal amount')
                amount = int(input('::>'))
                # optionally input balance from user as an integer
                # data2["balance"] = data2["balance"]-amount
                if data2["balance"] > amount:
                    data2["balance"] = data2["balance"]-amount
                    print(f'Withdrawal Successful, your balance is {data2["balance"]}')
                else:
                    print('insufficient funds')
            elif choice == "3":
                print('Enter recipient account number')
                rec_acct_no = input('::>')
                print('Enter amount')
                amount = int(input('::>'))
                print('Enter your transaction pin')
                transaction_pin = input('::>')
                t_pin = data2.get(transaction_pin, False)
                if t_pin:
                    if data2["balance"] < amount:
                        print('Insufficient funds')
                    else:
                        data2["balance"] = data2["balance"]-amount
                        print(f'Transfer Successful your balance is {data2["balance"]}')
                else:
                    print('Wrong transaction pin')
            elif choice == "4":
                print(f'Your balance is {data2["balance"]}')
            elif choice == "5":
                break
            else: print('Invalid input')
        else:
            print("\nInvalid Account number or login pin.")

    elif user_input == "3":
        break
