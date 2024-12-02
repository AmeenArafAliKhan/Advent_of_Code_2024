#This function feels like magic. return False, True, False *_*
def is_safe(row):
    if row == sorted(row) or row == sorted(row, reverse = True):
        for i in range(len(row)-1):
            if not (1 <= abs(row[i]-row[i+1]) <= 3):
                return False
        return True
    return False

res = 0
with open("input.txt", "r") as file:
    for line in file:
        row = list(map(int, line.strip().split()))
        if is_safe(row):
            res +=1
print(res)

final_res = 0
with open("input.txt", "r") as file:
    for line in file:
        row = list(map(int, line.strip().split()))
        if is_safe(row):
            final_res +=1
        else:
            for i in range(len(row)):
                temp_row = row[:i] + row[i+1:]    #Python trick to remove 'i'th position element from this list in each iteration of the loop
                if is_safe(temp_row):
                    final_res += 1
                    break
    print(final_res)

