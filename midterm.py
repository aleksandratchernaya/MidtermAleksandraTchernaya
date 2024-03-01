#1
a = 16
a = a // 2
print(a**2)
a = a + 11
print(a+1)
a = a - 3

#2
print((3+10**2/2) or 70.0)

#3
import datetime
a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

#4
# Define the function to check if a string is a palindrome
def palindrome(word):
    return word == word[::-1]
# Given strings to check
strings = [
    "6892149109325320763773670235239019412986",
    "9847255590886266818998186626880955527489",
    "1414884937242655719669145562427394884141",
    "6800923757255865070000705685527573290086"
]

not_palindromes = [s for s in strings if not palindrome(s)]
print(not_palindromes)

#5
def find_un_an_occurrences(text):
    # Initialize a counter to keep track of pattern matches
    count = 0

    # Iterate over each index in the text
    for i in range(len(text)):
        # Try to extract a substring that potentially matches our pattern
        # We look ahead for the length of the shortest possible match ("unan" = 4 characters) and extend to the end of the string to ensure we don't miss longer matches.
        for j in range(i + 4, len(text) + 1):
            substring = text[i:j]

            # Check if the substring matches our pattern
            if substring.startswith('un') and substring.endswith('an'):
                count += 1

    return count

# Example usage
text = "I am unsure if the plan for an unconventional plan was undertaken by an unknown man."
print(find_un_an_occurrences(text))

#6
# Original string
my_string = "hello"
print("Original string:", my_string)


# Attempt to change the first character
try:
    my_string[0] = "H"
except TypeError as e:
    print("Error:", e)


# Demonstrating string "modification" creates a new string
modified_string = "H" + my_string[1:]
print("Modified string:", modified_string)
print("Original string after attempt to modify:", my_string)

# Original list
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)


# Modify the first element
my_list[0] = 10
print("List after modification:", my_list)


# Add an element
my_list.append(6)
print("List after adding an element:", my_list)


# Remove an element
my_list.remove(3)
print("List after removing an element:", my_list)

#7
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

import random

# Generate a list of 10 random numbers
random_numbers = [random.randint(1, 100) for i in range(10)]

# Process the list to remove odd numbers and double even numbers
processed_numbers = [num * 2 for num in random_numbers if num % 2 == 0]

# Print the processed list
print(processed_numbers)

#8
def is_valid_url(url):
    # Check if the URL starts with "http://" or "https://"

    if url.startswith("http://") or url.startswith("https://"):
        # If the URL starts with either "http://" or "https://", it meets the basic criteria
        # Therefore, we return True to indicate this.
        return True
    else:
        # If the URL does not start with the expected prefixes we consider
        # it invalid and return False.
        return False

#9
def days_since_birthday(birthday):
    # Convert the birthday string to individual components
    day, month, year = birthday.split("/")

    # Convert the year to an integer
    birth_year = int(year)

    # For simplicity, let's assume the current year is 2024, as we're not using datetime
    current_year = 2024

    # Calculate the number of full years since the birth year
    full_years = current_year - birth_year - 1  # Exclude birth year and current year

    # Estimate the number of days in the full years, assuming 365.25 days per year
    total_days = full_years * 365.25

    return int(total_days)


# Example usage with my birthday
birthday = "09/07/2004"  # Note: Adjusted to DD/MM/YYYY format as per the function's requirement
days = days_since_birthday(birthday)
print(f"Days passed (excluding birth year and current year): {days}")

