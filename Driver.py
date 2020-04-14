class Driver:
    def __init__(self, model, nameArg, ageArg, steeringArg, stabilityArg):
        self.name = nameArg
        self.age = ageArg
        self.steeringFactor = steeringArg
        self.stabilityFactor = stabilityArg

    def writeString(self):
        return_string = ("\"" + self.name + "\"\t" + self.age + "\t" + self.steeringFactor + "\t" + self.stabilityFactor + "\n")
        return return_string

    def toString(self):
        return self.name
    