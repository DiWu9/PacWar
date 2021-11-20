import _PyPacwar
import numpy


# Example Python module in C for Pacwar
def main():

    ones = [1] * 50
    threes = [3] * 50

    # some genes discovered for submission 3, better than submission 2, but generally worse than submission 3
    best0 = [0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 3, 3, 3, 0, 3, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 2, 1, 3, 0, 1, 3, 0, 0, 3, 1, 1, 3, 1]
    best1 = [0, 3, 1, 0, 0, 0, 0, 0, 0, 3, 1, 1, 0, 2, 0, 0, 3, 3, 0, 0, 3, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 0, 2, 1, 1, 2, 2, 1, 3, 1, 1, 3, 1, 2, 3, 1, 1, 3, 1]
    best2 = [0, 3, 1, 0, 0, 0, 0, 0, 3, 1, 1, 0, 0, 2, 2, 0, 3, 3, 0, 3, 3, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 3, 2, 1, 1, 2, 1, 1, 3, 1, 1, 3, 0, 1, 3, 0, 1, 3, 1]

    # kill all threes at round 61 with remaining 129, all ones at round 48 and remaining 136
    submission2 = [0, 3, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 0, 2, 3, 3, 0, 0, 3, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 2, 3, 2, 1, 1, 2, 1, 1, 3, 1, 1, 3, 0, 1, 0, 0, 1, 3, 1]
    submission3 = [0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3, 0, 3, 0, 3, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 3, 0, 1, 3, 1, 0, 3, 1, 1, 3, 0]

    print("Example Python module in C for Pacwar")
    (rounds, c1, c2) = _PyPacwar.battle(submission2, submission3)
    print("Number of rounds:", rounds)
    print("Final remaining:", c1)
    print("Submission3 remaining:", c2)


if __name__ == "__main__":
    main()
