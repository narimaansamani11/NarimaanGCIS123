"""
Group number: 4

Student 1: Narimaan Samani (UID: 754005820)
Student 2: Ala'a Al Zein (UID: 759009741) 
Student 3: Youssef Abdelfattah (UID: 405008858)
Student 4: Ayman Abdulwahid (UID: 405008855)

Github link: https://github.com/narimaansamani11/NarimaanGCIS123/blob/main/Group4-Activity2.py

"""
import csv  # Importing the CSV module

def load_data():  # Defining a function to load data from a CSV file
    """
    Load data from a CSV file.
    
    Returns:
        list: The data loaded from the CSV file.
    """
    while True:  # Start an infinite loop to handle file loading
        try:  # Try to execute the following code
            filepath = input("Enter path to the CSV file: ")  # Asking user to input file path
            with open(filepath, 'r') as file:  # Opening the file in read mode
                print("File exists.")
                print("Loading file…")
                print("File successfully loaded!")

                csv_reader = csv.reader(file)  # Creating a CSV reader object
                csv_data = list(csv_reader)  # Converting CSV data into a list

                print("Preview of the CSV file:")  
                for row in csv_data[:9]:  # Looping through the first 9 rows of CSV data
                    print(row)  

                print("Columns in the CSV file:")  
                for i in range(len(csv_data[0])):  # Looping through the columns
                    print(i+1, csv_data[0][i])

                column_choice = input("Please choose a column (1, 2, 3, 4): ")  # Asking user to choose a column

                if column_choice.strip():  # Checking if user input is not empty
                    try:
                        column_choice = int(column_choice)  # Converting user input to integer
                        if column_choice < 1 or column_choice > len(csv_data[0]):  # Checking if column choice is valid
                            raise ValueError("Invalid column choice. Please choose again.")  # Raising an error for invalid choice
                    except ValueError: # Handling value error
                        print(ValueError) 
                        continue  
                else: 
                    print("Invalid column choice. Please choose again.")  
                    continue  

                selected_row = csv_data[1]  # Selecting the second row of data
                selected_column_index = column_choice - 1  # Calculating the index of the selected column
                selected_value = selected_row[selected_column_index]  # Getting the value of the selected column
                first_value = selected_value.strip()  # Stripping any whitespace from the selected value

                try:  
                    int(first_value)  # Converting the first value to an integer
                except ValueError:  # Handling value error
                    print("Selected column is not numerical. Please choose a numerical column.") 
                    continue  

                column_data = [row[column_choice - 1] for row in csv_data[1:]]  # Extracting data from the selected column
                print("Data loaded successfully.")  
                print("Selected column data:", column_data)  
                return column_data  

        except FileNotFoundError:  # Handling file not found error
            print("File not found. Please enter a valid file path.")  
        except Exception as e:  # Handling other exceptions
            print("An unexpected error occurred:", e)  

def clean_and_prepare_data(column_data):  # Defining a function to clean and prepare data
    print("Would you like to replace empty cells from the column with:")  
    print("1. Maximum value from the column") 
    print("2. Minimum value from the column") 
    print("3. Average value from the column") 

    numeric_column_data = []  # Initializing an empty list to store numeric data
    for value in column_data:  # Looping through the values in the column
        value_stripped = value.strip()  
        if value_stripped:  
            numeric_column_data.append(float(value_stripped))  

    if not numeric_column_data:  # Checking if there is no numeric data
        print("Error: The selected column does not contain any numeric data.")  
        return None  

    while True:  # Starting an infinite loop
        choice = input("Enter your choice (1, 2, or 3): ")  # Prompting user to choose an option

        if choice in ["1", "2", "3"]:  
            if choice == "1":  
                replacement_value = max(numeric_column_data)  
            elif choice == "2":
                replacement_value = min(numeric_column_data)  
            else:  
                replacement_value = sum(numeric_column_data) / len(numeric_column_data)  

            cleaned_column_data = [float(value.strip()) if value.strip() else replacement_value for value in column_data] 

            if choice == "1":  
                print("All empty values replaced with maximum value!")  
            elif choice == "2":
                print("All empty values replaced with minimum value!") 
            else:  
                print("All empty values replaced with average value!")  

            return cleaned_column_data  
        else:  
            print("Invalid choice, please try again.")  

def analyze_data(data):  # Defining a function to analyze data
    sorted_data = sorted(data)  # Sorting the data in ascending order

    print("Please choose how you want to sort the data:")  
    print("1. From small to large")  
    print("2. From large to small")  

    while True:  # Starting an infinite loop
        try:  # Try to execute the following code
            choice = int(input("Enter your choice: "))  # Prompting user to choose an option as integer

            if choice == 1:  
                print("Data is sorted from small to large!") 
                return sorted_data  
            elif choice == 2: 
                sorted_data.reverse()  
                print("Data is sorted from large to small!")  
                return sorted_data  
            else:
                print("Error: Invalid choice. Please choose again.")  
        except ValueError:  # Handling value error
            print("Error: Please enter a valid choice (1 or 2).")  

def visualize_data(data):  # Defining a function to visualize data
    print("Visualizing data...")  
    for value in data:  # Looping through the values in the data
        stars = min(int(value) // 5, 20)  # Calculating the number of stars to represent the value
        print("*" * stars)  # Printing stars based on the value

def main():  # Defining the main function
    """
    Main function to orchestrate the data analysis process.
    """
    print("--------------------------------")  
    print("Welcome to Data Analysis CLI")  
    print("--------------------------------")  
    print("Program stages:")  
    print("1. Load Data")  
    print("2. Clean and prepare data") 
    print("3. Analyze Data")  
    print("4. Visualize Data")  

    print("Stage 1: Load Data")  
    column_data = load_data()  

    print("Stage 2: Clean and prepare data") 
    cleaned_column_data = clean_and_prepare_data(column_data)  

    print("Stage 3: Analyze data")  
    analyzed_data = analyze_data(cleaned_column_data)  

    print("Stage 4: Visualize Data") 
    visualize_data(analyzed_data) 

if __name__ == "__main__":  
    main()  # Calling the main function
