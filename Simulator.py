# Need to find a simulator to use for Python that is equivalent to JPanel for Java
# A class that defines the entire simulation include driver, scenario, and samples.
from Env import env
from Simulation import Simulation


# The visual simulator as a ___________(JPanel)
class Simulator: # extends JPanel
    sim = Simulation()
    sim = None

    # Need to look further into setOpaque and background color
    def Simulator(self):
        super()
        setOpaque(True)
        setBackgroud(Color.black)
        setSize(Env.envwidth, Env.envHeight))

    def paintComponent(self, g = Graphics()):
        if(sim == None):
            return
        sim.draw(g)

    def useSimulation(self, simArg = Simulation()):
        sim = simArg

        