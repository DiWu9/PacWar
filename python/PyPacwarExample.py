import _PyPacwar
import numpy


# Example Python module in C for Pacwar
def main():

    ones = [1] * 50
    threes = [3] * 50

    # kill all threes at round 61 with remaining 129, all ones at round 48 and remaining 136
    bestKiller = [0, 3, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 0, 2, 3, 3, 0, 0, 3, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 2, 3, 2, 1, 1, 2, 1, 1, 3, 1, 1, 3, 0, 1, 0, 0, 1, 3, 1]

    # some other killer genes
    killer1 = [0, 3, 1, 0, 0, 0, 0, 0, 1, 1, 3, 1, 2, 2, 2, 0, 3, 3, 0, 0, 3, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 0, 2, 2, 1, 2, 2, 1, 3, 1, 1, 2, 0, 0, 3, 0, 2, 2, 3]

    print("Example Python module in C for Pacwar")
    print("all ones versus all threes ...")
    (rounds, c1, c2) = _PyPacwar.battle(ones, bestKiller)
    print("Number of rounds:", rounds)
    print("Ones PAC-mites remaining:", c1)
    print("Best Killer remaining:", c2)


if __name__ == "__main__":
    main()
