
def menu():
    print('MAIN MENU')
    print("[1] calculate body mass index (BMI)")
    print("[2] view membership cost")
    print("[3] exit the application")
    option = int(input("Enter your option: "))
    return option
        

def calculatebmi():
    while True:
        try:
            user_height = float(input('Please enter your height  (M): '))
            user_weight = float(input('Please enter your weight (KG): '))
            bmi = (user_weight / (user_height * user_height))
            bmi = round(bmi ,2)
            print("Your BMI is" , bmi)
        except ValueError:
            print("Sorry, I didn't understand that, please re-enter values")
            continue
        else:
            break
    if bmi < 18.5:
            print('You are underweight')
            input("Press enter to return to go to the menu") 
    elif bmi >= 18.5 and bmi < 25:
            print('You are normal')
            input("Press enter to return to go to the menu") 
    elif bmi >= 25 and bmi < 30:
            print('You are overweight')
            input("Press enter to return to go to the menu") 
    elif bmi >= 30:
            print('You are obese')
            input("Press enter to return to go to the menu") 
           
           

def viewMembershipCosts():
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
                    input("Press enter to see other packages")    
                case 2:
                    print("You have chosen the regular package prices are below")
                    regular_monthly = round(regular_monthly ,2)
                    print("Weekly Cost: $", regular)
                    print("Monthly Cost: $", regular_monthly) 
                    input("Press enter to see other packages")   
                case 3:
                    print("You have chosen premium package prices are below")
                    premium_monthly = round(premium_monthly ,2)
                    print("Weekly Cost: $", premium)
                    print("Monthly Cost: $", premium_monthly) 
                    input("Press enter to see other packages") 
                case 4:
                    return
                case _:
                    print("Wrong input, Please try again!")
                
selectingOption = True
while selectingOption:
    selection = menu()
    match selection:
            case 1:
                calculatebmi()
                
                
            case 2:
                viewMembershipCosts()
                
                
            case 3:
                selectingOption = False
                input("Goodbye! Please press Enter to exit!")
                exit()
