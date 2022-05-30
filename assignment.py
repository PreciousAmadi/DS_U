import random
import time
#you can give your random number generating function any name, I left mine as random_otp
def random_otp(n):
    #simply add 0 to the empty otp string so when 9 random numbers
    #are generated, it will always begin with 0, thereby making it 10 random numbers
    otp = '0'
    for i in range(n):
        otp = otp+ str(random.choice(range(n)))
    return otp

#create your empty dictionary
data = {}

#strings purely for the UX
print("*"*31)
print("Welcome to Univelcity Bank.")
print("*"*31)
#start a while conditional loop to run continuously using the Boolean:True
while True:
    print("What would you like to do?\n1. Login\n2. Create Account\n3. Quit")
    user_input = input("::>")
    #use an if conditional loop to run codes for each of the user input options: 1,2 and 3
    #start with 1 or 2, either is ok
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
        #use the random number generator function to generate the 10 digit account number
        acct_no = random_otp(9)
        #I assigned all the inputed values to variables then set those variables as the 'values'
        #to the given dictionary structure as specified by Desmond
        #note: I used a new dictionary data2, reason being so that I can manipulate
        #the transaction pin and balance later on
        data2 = {"first_name": first_name,
                 "last_name": last_name,
                 "login_pin": login_pin,
                 "transaction_pin": transaction_pin,
                 "balance": balance}
        #then I assigned the new dictionary data2 as the 'value' to the 'key':acct_no
        #to satisfy the dictionary structure specification
        data[acct_no] = data2
        
        #here I used the time delay function, it's optional, you can remove it
        print("Creating account...")
        time.sleep(1)
        print("Completing setup...")
        time.sleep(1)
        print(f"\nWelcome {first_name}!\nYour account has been created and activated. \nYour Account number is {acct_no}\nCheers\nUnivelcity Bank.\n")
    #now use an elif conditional statement to code what happens when the user input is '1'
    elif user_input == "1":
        print("\nPlease enter your Account number.")
        #assign the user input to a variable so you can manipulate it later
        act_no = input("::>")
        print("\nPlease enter your 4-digit login pin.")
        #also assign the pin to a variable
        pin = (input("::>"))
        #here we use the .get() method to validate the account number
        a = data.get(act_no, False)

        #here I used pin==data2["login_pin"] to validate the inputed pin
        #we can also use the .get() method to validate it,
        #but I wasn't getting it right, so I'll read up on it later
        #so now we cobine the the two conditions for login (correct account number and correct login_pin) into a while loop
        while a and pin==data2["login_pin"]:
            print(f'Welcome {first_name}.')
            print("*************************************")
            print("Press 1 to Deposit ")
            print("Press 2 to Withdraw ")
            print("Press 3 to Transfer ")
            print("Press 4 to Check Balance ")
            print("Press 5 to Exit/Quit ")
            print("*************************************")
            #assign the input to a variable called choice
            choice = input('::>')
            if choice == "1":
                print('Enter deposit amount')
                amount = int(input('::>'))
                #this is why i used a separate dictionary, so I can manipulate the "balance"
                data2["balance"] = data2["balance"] + amount
                print(f'You have succesfully deposited {amount}')
                print(f'Your new balance is {data2["balance"]}')
            elif choice == "2":
                print('Enter withdrawal amount')
                amount = int(input('::>'))
                print('Enter your transaction pin')
                transaction_pin = input('::>')
                #here again we validated the transaction pin using ==. But we can also use .get() method. 
                #read up how to do it
                if transaction_pin==data2["transaction_pin"]:
                    if data2["balance"] > amount:
                        data2["balance"] = data2["balance"]-amount
                        print(f'Withdrawal Successful, your balance is {data2["balance"]}')
                    else:
                        print('insufficient funds')
                #if transaction pin is wrong print('Wrong transaction pin)
                #if condition is over
                else:
                    print('Wrong transaction pin')
            elif choice == "3":
                print('Enter recipient account number')
                #recipient account number can be anything, we don't use it in the code
                rec_acct_no = input('::>')
                print('Enter amount')
                amount = int(input('::>'))
                print('Enter your transaction pin')
                #validate the transaction pin again
                transaction_pin = input('::>')
                if transaction_pin==data2["transaction_pin"]:
                    if data2["balance"] < amount:
                        print('Insufficient funds')
                    else:
                        data2["balance"] = data2["balance"]-amount
                        print(f'Transfer Successful your balance is {data2["balance"]}')
                #if transaction pin is wrong....
                else:
                    print('Wrong transaction pin')
            elif choice == "4":
                print(f'Your balance is {data2["balance"]}')
            elif choice == "5":
                #here we use a break to quit the loop
                break
            else: print('Invalid input')
        #if the account number or login pin is incorrect
        else:
            print("\nInvalid Account number or login pin.")
    #we use break to quit the while loop
    elif user_input == "3":
        break