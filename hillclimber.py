from solution import SOLUTION
import constants as c
import copy
class HILL_CLIMBER:
    def __init__(self) -> None:
        self.parent = SOLUTION()
        self.child = None

    def evolve(self):
        self.parent.Evaluate("GUI")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Select()
        self.Print()

    def Print(self):
        print("Parent fitness: "+str(self.parent.fitness)+", Child fitness: "+str(self.child.fitness))

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.mutate()

    def Select(self):
        if (self.parent.fitness < self.child.fitness):
            self.parent = self.child

    def Show_Best(self):
        self.parent.Evaluate("GUI")