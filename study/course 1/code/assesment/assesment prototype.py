#Assesment 1


print('MAIN MENU')

def menu():
    print("[1] calculate body mass index (BMI)")
    print("[2] view membership cost")
    print("[3] exit the application")

menu()
option = int(input("Enter your option: "))

while option != 0:
    if option ==1:
        #take to option 1 page
        print('Today we are going to calculate your BMI')
        user_weight = int(input('Please enter your weight: '))
        user_height = float(input('Please enter your height: '))
        bmi = (user_weight / (user_height * user_height))
        bmi = round(bmi ,2)
        print("Your BMI is" , bmi)
        if bmi < 18.5:
            print('You are underweight')
            break
        elif bmi >= 18.5 and bmi < 25:
            print('You are normal')
            break
        elif bmi >= 25 and bmi < 30:
            print('You are overweight')
            break
        elif bmi >= 30:
            print('You are obese')
        else:
            print("Wrong input, Please try again")
    
        
        
    elif option == 2:
        #take to option page
        print("Below are all our memberships, which one would you like?:")
        print("[1] Basic Package")
        print("[2] Regular Package")
        print("[3] Premium Package")
        membership = int(input("Enter your option: "))
        while membership != 0:
            if membership == 1:
                basic = 10
                regular = 15
                premium = 20
                basic = round(basic ,2)
                regular = round(regular ,2)
                premium = round(premium ,2)
                print("you have chosen basic package the prices are below")
                print("Weekly Cost: ", basic)
                print("Monthly Cost: ", basic*52/12)
                break
            elif membership ==2:
                print("You have chosen the regular package prices are below")
                print("Weekly Cost: ", regular)
                print("Monhtly Cost: ", regular*52/12)
                break
            elif membership == 3:
                print("You have chosen premium package prices are below")
                print("Weekly Cost: ", premium)
                print("Monthly Cost: ", premium*52/12)
                break
            else:
                print("Wrong input, Please try again!")
                




    elif option == 3:
        exit = str(input("Press any button to exit:  "))
        print("Goodbye!")
        quit()
            
       

    else:
        print("Invalid option, please try again!")

menu()
option = int(input("Enter your option"))



    

