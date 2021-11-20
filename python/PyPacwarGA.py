import _PyPacwar
import random


class GeneticAlgorithm:

    def __init__(self):
        self.population = []
        self.candidates = []
        self.U = [0, 4]
        self.V = [4, 20]
        self.W = [20, 23]
        self.X = [23, 26]
        self.Y = [26, 38]
        self.Z = [38, 50]
        self.functions = [self.U, self.V, self.W, self.X, self.Y, self.Z]
        self.mutationRate = 0.02
        self.candidateSize = 10
        self.populationSize = 100
        self.bestLocalGene = None
        self.bestGene = None
        self.bestScore = 0
        self.allOnes = [1] * self.populationSize
        self.allThrees = [3] * self.populationSize
        self.bestKiller = [0, 3, 1, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3, 3, 0, 0, 3, 1, 1, 1, 2, 1, 1, 2, 1, 1,
                           2, 1, 1, 2, 1, 1, 2, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1]

    def reset(self):
        self.population = []
        self.candidates = []
        self.bestLocalGene = None
        self.bestGene = None
        self.bestScore = 0

    def setUpCandidates(self):
        """
        set up competitive pool that is used for testing the quality of gene
        """
        self.candidates = []
        for j in range(self.candidateSize-2):
            candidate = [random.randint(0, 3) for i in range(50)]
            self.candidates.append(candidate)
        self.candidates.append(self.allOnes)
        self.candidates.append(self.allThrees)

    def setUpPopulation(self):
        for i in range(self.populationSize-2):
            randomGene = [random.randint(0, 3) for i in range(50)]
            self.population.append(randomGene)
        self.population.append(self.allOnes)
        self.population.append(self.allThrees)

    def setPopulation(self, genes):
        self.population = genes[:self.populationSize-3]
        self.population.append(self.bestKiller)
        self.population.append(self.allOnes)
        self.population.append(self.allThrees)

    def setCandidates(self, genes):
        self.candidates = genes[len(genes)-self.candidateSize+3:]
        self.candidates.append(self.bestKiller)
        self.candidates.append(self.allOnes)
        self.candidates.append(self.allThrees)

    def fitness(self, gene):
        """
        evaluate the quality of the gene by letting it competing with the candidates
        in the pool.
        """
        score = 0
        for candidate in self.candidates:
            round, nCandidate, nGene = _PyPacwar.battle(candidate, gene)
            score += (nGene - nCandidate) / round
        return max(int(score), 0)

    def selection(self):
        localBestGene = None
        localBestScore = 0
        totalScore = 0
        scores = []
        for gene in self.population:
            score = self.fitness(gene)
            scores.append(score)
            totalScore += score
            if localBestScore < score:
                localBestGene = gene
                localBestScore = score

        self.bestLocalGene = localBestGene
        if localBestScore > self.bestScore:
            # print("New Highest Score: {}!".format(localBestScore))
            self.bestScore = localBestScore
            self.bestGene = localBestGene

        probInterval = []
        prevScore = 0
        for score in scores:
            probInterval.append((prevScore + score) / totalScore)
            prevScore += score

        # Generate new population with prob based on genes' score
        newPopulation = []
        for i in range(self.populationSize):
            rand = random.uniform(0, 1)
            ithGene = 0
            while probInterval[ithGene] < rand and ithGene < self.populationSize:
                ithGene += 1
            newPopulation.append(self.population[ithGene])
        self.population = newPopulation

        return totalScore, localBestScore

    def easySelection(self):
        """
        drop the worst and add a copy of the best
        """
        fitnesses = [self.fitness(gene) for gene in self.population]
        maxFitness = max(fitnesses)
        localBestGene = self.population[fitnesses.index(maxFitness)]
        if maxFitness > self.bestScore:
            self.bestScore = maxFitness
            self.bestGene = localBestGene
        self.population[fitnesses.index(min(fitnesses))] = localBestGene  # replace worst with best
        return sum(fitnesses), maxFitness

    def crossover(self, i1, i2):
        """
        do a one point crossover for each function
        i1, i2: index of gene in population
        """
        res1 = []
        res2 = []
        cpts = [random.randint(function[0], function[1]) for function in self.functions]  # crossover points
        gene1 = self.population[i1]
        gene2 = self.population[i2]
        for i in range(len(self.functions)):
            function = self.functions[i]
            cpt = cpts[i]
            res1 += gene1[function[0]:cpt] + gene2[cpt:function[1]]
            res2 += gene2[function[0]:cpt] + gene1[cpt:function[1]]
        self.population[i1] = res1
        self.population[i2] = res2

    def mutation(self):
        for gene in self.population:
            for i in range(len(gene)):
                if random.uniform(0, 1) < self.mutationRate:
                    gene[i] = random.randint(0, 3)

    def isConverged(self, score):
        """
        converge when average population score difference <= 0.1 twice
        """
        if score[0] is None or score[1] is None or score[2] is None:
            return False
        return abs(score[0]-score[1]) <= 0.01 and abs(score[1]-score[2]) <= 0.01

    def toString(self, gene):
        s = ""
        for num in gene:
            s += str(num)
        return s

    def getBetterCandidates(self, n):
        """
        use random candidate pool to find n better candidates
        """
        better_candidates = []
        for x in range(n):
            self.reset()
            self.setUpCandidates()
            self.setUpPopulation()
            scores = [None, None, None]  # population average in the last three rounds
            currRound = 1
            while True:
                # selection
                score, localBestScore = self.selection()
                avgScore = score / self.populationSize

                # print status
                """
                print("Iteration {}: ".format(currRound))
                print("Local Best Score: {}.".format(localBestScore))
                print("Local Best Gene: {}.".format(self.bestLocalGene))
                print("Global Best Score: {}.".format(self.bestScore))
                print("Current Best Gene: {}.".format(self.bestGene))
                print("Avg score: {}.".format(avgScore))
                print("Latest scores: {}.".format(scores))
                print("\n")
                """

                # convergence check
                if self.isConverged(scores):
                    print("Found {}th better gene for the pool.".format(x+1))
                    print("String: {}.".format(self.toString(self.bestGene)))
                    better_candidates.append(self.bestGene)
                    # print("Population: {}.".format(self.population))
                    break

                # crossover
                for i in range(0, len(self.population), 2):
                    self.crossover(i, i + 1)

                # mutation
                self.mutation()

                scores[2] = scores[1]
                scores[1] = scores[0]
                scores[0] = avgScore
                currRound += 1

        better_candidates.append(self.allOnes)
        better_candidates.append(self.allThrees)
        return better_candidates

    def run(self):
        """
        self.population = self.getBetterCandidates(self.populationSize)  # takes lot of time to find 80 better gene
        but the random population will make the total score to be 0
        """
        genes = readGene("genes.txt")
        self.reset()
        self.setPopulation(genes)
        self.setCandidates(genes)
        print("Population size: {}.".format(len(self.population)))
        print("Candidate size: {}.".format(len(self.candidates)))
        print("Starting to find best gene: ")

        scores = [None, None, None]  # population average score in the last three rounds
        currRound = 1
        while True:
            # selection
            score, localBestScore = self.selection()
            avgScore = score / self.populationSize

            # print status
            print("Iteration {}: ".format(currRound))
            print("Local Best Score: {}.".format(localBestScore))
            print("Local Best Gene: {}.".format(self.bestLocalGene))
            print("Global Best Score: {}.".format(self.bestScore))
            print("Global Best Gene: {}.".format(self.bestGene))
            print("Avg score: {}.".format(avgScore))
            print("\n")

            # convergence check
            if self.isConverged(scores):
                best = ""
                for num in self.bestGene:
                    best += str(num)
                print("Best Gene: " + best)
                print("Population: {}.".format(self.population))
                return

            # crossover
            for i in range(0, len(self.population), 2):
                self.crossover(i, i + 1)

            # mutation
            self.mutation()

            scores[2] = scores[1]
            scores[1] = scores[0]
            scores[0] = avgScore
            currRound += 1


def readGene(filename):
    genes = []
    file = open(filename, 'r')
    lines = file.readlines()
    for line in lines:
        # print(line)
        if line.startswith("String:"):
            gene = line.split(" ")[1]
            gene = gene[0:len(gene)-2]
            gene_list = []
            for x in gene:
                gene_list.append(ord(x)-ord('0'))
            genes.append(gene_list)
    print("Loaded {} genes from {}.".format(len(genes), filename))
    return genes


def main():
    solver = GeneticAlgorithm()
    # better_candidates = solver.getBetterCandidates(10)
    # print(better_candidates)
    # list = []
    # solver.selection()
    # solver.getBetterCandidates(20)
    print(solver.toString([0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3, 0, 3, 0, 3, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 3, 0, 1, 3, 1, 0, 3, 1, 1, 3, 0]))
    # solver.run()


if __name__ == '__main__':
    main()
