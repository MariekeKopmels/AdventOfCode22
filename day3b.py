# Advent of Code 2022
# Marieke Kopmels

from curses.ascii import isupper


def get_priority(shared_item):
    if isupper(shared_item):
        return ord(shared_item)-64+26
    else:
        return ord(shared_item)-96


if __name__ == '__main__':
    input = open("input/day3.txt")
    priority_sum = 0
    
    line_number = 0
    lines = [0, 0, 0]
    
    for line in input:
        # First, remove the "\n" characters from the string
        line = line.replace("\n", "")
        lines[line_number%3] = line
        line_number = line_number + 1
        
        # Check which item is shared among the three elves
        if line_number == 3: 
            shared_item = list(set(lines[0]) & set(lines[1]) & set(lines[2]))
        
            # Calculate the priority, add it to the sum
            priority_sum = priority_sum + get_priority(shared_item[0])
            
            line_number = 0
        
    print("Priority sum: ", priority_sum)