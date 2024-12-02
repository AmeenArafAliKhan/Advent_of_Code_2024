# Advent_of_Code_2024
My solutions to the Advent Of Code puzzles 2024. https://adventofcode.com/

## Day 1

This puzzle gives you input which can be copied and stored as a .txt file. From the .txt file, we can get the first and second rows of number using the following shell commands:

```bash
awk '{print $1}' input.txt > col_1.txt
awk '{print $12}' input.txt > col_12.txt
```

## Day 2

A bit more challenging compared to the first one, but still doable. Had to take some external hints to come up with the logic for the second part. 

```python
def is_safe(row):
    if row == sorted(row) or row == sorted(row, reverse = True):
        for i in range(len(row)-1):
            if not (1 <= abs(row[i]-row[i+1]) <= 3):
                return False
        return True
    return False
```
This function lowkey goes hard. 

## Day 3

