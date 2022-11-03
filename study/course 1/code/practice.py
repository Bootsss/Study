selectingMembership = True
basic = 10
regular = 15
premium = 20
basic_monthly = basic*52/12
regular_monthly = regular*52/12
premium_monthly = premium*52/12

while True:
        print("Below are all our memberships, which one would you like?:")
        print("[1] Basic Package")
        print("[2] Regular Package")
        print("[3] Premium Package")
        print("[4] Return to Main Menu")
        try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
            membership = int(input("Enter your option: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
            continue
        match membership:
                case 1:
                    print("you have chosen basic package the prices are below")
                    basic_monthly = round(basic_monthly ,2)
                    print("Weekly Cost: $", basic)
                    print("Monthly Cost: $", basic_monthly) 
                    input("Press enter to go next")    
                case 2:
                    print("You have chosen the regular package prices are below")
                    regular_monthly = round(regular_monthly ,2)
                    print("Weekly Cost: $", regular)
                    print("Monthly Cost: $", regular_monthly) 
                    input("Press enter to go next")   
                case 3:
                    print("You have chosen premium package prices are below")
                    premium_monthly = round(premium_monthly ,2)
                    print("Weekly Cost: $", premium)
                    print("Monthly Cost: $", premium_monthly) 
                    input("Press enter to go next") 
                case _:
                    print("Wrong input, Please try again!")   
            
