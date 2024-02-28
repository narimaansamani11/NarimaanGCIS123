"""
Group number: 4

Student 1: Narimaan Samani (UID: 754005820)
Student 2: Ala'a Al Zein (UID: 759009741) 
Student 3: Youssef Abdelfattah (UID: 405008858)
Student 4: Ayman Abdulwahid (UID: 405008855)

Github link: 

"""

"""Currency conversion rates"""
AED_to_EUR = 0.24
AED_to_GBP = 0.20
AED_to_USD = 0.27
EUR_to_AED = 4.17
GBP_to_AED = 5.0
USD_to_AED = 3.70

"""Convert AED to EUR."""
def convert_AED_to_EUR(money):
    return float(money * AED_to_EUR)

"""Convert AED to GBP."""
def convert_AED_to_GBP(money):
    return float(money * AED_to_GBP)

"""Convert AED to USD."""
def convert_AED_to_USD(money):
    return float(money * AED_to_USD)

"""Convert EUR to AED."""
def convert_EUR_to_AED(money):
    return float(money * EUR_to_AED)

"""Convert GBP to AED."""
def convert_GBP_to_AED(money):
    return float(money * GBP_to_AED)

"""Convert USD to AED."""
def convert_USD_to_AED(money):
    return float(money * USD_to_AED)    

"""Main function to execute the currency converter."""
def main():
    print("         Main Menu")
    print(" Welcome to Currency Converter")
    print("-------------------------------")

    print("")
    
    # Conversion options display
    print("Select the conversion direction:")
    print("1. AED to other currencies")
    print("2. Other currencies to AED")
    print("3. Exit")

    # Get user choice
    choice = input("Enter your choice (1/2/3): ")
    
    # Conversion from AED to other currencies
    if choice == '1': 

        # Get amount to convert
        money = int(input("Enter your amount you want to convert: "))

        print("\nConvert AED to:")
        print("1. Euro (EUR)")
        print("2. British Pound (GBP)")
        print("3. US Dollar (USD)")
        print("4. Go back to Main Menu")

        # Get sub-choice
        sub_choice = input("Enter your choice (1/2/3/4): ")

        # Convert AED to EUR
        if sub_choice == '1':
            print(money, "AED is equal to ", convert_AED_to_EUR(money), "EUR")

        # Convert AED to GBP
        elif sub_choice == '2':
            print(money, "AED is equal to ", convert_AED_to_GBP(money), "GBP")
        
        # Convert AED to USD
        elif sub_choice == '3':        
            print(money, "AED is equal to ", convert_AED_to_USD(money), "USD")

        elif sub_choice == '4':
            print("")
            main() # Go back to Main Menu

        else:
            print("Invalid! Please enter a number from 1-4!") # Display error message
            main() # Go back to Main Menu

    # Conversion from other currencies to AED
    elif choice == '2':

        # Get amount to convert
        money = int(input("Enter your amount you want to convert: "))

        # Conversion options display 
        print("\nConvert from:")
        print("1. Euro (EUR)")
        print("2. British Pound (GBP)")
        print("3. US Dollar (USD)")
        print("4. Go back to Main Menu")
        
        # Get sub-choice
        sub_choice = input("Enter your choice (1/2/3/4): ")

        # Convert EUR to AED
        if sub_choice == '1':        
            print(money, "EUR is equal to ", convert_EUR_to_AED(money), "AED")

        # Convert GBP to AED
        elif sub_choice == '2':    
            print(money, "GBP is equal to ", convert_GBP_to_AED(money), "AED")
        
        # Convert USD to AED
        elif sub_choice == '3':
            print(money, "USD is equal to ", convert_USD_to_AED(money), "AED")


        elif sub_choice == '4':
            print("")
            main() # Go back to Main Menu

        else:
            print("Invalid! Please enter a number from 1-4!") # Display error message
            main() 

    # Exiting the program
    elif choice == '3':
        print("Thank you for using Currency Converter!")

    # Ask user if they want to continue
    another_conversion = input("Do you want to continue? (yes/no): ")
    if another_conversion == 'yes': # If user wants to continue
        print("")
        main() # Go back to Main Menu

    else:
        print("Thank you for using Currency Converter!")

# Calling the main function
if __name__ == "__main__":
    main()