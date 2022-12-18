# Advent of Code 2022
# Marieke Kopmels

WIN = 6
TIE = 3
LOSE = 0

options = {
    'A': 1, 
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

if __name__ == '__main__':
    input = open("input/day2.txt")
    
    score = 0
    nr = 0
    for line in input:
        opponent, you = line[0], line[2]
        opponent = options[opponent]
        you = options[you]
        if opponent == you:
            score = score + TIE + you
        elif (opponent == 1 and you == 2) or (opponent == 2 and you == 3) or (opponent == 3 and you == 1):
            score = score + WIN + you
        else:
            score = score + LOSE + you
        
    print(score)

            
            
