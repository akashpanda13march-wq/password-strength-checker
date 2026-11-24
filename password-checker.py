

import string

print("==============================")
print("  PASSWORD STRENGTH CHECKER")
print("==============================")

password = input("Enter a fictional test password: ")

# 1. Length check
length_check = len(password) >= 12

# 2. Uppercase check
uppercase_check = any(char.isupper() for char in password)

# 3. Lowercase check
lowercase_check = any(char.islower() for char in password)

# 4. Number check
number_check = any(char.isdigit() for char in password)

# 5. Special character check
special_check = any(char in string.punctuation for char in password)

# Display all results
print("\n========== CHECK RESULTS ==========")

print("Length check:", "Passed" if length_check else "Failed")
print("Uppercase check:", "Passed" if uppercase_check else "Failed")
print("Lowercase check:", "Passed" if lowercase_check else "Failed")
print("Number check:", "Passed" if number_check else "Failed")
print("Special character check:", "Passed" if special_check else "Failed")

# Overall strength score
score = sum([
    length_check,
    uppercase_check,
    lowercase_check,
    number_check,
    special_check
])

print("\n========== STRENGTH RESULT ==========")
print("Score:", score, "/ 5")

if score <= 2:
    print("Password strength: Weak")
elif score <= 4:
    print("Password strength: Medium")
else:
    print("Password strength: Strong")

