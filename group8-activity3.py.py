"""
Students: Meera Alshara, Syed Hossain, Caesar Al Shdaifat
contribution of Syed: analyze data and main functions
contribution of Caesar: 
contribution of Meera: load_data function & docstring
Description: 

Repository Links:
Syed : https://github.com/LagSpikeee/GCIS-123/blob/main/group8-activity3.py.py
Meera : https://github.com/meeralshara/gcis123/new/main
Caesar : 
"""
import csv

def load_data():
    """this function will prompt the user to put the correct csv file path and then 
    puts the data into lists and then returns the header and data"""
    while True:
        file_path = input("Stage 1: Load Data\nPlease enter the path to the CSV file: ")
        if not file_path.endswith('.csv'): #if the file path entered by the user is incorrect the user enters it again
            print("Invalid file format. Please enter a path to a CSV file.")
        else:
            try:
                with open(file_path, 'r') as file:
                    file_name_reader = csv.reader(file)
                    header = next(file_name_reader)
                    data = [line for line in file_name_reader]

                print("\nFile exists.")
                print("Loading file...")
                print("File successfully loaded!\n")
                print("Loaded Data: ")
                for line in data:
                    print(line)
                return header, data
            except FileNotFoundError:
                print("File not found. Please enter a valid file path.")
            except ValueError:
                print("Non-numerical column, please try again.")

def clean_and_prepare_data(column):
"""this function prompts the user to chose between 3 types of calculation ways to replace the rows
in the file with the final result of the chosen calculation type
"""

    while True:
        print("Replace empty cells with:")
        print("1. Minimum value")
        print("2. Maximum value")
        print("3. Average value")
        choice = input("Enter your choice (1/2/3): ")

        if choice in ['1', '2', '3']:
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    values = [float(val) for val in column if val.strip()]
    if not values:
        print("No valid data in the column to calculate.")
        return column

    if choice == '1':
        replacement_value = min(values)
    elif choice == '2':
        replacement_value = max(values)
    elif choice == '3':
        replacement_value = sum(values) / len(values)
    else:
        print("Please choose between 1-3")

    column = [replacement_value if val.strip() == '' else float(val) for val in column]
    print("Data cleaned and prepared successfully.")
    print("Updated Column:")
    for value in column:
        print(value)
    return column

def analyze_data(data):
""""this function makes the user chose a sorting order and colomn and then returns it"
"""
    while True:
        try:
            print("Choose sorting option:")
            print("1. Sort data in ascending order")
            print("2. Sort data in descending order")
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                sorted_data = sorted(data)
                print("Data sorted in ascending order.")
            elif choice == 2:
                sorted_data = sorted(data, Ascending=False)
                print("Data sorted in descending order.")
            else:
                print("Invalid choice! Please enter either 1 or 2.")
                continue
            
            return sorted_data
        except ValueError:
            print("Invalid input! Please enter a valid numeric value.")


def visualize_data(data):
     """this function prints all the sorted data visually """

    print()
    print("Stage 4: Visualize Data")
    print("Legend: each '*' represents 5 units")
    print()
    col_name = input("Enter the column name you want to represent: ")
    units_column = [int(float(row[1])) // 5 for row in data if row[0] == col_name.strip()]
    for units in units_column:
        print('*' * units)
    print("Updated Data:")
    for row in data:
        print(row)

def main():
    print("---------------------------------")
    print("Welcome to Data Analysis CLI")
    print("---------------------------------")
    print("Program stages:\n ")
    print("1. Load Data\n2. Clean and prepare data\n3. Analyze Data\n4. Visualize Data\n")
  
    header, data = load_data()
    cleaned_column = clean_and_prepare_data(column_to_clean)
    sorted_data = analyze_data(data)
    visualize_data(sorted_data)
    print("\nVisualisation completed!\nThank you and goodbye!")

if __name__ == "__main__":
    main()
