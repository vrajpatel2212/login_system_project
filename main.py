name = input("Enter your name:")
print("Hello", name,"\n----WELCOME TO YOUR ACCOUNT----")
print()
user_input = input("Do you want to login to your account?(yes/no): ")
print()
if user_input == "yes":
    user_input = input("how do you want to login? \n Password or Phone number?: ")
    print()
    if user_input == "Password":
        Userid = input("Enter your userid: ")
        user_input = input("Enter your password:")
        print()
        if user_input == "Vraj@123":
            print("Password is correct, \nPlease welcome to your account.")
        else:
            print("Password incorrect")
            user_input = input("Enter ypur password: ")
            print()
            if user_input == "Vraj@123":
                print("Password is correct, \nPlease welcome to your account.")
            else:
                print("Password incorrect")
                user_input = input("Enter ypur password: ")
                print()
                if user_input == "Vraj@123":
                    print("Password is correct, \nPlease welcome to your account.")
                else:
                    print("Password incorrect")
                    user_input = input("Enter ypur password: ")
                    print()
                    if user_input == "Vraj@123":
                        print("Password is correct, \nPlease welcome to your account.")
                    else:
                        print("Sorry you reached your maximum limit, \nPlease try again later")
    else:
        user_input = input("Enter your phone number:")
        if user_input == "7203902212":
            print("Correct phone number, \nPlease welcome to your account.")
        else:
            print("Wrong number")
            user_input = input("Enter your phone number:")
            print()
            if user_input == "7203902212":
                print("Correct phone number, \nPlease welcome to your account.")
            else:
                print("Wrong number")
                user_input = input("Enter your phone number:")
                print()
                if user_input == "7203902212":
                    print("Correct phone number, \nPlease welcome to your account.")
                else:
                    print("Wrong number")
                    user_input = input("Enter your phone number:")
                    print()
                    if user_input == "7203902212":
                        print("Correct phone number, \nPlease welcome to your account.")
                    else:
                        print("Wrong number")
                        print("Sorry you reached your maximum limit, \nPlease try again later")
else:
    print("Ok, \nSee you soon")
