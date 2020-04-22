class Driver:
    # Need to find out how to define a model
    model = Model()

    def __init__(self, nameArg, ageArg, steeringArg, stabilityArg):
        self.name = nameArg
        self.age = ageArg
        self.steeringFactor = steeringArg
        self.stabilityFactor = stabilityArg

    def writeString(self):
        return_string = ("\"" + self.name + "\"\t" + self.age + "\t" + self.steeringFactor + "\t" + self.stabilityFactor + "\n")
        return return_string

    def toString(self):
        return self.name
    