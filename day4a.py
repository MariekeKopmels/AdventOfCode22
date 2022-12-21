# Advent of Code 2022
# Marieke Kopmels

import re

def overlaps(sections):
    sections_A = set(list(range(int(sections[0]), (int(sections[1])+1))))
    sections_B = set(list(range(int(sections[2]), (int(sections[3])+1))))

    differenceA = sections_A.difference(sections_B)
    differenceB = sections_B.difference(sections_A)

    if len(differenceA) == 0 or len(differenceB) == 0:
        return 1
    return 0

if __name__ == '__main__':
    input = open("input/day4.txt")
    total_overlapping = 0 
    
    for line in input:
        line = line.replace("\n", "")
        sections = re.split(r"\W+", line)
        if overlaps(sections):
            total_overlapping = total_overlapping + 1
    
    print("Total number of assignment pairs fully containing the other: ", total_overlapping)