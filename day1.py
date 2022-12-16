# Advent of Code 2022
# Marieke Kopmels

if __name__ == '__main__':
    input = open("input/day1.txt")
    line = input.readline()
    
    max = [0, 0, 0]
    current = 0
    while line != '':
        max = sorted(max)
        if line != "\n":
            current += int(line)
        else:
            if current > max[0]:
                max[0] = current
            current = 0
        line = input.readline()
        
    print(sum(max))
    
        
        
        
        
        
        

    







