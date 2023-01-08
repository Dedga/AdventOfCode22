##Scores:
#Rock 1p, Paper 2p, Scissor 3p
#W 6p, D 3p, L 0p

##Strat:
#A Y
#B X
#C Z

# A = "Rock"
# B = "Paper"
# C = "Scissor"

# X = "Rock"
# Y = "Paper"
# Z = "Scissor"

rules = [
    ["C X", "A Y", "B Z"],
    ["A X", "B Y", "C Z"],
    ["B X", "C Y", "A Z"]
]

file = open("C:/Users/edgar/Documents/python/AdventOfCode22/Day_2/input.txt", "r")

score = 0 

for line in file:
    line = line.replace("\n", "")
    for x in range(3):
        for y in range(3):
            if line == rules[x][y]:
                if x == 0:
                    score += 6
                elif x == 1: 
                    score += 3

                if y == 0:
                    score += 1
                elif y == 1:
                    score += 2
                elif y == 2:
                    score += 3
                break

print(score)
