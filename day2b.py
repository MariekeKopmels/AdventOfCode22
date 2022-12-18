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

# We know 1 beats 2, 2 beats 3 and 3 beats 1
def response(opponent, outcome):
    # For a tie
    if outcome == "Y": 
        return options[opponent]
    # For losing
    if outcome == "Z":
        if options[opponent]+1 == 3:
            return 3
        else:
            return (options[opponent]+1)%3
    # For a win
    if outcome == "X":
        if options[opponent]+2 == 3:
            return 3
        else:
            return (options[opponent]+2)%3
        
if __name__ == '__main__':
    input = open("input/day2.txt")
    
    score = 0
    nr = 0
    for line in input:
        opponent, outcome = line[0], line[2]
        res = response(opponent, outcome)
        opponent = options[opponent]
        outcome = options[outcome]
        
        print("opponent: ", opponent, "response: ", res, " outcome: ", outcome)
        
        if outcome == 1:
            score = score + LOSE + res
        elif outcome == 2:
            score = score + TIE + res
        else:
            score = score + WIN + res
        nr = nr + 1
        
    print(score)

            
            
