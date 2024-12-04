# import re

# with open('input.txt', 'r') as file:
#     res = 0  # Initialize result
#     first_mul_done = False  # Track if the first mul(int, int) has been processed
#     calculate = True  # Track whether to calculate based on the presence of don't() and do()

#     # Loop through each line in the file
#     for line in file:
#         # Updated regex to match mul(int,int), don't(), or do()
#         pattern = r"mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\)"

#         # Find all valid matches
#         matches = re.findall(pattern, line)

#         # Loop through all matches
#         for match in matches:
#             if match[0] != '' and match[1] != '':  # This is a mul(int,int) match
#                 if not first_mul_done:  # Process the first mul(int, int) no matter what
#                     num1, num2 = int(match[0]), int(match[1])
#                     res += num1 * num2  # Multiply and add to result
#                     first_mul_done = True  # Mark that the first mul has been processed
#                 elif calculate:  # Only process if calculations are allowed (i.e. no don't() encountered)
#                     num1, num2 = int(match[0]), int(match[1])
#                     res += num1 * num2  # Multiply and add to result
#             elif match == ("", "", "don't()"):  # This is a don't() match
#                 calculate = False  # Stop calculations until a do() is encountered
#             elif match == ("", "", "do()"):  # This is a do() match
#                 calculate = True  # Resume calculations from the next mul(int, int)

#     # Output the final result
#     print(f"The sum of all products is: {res}")

import re

with open('input.txt', 'r') as file:
    input_str = file.read().strip()

# Updated regex to match mul(int,int), don't(), or do()
pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)" #order of do and dont doesnt amtter

# Find all valid matches
matches = re.findall(pattern, input_str)
# print(matches)
flag = True
res = 0
for match in matches:
    if match == "do()":
        flag = True
    elif match == "don't()":
        flag = False
    else:
        if flag:
            # Extract integers using regular expression
            numbers = re.findall(r'\d+', match)
            # Convert them to integers and assign to variables
            num1 = int(numbers[0])
            num2 = int(numbers[1])
            res += num1 * num2
print(f"The sum of all products is: {res}")

            
