import numpy as np

k = 1.380649E-23
h = 6.62607015E-34
avogadro = 6.02214076E23
conversion = 2.4025E32     #from units to picometers to meters to meters squared given rN2 = 155pm

class thermoSystem:

    def __init__(self, particles, energy, bounds):

        self.n = particles
        self.q = energy
        self.mass = 4.65E-26       #mass of N2 molecule in kg
        self.bounds = bounds
        self.volume = (self.bounds[2]-self.bounds[0]) * (self.bounds[3]-self.bounds[1])
        self.volume0 = (bounds[2]-bounds[0]) * (bounds[3]-bounds[1])

        self.entropy = k*self.n*avogadro * (np.log(self.volume/(self.n*avogadro) * (4*np.pi*self.mass*self.q/3/self.n/h**2)**1.5) + (2.5))
        self.entropy0 = k*self.n*avogadro * (np.log(self.volume0/(self.n*avogadro) * (4*np.pi*self.mass*self.q/3/self.n/h**2)**1.5) + (2.5))
        
        self.positions = np.zeros((self.n, 2))
        for i in range(self.n):
            self.positions[i] = [np.random.randint(self.bounds[0], self.bounds[2]), np.random.randint(self.bounds[1], self.bounds[3])]

        self.directions = np.zeros(self.n)
        for i in range(self.n):
            self.directions[i] = np.random.rand()*2*np.pi
        
        self.energies = np.zeros(self.n)
        for i in range(self.n):
            self.energies[i] = self.q/self.n


    def evolve(self, dt):
        for i in range(self.n):
            stepx = np.sqrt(self.energies[i]/self.mass)*dt * np.cos(self.directions[i])
            stepy = np.sqrt(self.energies[i]/self.mass)*dt * np.sin(self.directions[i])
            self.positions[i] = self.positions[i][0] + stepx, self.positions[i][1] + stepy
            
            if self.positions[i][0] < self.bounds[0] or self.positions[i][0] > self.bounds[2]:
                self.directions[i] = np.pi - self.directions[i]
            elif self.positions[i][1] < self.bounds[1] or self.positions[i][1] > self.bounds[3]:
                self.directions[i] = 2*np.pi - self.directions[i]

    def get_positions(self):
        return self.positions

    def get_entropy(self):
        return self.entropy,  self.entropy0

    def get_volume(self):
        return self.volume

    def get_n(self):
        return self.n

    def set_state(self):
        self.volume = (self.bounds[2]-self.bounds[0]) * (self.bounds[3]-self.bounds[1])
        self.entropy = k*self.n*avogadro * (np.log(self.volume/(self.n*avogadro) * (4*np.pi*self.mass*self.q/3/self.n/h**2)**1.5) + (2.5))

    def impulse(self, input):
        
        wallmove = 25
        if input == 2:
            self.bounds[3] += wallmove
        elif input == 3:
            self.bounds[1] -= wallmove
        elif input == 4:
            self.bounds[2] += wallmove
        elif input == 5:
            self.bounds[0] -= wallmove

        self.set_state()
