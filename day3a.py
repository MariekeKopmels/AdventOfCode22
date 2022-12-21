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
    
    for line in input:
        # First, remove the "\n" characters from the string
        line = line.replace("\n", "")
        
        # Identify the two compartments
        half = int(len(line)/2)
        compartment_one = line[:half]
        compartment_two = line[half:]
        print(compartment_one)
        print(compartment_two)
        shared_item = list(set(compartment_one) & set(compartment_two))

        # Calculate the priority, add it to the sum
        priority_sum = priority_sum + get_priority(shared_item[0])
        
    print("Priority sum: ", priority_sum)