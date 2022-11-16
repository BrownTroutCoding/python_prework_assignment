# Question 1

# Write a function to print "hello_USERNAME!"
# USERNAME is the input of the function.
# The first line of the code has been defined as below.

# First, defines hello_name.
def hello_name(user_name):
    """Prints a simple greeting."""
    # Prints user_name as a complete string.
    print('hello_' + user_name + '!')
# Call function and enters username as 'USERNAME'. This would be a funny username!
hello_name('USERNAME')


# Question 2

# Write a python function, first_odds that prints the
# odd numbers from 1-100 and returns nothing.

def first_odds():
    """counts all odd numbers from 1-100."""
    # takes first_odds and counts by 2, from 1 to 100
    for first_odds in range(1,101,2):
        print(first_odds)
# Call function, which prints due to previous 'for' loop.
first_odds()


# Question 3

# Please write a Python function, max_num_in_list to return the max number of a given list.
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    """Prints the largest number in the list"""
    # returns maximum number in a_list.
    return max(a_list)

# Creates list for a_list. Could us input if dev wanted user to make list.
a_list = [1000, 1100, 1101, 1111, 1010]
# Prints max number in string.
print('The largest number in the list is: ', max_num_in_list(a_list))


# Question 4 version 1

# Write a function to return if the given year is a leap year.
# # A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
# # The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """Checking if the given year is a leap year."""
    # if a_year is divisible by 400, it is a leap year.
    if a_year % 400 == 0:
        return True
    # if a_year is divisble by 4 but not 100, it is a leap year.
    if a_year % 4 == 0 and a_year % 100 != 0:
        return True
    else:
        return False

# Input for user to enter a year, converts into integer.
enter_year = int(input('Enter any year and I will tell you it if is a leap year: '))
# if integer == True, prints as 'a leap year'.
if is_leap_year(enter_year):
    print(enter_year, 'is a leap year.')
#if integer == False, prints as 'not a leap year'.
else:
    print(enter_year, 'is not a leap year.')


#Question 4 version 2
def is_leap_year(a_year):
    """Checking if the given year is a leap year."""
    #returns if the year is divisible by 400 or just by 4 and not 100.
    return a_year % 400 == 0 or (a_year % 4 == 0 and a_year % 100 != 0)

# Input for user to enter a year, converts into integer.
enter_year = int(input('Enter any year and I will tell you it if is a leap year: '))
# if integer == True, prints as a 'leap year'.
if is_leap_year(enter_year):
    print(enter_year, 'is a leap year.')
#if integer == False, prints as 'not a leap year'.
else:
    print(enter_year, 'is not a leap year.')


# Question 5 version 1

# Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
# The return should be boolean Type.
def is_consecutive(a_list):
    """Checking to see if all numbers in the list for consecutive."""
    # Sorting the list
    sorted_a_list = sorted(a_list)
    # Sorted a_list with min to max.

    # Making a sorted_list with the sorted numbers from a_list.
    # Add +1 to max to test whether list is consecutive.
    consecutive_list = list(range(min(a_list), max(a_list) + 1))

    return sorted_a_list == consecutive_list

# Create a_list numbers
a_list = [1,2,3,4,5,6]
# if a_list is returned, print 'This list is consecutive'.
if is_consecutive(a_list):
    print('This list is consecutive', a_list)
# if a_list is not returned, print 'This list is not consecutive'.
else:
    print('This list is not consecutive', a_list)


# Question 5 version 2
def is_consecutive(a_list):
    """Checking to see if all numbers in the list for consecutive."""
    # Returns list if sorted a_list == consecutive numbers
    # Similar to code above, except no need to name second list.
    # Immediately returns if lists == eachother.
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

# Create a_list numbers
a_list = [1,2,3,4,5,7]
# if a_list is returned, print 'This list is consecutive'.
if is_consecutive(a_list):
    print('This list is consecutive', a_list)
# if a_list is not returned, print 'This list is not consecutive'.
else:
    print('This list is not consecutive', a_list)