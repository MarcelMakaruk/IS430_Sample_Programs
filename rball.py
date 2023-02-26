from random import random


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)


def printIntro():
    print('This program simulates a game of racquetball between two')
    print('players called "A" and "B". The ability of each player is')
    print('indicated by a probability (a number between 0, and 1) that')
    print('the player wins the point when serving. Player A always')
    print('has the first serve.')


def getInputs():
    # Returns the three simulation parameters probA, probB, and n
    a = float(input('What is the prob. player A wins a serve? '))
    b = float(input('What is the prob. player B wins a serve? '))
    n = int(input('How many games to simulate? '))
    return a, b, n


def simNGames(n, probA, probB):
    winsA = winsB = 0

    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


def simOneGame(probA, probB):
    scoreA = scoreB = 0
    serving = 'A'
    while not gameOver(scoreA, scoreB):
        if serving == 'A':
            if random() < probA:
                scoreA += 1
            else:
                serving = 'B'
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = 'A'
    return scoreA, scoreB


def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise
    return a == 15 or b == 15


def printSummary(winsA, winsB):
    # Prints a summary of wins for each player
    n = winsA + winsB
    print(f'\nGames simulated: {n}')
    print('Wins for A: {0} ({1:0.1%})'.format(winsA, winsA/n))
    print('Wins for B: {0} ({1:0.1%})'.format(winsB, winsB/n))


if __name__ == '__main__':
    main()
