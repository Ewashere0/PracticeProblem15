#Arrange all of the digits from the numbers 1 through 15 
#in such a order that the sum of any adjacent pair
#is a perfect square. No repeats.

import math

sequence = []

def nextNum():
    duplicate = False
    if len(sequence) == 15:
        print(sequence)
        return
    for x in range(15):
        sequence.append(x + 1)
        for y in range(len(sequence) - 1): #minus one to not check the newest number as a dupe of itself
            if sequence[len(sequence) - 1] == sequence[y]:
                del sequence[-1]
                duplicate = True
                break
        if duplicate == True:
            duplicate = False
            continue
        if perfectSquare():
            nextNum()
        del sequence[-1]

def perfectSquare():
    if math.sqrt(sequence[len(sequence) - 1] + sequence[len(sequence) - 2]) % 1 == 0:
        return True
    else:
        return False

for x in range(15):
    sequence.append(x + 1)
    nextNum()
    del sequence[-1]
