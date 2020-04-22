from Simulation import Simulation

# Java file says 'class Driving extends actr.task.Task;
class Driving:
    # Need to find out how to declare these variables
    Simulator simulator = None
    JLabel nearLabel, carLabel, keypad    
    simulation = Simulation()

    def __init__(self):
        self.scale = 0.6
        self.steerFactor_dfa = (16 * self.scale)
        self.steerfactor_dna = (4 * self.scale)
        self.steerFactor_na  = (3 * self.scale)
        self.steerFactor_fa  = (0 * self.scale)
        self.accelFactor_thw  = (1 * .40)
        self.accelFactor_dthw = (3 * .40)
        self.steerNaMax = .07
        self.thwFollow = 1.0
        self.thwMax = 4.0

        self.startTime = 0
        self.endTime = 60
        self.accelBrake = 0
        self.speed = 0

        self.minX = 174
        self.maxX = (238+24)
        self.minY = 94
        self.maxY = (262+32)
        self.centerX = (self.minX + self.maxX)/2
        self.centerY = (self.minY + self.maxY)/2

    def Driving(self):
        super()
        nearLabel = JLabel(".")
        carLabel = JLabel("X")
        keypad = JLabel("*")

    def start(self):
        simulation = Simulation(getModel())

        if(getModel().getRealTime()):
            setLayout(BoderLayout())
            if(simulator == None):
                simulator = Simulator()
            add(simulator, BorderLayout.CENTER)
            simulator.useSimulation(simulation)
        else:
			add(nearLabel)
			nearLabel.setSize(20, 20)
			nearLabel.setLocation(250, 250)
			add(carLabel)
			carLabel.setSize(20, 20)
			carLabel.setLocation(250, 250)
			add(keypad)
			keypad.setSize(20, 20)
			keypadX = 250 + int(actr.model.Utilities.angle2pixels (10.0))
			keypad.setLocation(keypadX, 250)
