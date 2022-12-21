# Advent of Code 2022
# Marieke Kopmels

import re

def intersects(sections):
    sections_A = set(list(range(int(sections[0]), (int(sections[1])+1))))
    sections_B = set(list(range(int(sections[2]), (int(sections[3])+1))))

    intersects = sections_A.intersection(sections_B)

    if len(intersects) == 0:
        return 0
    return 1

if __name__ == '__main__':
    input = open("input/day4.txt")
    total_intersecting = 0 
    
    for line in input:
        line = line.replace("\n", "")
        sections = re.split(r"\W+", line)
        if intersects(sections):
            total_intersecting = total_intersecting + 1
    
    print("Total number of assignment pairs intersecting with the other: ", total_intersecting)