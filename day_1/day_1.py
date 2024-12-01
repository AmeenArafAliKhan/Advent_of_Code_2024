# col_1 and col_2 are created using shell command: awk '{print $1}' your_input_file.txt > output_file.txt

with open('col_1.txt', 'r') as file:
    list1 = [int(line.strip()) for line in file]

list1.sort()

with open('col_2.txt', 'r') as file:
    list2 = [int(line.strip()) for line in file]

list2.sort()


res = sum(abs(a-b) for a, b in zip(list1, list2))

print(res)

#Part 2 is sovled using a frequency_dict to count how many times the numbers in list2 appears and then comparing that with the numbers in list1

frequency_dict = {}

for num in list2:
    frequency_dict[num] = frequency_dict.get(num, 0) + 1

final_res = sum(num * frequency_dict.get(num,0) for num in list1)

print(final_res)