# Part 1: Job application inventory
# Name: Thian Zhi Xin Jabez
# Admin No: 190900M
# Tutorial Group: IT2653_04

# Records stored:
#     1. Record index
#     2. Package name
#     3. Customer name
#     4. Check-in date
#     5. Customer gender
#     6. Customer birth date

# Menu selections:
#      Add record
#      Update selected record
#      Remove record
#      Display all records
#      Sort record (sort by index)
#         + Bubble sort
#         + Selection sort
#         + Insertion sort
#      Search record
#         + Linear search
#             - Index
#             - Customer Name
#         + Binary search (sort by index)
#      Exit Application

from datetime import datetime
import math
# Sample record 1
records = {1: {'Package Name': 'A', 'Customer Name': 'Matthew', 'Check-in Date': '16/02/2020', 'Customer Gender': 'M', 'Customer Birthdate': '20/02/1996'},
2: {'Package Name': 'C', 'Customer Name': 'Mark', 'Check-in Date': '25/06/2020', 'Customer Gender': 'M', 'Customer Birthdate': '14/03/2000'},
3: {'Package Name': 'B', 'Customer Name': 'Eve', 'Check-in Date': '10/12/2019', 'Customer Gender': 'F', 'Customer Birthdate': '16/12/1975'},
4: {'Package Name': 'B', 'Customer Name': 'Eliz', 'Check-in Date': '16/01/2021', 'Customer Gender': 'F', 'Customer Birthdate': '18/02/1988'},
5: {'Package Name': 'E', 'Customer Name': 'Luke', 'Check-in Date': '17/01/2021', 'Customer Gender': 'M', 'Customer Birthdate': '01/08/1968'},
6: {'Package Name': 'D', 'Customer Name': 'Mary', 'Check-in Date': '18/01/2021', 'Customer Gender': 'F', 'Customer Birthdate': '05/04/1987'}}

# Sample record 2
# records = {1: {'Package Name': 'A', 'Customer Name': 'Isabella', 'Check-in Date': '18/12/1999', 'Customer Gender': 'F', 'Customer Birthdate': '20/02/1982'},
# 2: {'Package Name': 'C', 'Customer Name': 'Siri', 'Check-in Date': '25/07/2016', 'Customer Gender': 'F', 'Customer Birthdate': '14/03/2003'},
# 3: {'Package Name': 'D', 'Customer Name': 'Ava', 'Check-in Date': '10/12/2018', 'Customer Gender': 'F', 'Customer Birthdate': '16/12/1987'},
# 4: {'Package Name': 'B', 'Customer Name': 'Ellien', 'Check-in Date': '18/04/2020', 'Customer Gender': 'F', 'Customer Birthdate': '18/02/1984'},
# 5: {'Package Name': 'E', 'Customer Name': 'Tom', 'Check-in Date': '20/09/2020', 'Customer Gender': 'M', 'Customer Birthdate': '01/08/1967'},
# 6: {'Package Name': 'F', 'Customer Name': 'Jerry', 'Check-in Date': '25/01/2020', 'Customer Gender': 'M', 'Customer Birthdate': '05/04/1986'},
# 7: {'Package Name': 'G', 'Customer Name': 'John', 'Check-in Date': '01/08/2014', 'Customer Gender': 'M', 'Customer Birthdate': '20/02/1998'},
# 8: {'Package Name': 'C', 'Customer Name': 'Jospeh', 'Check-in Date': '05/10/2017', 'Customer Gender': 'M', 'Customer Birthdate': '14/03/2000'},
# 9: {'Package Name': 'B', 'Customer Name': 'Megan', 'Check-in Date': '12/07/2016', 'Customer Gender': 'F', 'Customer Birthdate': '16/12/2002'},
# 10: {'Package Name': 'B', 'Customer Name': 'Reyna', 'Check-in Date': '15/05/2012', 'Customer Gender': 'F', 'Customer Birthdate': '18/02/2000'},
# 11: {'Package Name': 'E', 'Customer Name': 'Jett', 'Check-in Date': '28/11/2008', 'Customer Gender': 'F', 'Customer Birthdate': '01/08/1965'},
# 12: {'Package Name': 'F', 'Customer Name': 'Martin', 'Check-in Date': '24/12/2021', 'Customer Gender': 'M', 'Customer Birthdate': '05/04/1988'}
# }

# Sample record 3
# records = {1: {'Package Name': 'A', 'Customer Name': 'Isabella', 'Check-in Date': '18/12/1999', 'Customer Gender': 'F', 'Customer Birthdate': '20/02/1982'},
# 2: {'Package Name': 'D', 'Customer Name': 'Siri', 'Check-in Date': '25/07/2016', 'Customer Gender': 'F', 'Customer Birthdate': '14/03/2003'},
# 3: {'Package Name': 'F', 'Customer Name': 'Ava', 'Check-in Date': '10/12/2018', 'Customer Gender': 'F', 'Customer Birthdate': '16/12/1987'},
# 4: {'Package Name': 'B', 'Customer Name': 'Ellien', 'Check-in Date': '18/04/2020', 'Customer Gender': 'F', 'Customer Birthdate': '18/02/1984'},
# 5: {'Package Name': 'E', 'Customer Name': 'Tom', 'Check-in Date': '20/09/2020', 'Customer Gender': 'M', 'Customer Birthdate': '01/08/1967'},
# 6: {'Package Name': 'D', 'Customer Name': 'Jerry', 'Check-in Date': '25/01/2020', 'Customer Gender': 'M', 'Customer Birthdate': '05/04/1986'},
# 7: {'Package Name': 'A', 'Customer Name': 'John', 'Check-in Date': '01/08/2014', 'Customer Gender': 'M', 'Customer Birthdate': '20/02/1998'},
# 8: {'Package Name': 'CA', 'Customer Name': 'Jospeh', 'Check-in Date': '05/10/2017', 'Customer Gender': 'M', 'Customer Birthdate': '14/03/2000'},
# 9: {'Package Name': 'B', 'Customer Name': 'Megan', 'Check-in Date': '12/07/2016', 'Customer Gender': 'F', 'Customer Birthdate': '16/12/2002'},
# 10: {'Package Name': 'B', 'Customer Name': 'Reyna', 'Check-in Date': '15/05/2012', 'Customer Gender': 'F', 'Customer Birthdate': '18/02/2000'},
# 11: {'Package Name': 'E', 'Customer Name': 'Jett', 'Check-in Date': '28/11/2008', 'Customer Gender': 'F', 'Customer Birthdate': '01/08/1965'},
# 12: {'Package Name': 'D', 'Customer Name': 'Martin', 'Check-in Date': '24/12/2021', 'Customer Gender': 'M', 'Customer Birthdate': '05/04/1988'},
# 13: {'Package Name': 'A', 'Customer Name': 'Matthew', 'Check-in Date': '16/02/2020', 'Customer Gender': 'M', 'Customer Birthdate': '20/02/1996'},
# 14: {'Package Name': 'H', 'Customer Name': 'Mark', 'Check-in Date': '25/06/2020', 'Customer Gender': 'M', 'Customer Birthdate': '14/03/2000'},
# 15: {'Package Name': 'B', 'Customer Name': 'Eve', 'Check-in Date': '10/12/2019', 'Customer Gender': 'F', 'Customer Birthdate': '16/12/1975'},
# 16: {'Package Name': 'A', 'Customer Name': 'Eliz', 'Check-in Date': '16/01/2021', 'Customer Gender': 'F', 'Customer Birthdate': '18/02/1988'},
# 17: {'Package Name': 'E', 'Customer Name': 'Luke', 'Check-in Date': '17/01/2021', 'Customer Gender': 'M', 'Customer Birthdate': '01/08/1968'},
# 18: {'Package Name': 'D', 'Customer Name': 'Mary', 'Check-in Date': '18/01/2021', 'Customer Gender': 'F', 'Customer Birthdate': '05/04/1987'}}
count = len(records) + 1
choice = "0"


# Function of adding records
def add_record(counts):
    valid_check_in = False
    valid_birthday = False

    # Package Input and validation
    package = input("Enter package name: ")
    while package.isalnum() is False:
        print("Your Package should only include letters and numbers with no spacing")
        package = input("Enter Package name: ")

    # Name input and validation
    name = input("Enter your name: ")
    while name.isalpha() is False:
        print("Your Name should only contain letters with no spacing")
        name = input("Enter your name: ")

    # Check_in date input and validation
    while valid_check_in is False:
        try:
            check_in = input("Enter check-in date (dd/mm/yyyy): ")
            datetime.strptime(check_in, '%d/%m/%Y')
            valid_check_in = True
        except ValueError:
            print("Incorrect date format!")
            print("Date format should be dd/mm/yyyy; Example: 12/01/2018")

    # Gender input and validation
    gender = input("Enter your gender (enter either M or F): ").capitalize().strip()
    while gender != "M" and gender != "F":
        print("Enter only M or F")
        gender = input("Enter your gender: (enter either M or F): ").capitalize().strip()

    # Birthday date input and validation
    while valid_birthday is False:
        try:
            birthday = input("Enter your birth date (dd/mm/yyyy): ")
            datetime.strptime(birthday, '%d/%m/%Y')
            valid_birthday = True
        except ValueError:
            print("Incorrect date format")
            print("Date format should be dd/mm/yyyy; Example: 07/09/1999")

    # Adds the 6 information into record
    records[counts] = {"Package Name": package, "Customer Name": name, "Check-in Date": check_in, "Customer Gender": gender, "Customer Birthdate": birthday}
    counts += 1

    return counts


# Function of update records
def update_record(indexNo):
    valid_check_in = False
    valid_birthday = False

    # Package Input and validation
    package = input("Enter package name (Press enter if there is no change): ")
    if package == "":
        # When user enters nothing it passes; takes as record need not be updated
        pass
    else:
        while package.isalnum() is False and package != "":
            print("Your Package should only include letters and numbers with no spacing")
            package = input("Enter package name (Press enter if there is no change): ")
        if package == "":
            # When user enters nothing it passes; takes as record need not be updated
            pass
        else:
            # Stores updated information in Package Name
            records[indexNo]["Package Name"] = package

    # Name input and validation
    name = input("Enter your name (Press enter if there is no change): ")
    if name == "":
        # When user enters nothing it passes; takes as record need not be updated
        pass
    else:
        while name.isalpha() is False and name != "":
            print("Your Name should only contain letters with no spacing")
            name = input("Enter your name (Press enter if there is no change): ")
        if name == "":
            # When user enters nothing it passes; takes as record need not be updated
            pass
        else:
            # Stores updated information into Customer Name
            records[indexNo]["Customer Name"] = name

    # Check_in date input and validation
    while valid_check_in is False:
        # Exception to validate the date format
        try:
            check_in = input("Enter check-in date (dd/mm/yyyy, press enter if there is no change): ")
            if check_in == "":
                # When user enters nothing it passes; takes as record need not be updated
                pass
            else:
                # Stores updated information into Check-in Date
                datetime.strptime(check_in, '%d/%m/%Y')
                records[indexNo]["Check-in Date"] = check_in    # Stores updated information
            valid_check_in = True
        except ValueError:
            if check_in == "":
                # When user enters nothing it passes; takes as record need not be updated
                pass
            else:
                print("Incorrect date format")
                print("Date format should be dd/mm/yyyy; Example: 12/01/2018")

    # Gender input and validation
    # Remove any spacing and capitalise it to standardize
    gender = input("Enter your gender (Type either M or F or press enter if there is no change): ").capitalize().strip()
    if gender == "":
        # When user enters nothing it passes; takes as record need not be updated
        pass
    else:
        while gender != "M" and gender != "F" and gender != "":
            print("Enter only M or F")
            gender = input("Enter your gender (Type either M or F or press enter if there is no change): ").capitalize().strip()
        if gender == "":
            # When user enters nothing it passes; takes as record need not be updated
            pass
        else:
            # Stores updated information Customer Gender
            records[indexNo]["Customer Gender"] = gender

    # Birthday date input and validation
    while valid_birthday is False:
        # Exception to validate the date format
        try:
            birthday = input("Enter your birth date (dd/mm/yyyy, press enter if there is no change): ")
            if birthday == "":
                # When user enters nothing it passes; takes as record need not be updated
                pass
            else:
                # Stores updated information Customer Birthdate
                datetime.strptime(birthday, '%d/%m/%Y')
                records[indexNo]["Customer Birthdate"] = birthday
            valid_birthday = True
        except ValueError:
            if birthday == "":
                # When user enters nothing it passes; takes as record need not be updated
                pass
            else:
                print("Incorrect date format")
                print("Date format should be dd/mm/yyyy; Example: 07/09/1999")

    print("Records has been successfully updated!")


#  Function to remove records
def remove_record(indexNo):
    # Removes the dictionary in the dictionary by the index number
    records.pop(indexNo)
    print("Index {} have been removed!".format(indexNo))


# Function of Bubble sort
def bubble(dict_record, orders):
    # making dict_record into a list with tuples
    list_record = list(dict_record.items())
    # where n is the length in list_record
    n = len(list_record)
    # print(list_record)       # Checking what is in list_record
    # Where n is the length of list_records
    indexing_length = n - 1
    sorting = False

    while sorting is False:
        sorting = True
        # Checking if order is A for ascending
        if orders == "A":
            for i in range(0, indexing_length):
                # Check if the first index is larger than the second index (ascending)
                if list_record[i][0] > list_record[i + 1][0]:
                    # Sorting change back to False
                    sorting = False
                    # Swapping the position using bubble sort
                    list_record[i], list_record[i + 1] = list_record[i + 1], list_record[i]

        # Checking if order is D for descending
        elif orders == "D":
            for i in range(0, indexing_length):
                # Check if the first index is smaller than the second index (descending)
                if list_record[i][0] < list_record[i + 1][0]:
                    sorting = False
                    # Swapping the position using bubble sort
                    list_record[i], list_record[i + 1] = list_record[i + 1], list_record[i]

        else:
            print("Invalid option!")

    # print(list_record)   # Sorted arrangement of tuples in a list

    # Putting the tuples in a list back into a dictionary
    dict_record = {list_record[j][0]: list_record[j][1] for j in range(n)}

    return dict_record


# Function of Selection sort
def selection(dict_record, orders):
    # making dict_record into a list with tuples
    list_record = list(dict_record.items())
    # range of the length in list_record
    indexing_length = range(len(list_record))

    # Checking if order is A for ascending
    if orders == "A":
        # Moving the minimum value up through the list
        for i in indexing_length:
            # Index of the minimum value
            min_value = i

            # Moving through the list of numbers
            for j in range(i+1, len(list_record)):
                # Check if the value has a smaller value compared to min_value by the index
                if list_record[j][0] < list_record[min_value][0]:
                    # If value is smaller than min_value than swap
                    min_value = j

            # Check if the min_value is really minimum and if it is not
            if min_value != i:
                # swap the minimum value with the current value and current value as the minimum value
                list_record[min_value], list_record[i] = list_record[i], list_record[min_value]
        print("All records are all sorted!")

    # Checking if order is D for descending
    elif orders == "D":
        # Moving the maximum value up through the list
        for i in indexing_length:
            # Index of the maximum value
            max_value = i

            # Moving through the list of numbers
            for j in range(i+1, len(list_record)):
                # Check if the value has a larger value compared to max_value by the index
                if list_record[j][0] > list_record[max_value][0]:
                    # If value is larger than max_value than swap
                    max_value = j

            # Check if the max_value is really maximum and if it is not
            if max_value != i:
                # swap the maximum value with the current value and current value as the maximum value
                list_record[max_value], list_record[i] = list_record[i], list_record[max_value]
        print("All records are all sorted!")

    else:
        print("Invalid option!")

    # Putting the tuples in a list back into a dictionary
    dict_record = {list_record[j][0]: list_record[j][1] for j in range(len(list_record))}

    return dict_record


# Function of Insertion sort
def insertion(dict_record, orders):
    # making dict_record into a list with tuples
    list_record = list(dict_record.items())
    # range of the length in list_record where it starts at 1
    indexing_length = range(1, len(list_record))
    # Checking if order is A for ascending
    if orders == "A":
        for i in indexing_length:
            value_to_sort = list_record[i][0]
            while list_record[i-1][0] > value_to_sort and i > 0:
                # Swap the
                list_record[i], list_record[i-1] = list_record[i-1], list_record[i]
                i -= 1
        print("All records are all sorted!")

    # Checking if order is D for descending
    elif orders == "D":
        for i in indexing_length:
            value_to_sort = list_record[i][0]
            while list_record[i-1][0] < value_to_sort and i > 0:
                list_record[i], list_record[i-1] = list_record[i-1], list_record[i]
                i -= 1
        print("All records are all sorted!")

    else:
        print("Invalid option!")

    # print(list_record)   # Sorted arrangement of tuples in a list

    # Putting the tuples in a list back into a dictionary
    dict_record = {list_record[j][0]: list_record[j][1] for j in range(len(list_record))}
    return dict_record


# Function of Linear search
def linear_search(dict_record, key_choices):
    # making dict_record into a list with tuples
    list_record = list(dict_record.items())

    # search by index
    if key_choices == "1":
        counting = 0
        try:
            # asking user to enter index to find
            index_input = int(input("Enter record index: "))
            # Using a for loop to find and display the index
            for index, info in list_record:
                if index_input == index:
                    counting += 1
                    print("")
                    print("Record index: {}".format(index))
                    for key in info:
                        print(key + ":", info[key])
            # if the index do not exist
            if counting == 0:
                print("No records found!\n")
            else:
                print("Search done!\n")
            return counting

        except ValueError:
            print("Invalid choice\n")

    # search by name
    elif key_choices == "2":
        # asking user for name to search
        name_input = input("Enter name: ")
        counting = 0
        # using a for loop to search for the name and display
        for index, info in list_record:
            if name_input == dict_record[index]["Customer Name"]:
                counting += 1
                print("")
                print("Record index: {}".format(index))
                for key in info:
                    print(key + ":", info[key])
        # if the index do not exist
        if counting == 0:
            print("No records found!\n")
        else:
            print("Search done!\n")
        return counting

    else:
        print("Exit from linear search!\n")
    return None


# Function of Binary Search
def binary_search(dict_record, target):
    # making dict_record into a list with tuples
    list_record = list(dict_record.items())
    # Set the start index to 0 (left)
    start_index = 0
    # Set the end index from the length of the list -1 (right)
    end_index = len(list_record) - 1

    # If the start is lesser or equal to the end index (left <= right) continue
    while start_index <= end_index:
        # midpoint index
        midpoint = math.floor((end_index + start_index) / 2)
        # midpoint value
        midpoint_value = list_record[midpoint][0]
        # check if the mid point value is the same as the target input
        if midpoint_value == target:
            # Return the midpoint index
            return midpoint

        # if target is lesser than midpoint value
        # the end index (right) will become the midpoint index - 1
        elif target < midpoint_value:
            end_index = midpoint - 1

        # if the target is more than midpoint value
        # the start index (left) will become the midpoint index + 1
        else:
            start_index = midpoint + 1

    # If there is no such target found, return None
    return None


# Function of interpolation search
def interpolation_search(dict_record, target):
    # making dict_record into a list with tuples
    list_records = list(dict_record.items())
    low = 0
    high = len(list_records) - 1
    while list_records[high][0] != list_records[low][0] and list_records[low][0] <= target <= list_records[high][0]:
        # Estimate mid
        mid = low + ((target - list_records[low][0]) * (high - low) // (list_records[high][0] - list_records[low][0]))

        # target is found
        if target == list_records[mid][0]:
            return mid

        # discard all elements in the right search space,
        # including the middle element
        elif target < list_records[mid][0]:
            high = mid - 1

        # discard all elements in the left search space,
        # including the middle element
        else:
            low = mid + 1

    # if the target is found
    if target == list_records[low][0]:
        return low

    # target doesn't exist in the list
    return None


# Test Programme
while choice != "7":
    print("Select your choice:")
    print("1 --> Add record")
    print("2 --> Update record")
    print("3 --> Remove record")
    print("4 --> Display record")
    print("5 --> Sort records")
    print("6 --> Search records")
    print("7 --> Exit Application")
    choice = input("Enter your choice: ").strip()

    # Add records
    if choice == "1":
        print("")
        if len(records) < 20:
            count = add_record(count)
        else:
            print("You have reach the maximum records!")
        print("")

    # Update records
    elif choice == "2":
        print("")
        valid_index = False
        while valid_index is False:
            try:
                index = int(input("Enter the index that you want to change (Enter -1 to exit): "))
                if index == -1:
                    valid_index = True
                    break
                for i in records:
                    if index == i:
                        valid_index = True
                if valid_index is True:
                    update_record(index)
                else:
                    print("No such index number, try again")
            except ValueError:
                print("Invalid index number, try again!")
        print("")

    # Delete record
    elif choice == "3":
        valid_index = False
        while valid_index is False:
            try:
                index = int(input("Enter the index that you want to remove (Enter -1 to exit): "))
                if index == -1:
                    valid_index = True
                    break
                for i in records:
                    if index == i:
                        valid_index = True
                if valid_index is True:
                    remove_record(index)
                else:
                    print("No such index number, try again")
            except ValueError:
                print("Invalid index number, try again!")
        print("")

    # Display records
    elif choice == "4":
        if len(records) == 0:
            print("\nNo records to display!")
        else:
            for index, info in records.items():
                print("\nRecord index: {}".format(index))
                for key in info:
                    print(key + ":", info[key])
        print("")

    # Sort records
    elif choice == "5":
        # Sort option (to have 3 types of sort for user to choose)
        # Check if there is any record
        if len(records) == 0:
            print("\nNo records to sort!")
        else:
            print("\nTypes of sorts:")
            print("1 ---> Bubble sort")
            print("2 ---> Selection sort")
            print("3 ---> Insertion sort")
            sort_choice = input("Please type the number to select the type of sort (press any other key to exit): ")

            # Bubble sort
            if sort_choice == "1":
                print("Bubble sort")
                order = input("Type 'a' for ascending order and 'd' for descending order: ").upper()
                while order != "A" and order != "D":
                    print("Invalid input!")
                    order = input("Type 'a' for ascending order and 'd' for descending order: ").upper()
                records = bubble(records, order)
                print("All records are all sorted!\n")

            # Selection sort
            elif sort_choice == "2":
                print("Selection sort")
                order = input("Type 'a' for ascending order and 'd' for descending order: ").upper()
                while order != "A" and order != "D":
                    print("Invalid input!")
                    order = input("Type 'a' for ascending order and 'd' for descending order: ").upper()
                records = selection(records, order)
                print("")

            # Insertion sort
            elif sort_choice == "3":
                print("Insertion sort")
                order = input("Type 'a' for ascending order and 'd' for descending order: ").upper()
                while order != "A" and order != "D":
                    print("Invalid input!")
                    order = input("Type 'a' for ascending order and 'd' for descending order: ").upper()
                records = insertion(records, order)
                print("")

            # Exit from sort
            else:
                print("Exit from sort!\n")

    # Search records
    elif choice == "6":
        # Search option (to have 2 types of search for user to choose)
        print("\n1 ---> Linear Search")
        print("2 ---> Binary Search")
        print("3 ---> Interpolation Search")
        search_choice = input("Enter number to choose the type of search (press any other key to exit): ")

        # Linear search
        if search_choice == "1":
            print("\n1 ---> Record index")
            print("2 ---> Customer name")
            key_choice = input("Enter the number that you would like to search by (Enter any other key to exit): ")
            print("")
            linear_search(records, key_choice)

        # Binary search
        elif search_choice == "2":
            print("")

            # Sort to make sure method can work
            records = selection(records, "A")
            validation = True
            while validation is True:
                try:
                    index_input = int(input("Enter record index: "))
                    validation = False
                    if binary_search(records, index_input) is not None:
                        list_b = list(records.items())[binary_search(records, index_input)]
                        list_a = {int(list_b[0]): list_b[1]}

                        for index, info in list(list_a.items()):
                            print("")
                            print("Record index: {}".format(index))
                            for key in info:
                                print(key + ":", info[key])

                    else:
                        print("No records found")
                    print("")
                except ValueError:
                    print("This is an invalid record index, try again!")

        elif search_choice == "3":
            print("")

            # Sort to make sure method can work
            records = selection(records, "A")
            validation = True
            while validation is True:
                try:
                    index_input = int(input("Enter record index: "))
                    validation = False
                    if interpolation_search(records, index_input) is not None:
                        list_b = list(records.items())[interpolation_search(records, index_input)]
                        list_a = {int(list_b[0]): list_b[1]}

                        for index, info in list(list_a.items()):
                            print("")
                            print("Record index: {}".format(index))
                            for key in info:
                                print(key + ":", info[key])

                    else:
                        print("No records found")
                    print("")
                except ValueError:
                    print("This is an invalid record index, try again!")

        else:
            print("Exit from search!\n")

    elif choice == "7":
        print("Program has ended! ")
        exit()

    else:
        print("Please choose the correct options, try again!\n")
