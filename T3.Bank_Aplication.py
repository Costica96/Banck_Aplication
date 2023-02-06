""" This is a Bank Aplication"""


user_name = input("Please introduce your name: ")
user_iban = input("Please introduce your IBAN number: ")
user_account_balance = 0

is_user_continue = True

IBAN_LENGHT = 24

if len(user_iban) == IBAN_LENGHT:
    while is_user_continue:
        account_operation = input("Please introduce desired operation. Write 'withdraw', 'add', 'display', or 'exit': ")
        if account_operation == "withdraw":
            action_amount = int(input("Please introduce de amount:"))
            if user_account_balance < action_amount :
                print("Insuficient balance!")
            else:
                user_account_balance -= action_amount
        elif account_operation == "add":
            action_amount = int(input("Please introduce de amount:"))
            user_account_balance += action_amount
        elif account_operation == "display":
            print(f"Numele tau este: "+ (user_name))
            print(f"IBAN-ul contului tau este: "+ (user_iban))
            print(f"Valoarea contului tau este: "+ str(user_account_balance))
        elif account_operation == "exit":
            is_user_continue = False
        else:
            print("Incorrect action!")
else:
    print("The introcuced IBAN is incorrect!")