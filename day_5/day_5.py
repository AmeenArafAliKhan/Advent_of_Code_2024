rules = []

with open('input.txt', 'r') as file:
    for line in file:
        rules.append([line[:2], line[3:5]])
print(type(rules[0]))
res = 0

with open('check.txt', 'r') as file:
    for line in file:
        count = 0
        num_list = [int(num ) for num in line.split(',')] 
        print(num_list)
          #Check of order is correct here
        for i in range(len(num_list)-1):
            temp1 = num_list[i]
            temp2 = num_list[i+1]
            for j in rules:
                print(j)
                if j[0] == temp1 and j[1] == temp2:
                    #no problem
                    count +=1 
                elif j[0] == temp2 and j[1] == temp1:
                    count = -1
                    break
                else:
                    continue
            if count == -1:
                break
        if count == len(num_list)-1:
            res += num_list[(len(num_list)-1)//2]
    
    print(res)
            

