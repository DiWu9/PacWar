import _PyPacwar
import random
import numpy as np

# Example Python module in C for Pacwar


def main():
    """
    ones = [1] * 50
    threes = [3] * 50
    print("Example Python module in C for Pacwar")
    print("all ones versus all threes ...")
    (rounds, c1, c2) = _PyPacwar.battle(ones, threes)
    print("Number of rounds:", rounds)
    print("Ones PAC-mites remaining:", c1)
    print("Threes PAC-mites remaining:", c2)
    """
    ones = [1] * 50
    threes = [3] * 50
    
    g = [random.randint(0, 3) for i in range(50)]
    print("Initial random gene: ", g)
    while (True):
        max_score = 0
        best_nbr = None
        for i in range(50):

            # find neighbor
            nbr = g.copy()
            if (g[i] == 3):
                nbr[i] = 0
            else:
                nbr[i] += 1

            (rounds, c1, c2) = _PyPacwar.battle(g, nbr)
            if (c1 == 0 and c2 > 0):
                if np.divide(c2-c1, rounds) > max_score:
                    max_score = np.divide(c2-c1, rounds)
                    best_nbr = nbr

        if (best_nbr is None): 
            print("No better neighbor found. Retuning the answer: ", g)
            (rounds, c1, c2) = _PyPacwar.battle(g, ones)
            if (c2 == 0):
                print("Win all-one!")
            (rounds, c1, c2) = _PyPacwar.battle(g, threes)
            if (c2 == 0):
                print("Win all-three!")
            return
        
        g = best_nbr
        print("Best neighbor", g)

if __name__ == "__main__":
    #main()
    '''
    ones = [1] * 50
    threes = [3] * 50
    betterThanOnes = [3, 1, 1, 3, 0, 2, 0, 0, 1, 1, 1, 1, 0, 2, 2, 1, 3, 0, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 2, 2, 3, 3, 1, 0, 1, 1, 3, 2, 0, 2, 1, 2, 3]
    betterThanOnes2 = [1, 0, 1, 2, 0, 0, 0, 0, 1, 1, 0, 1, 3, 2, 2, 2, 1, 3, 0, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 1, 3, 1, 3, 1, 3, 3, 3, 2, 3, 1, 3, 1, 0, 0, 1, 1, 2, 2, 0, 0]
    betterThanThrees = [3, 3, 3, 2, 0, 2, 1, 2, 3, 3, 3, 3, 0, 2, 0, 0, 0, 1, 1, 1, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3, 3, 2, 3, 1, 3, 3, 3, 0, 3, 1, 1, 2, 0]
    betterThanThrees2 = [1, 1, 1, 0, 0, 0, 2, 0, 1, 1, 1, 1, 2, 3, 2, 1, 3, 1, 1, 2, 3, 3, 0, 2, 3, 3, 2, 2, 3, 3, 2, 3, 3, 3, 1, 3, 3, 3, 2, 1, 1, 0, 3, 3, 3, 2, 2, 1, 0, 2]
    better = [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 3, 3, 3, 3, 2, 1, 1, 0, 0, 1, 2, 3, 3, 3, 0, 0, 1, 0, 3, 3, 1, 3, 3, 2, 3, 3, 1, 3, 2, 1, 1, 2, 1, 2, 0, 2, 3, 2, 3]
    (rounds, c1, c2) = _PyPacwar.battle(better, ones)
    print("Number of rounds:", rounds)
    print("Better PAC-mites remaining:", c1)
    print("Threes PAC-mites remaining:", c2)
    '''
    betterThanThrees = [3, 3, 3, 2, 0, 2, 1, 2, 3, 3, 3, 3, 0, 2, 0, 0, 0, 1, 1, 1, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3, 3, 2, 3, 1, 3, 3, 3, 0, 3, 1, 1, 2, 0]

    str = "3, 3, 3, 2, 0, 2, 1, 2, 3, 3, 3, 3, 0, 2, 0, 0, 0, 1, 1, 1, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3, 3, 2, 3, 1, 3, 3, 3, 0, 3, 1, 1, 2, 0"
    list = str.split(", ")
    s = ''.join(list)
    print(s)