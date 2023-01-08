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

#part 2:
# X = Lose
# Y = Draw
# Z = Win

#Rules matrix where Col 0 = Rock(1p), Col 1 = Paper(2p), Col 2 = Scissor(3p)
rules = [
    ["C X", "A Y", "B Z"], #Row 0 = Winning scenarios
    ["A X", "B Y", "C Z"], #Row 1 = Draw scenarios
    ["B X", "C Y", "A Z"]  #Row 2 = Losing scenarios
]

#Rules matrix for part 2 where Col 1 = Draw scenario, Col 2 = Winning scenario.  
rules2 = [
    ["B X", "A Y", "C Z"], #Scenario where we need to pick Rock
    ["C X", "B Y", "A Z"], #Scenario where we need to pick Paper
    ["A X", "C Y", "B Z"]  #Scenario where we need to pick Scissor
]

file = open("C:/Users/edgar/Documents/python/AdventOfCode22/Day_2/input.txt", "r")

score = 0 
score2 = 0

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

            if line == rules2[x][y]:
                if y == 1:
                    score2 += 3
                elif y == 2:
                    score2 += 6

                if x == 0:
                    score2 += 1
                elif x == 1:
                    score2 += 2
                elif x == 2:
                    score2 += 3

print("Score for part 1 " + str(score))
print("Score for part 2 " + str(score2))
