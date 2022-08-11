import numpy as np

k = 1.380649E-23

class thermoSystem:

    def __init__(self, particles, energy, bounds):

        self.n = particles
        self.q = energy
        self.mass = 4.65E-26       #mass of N2 molecule
        self.multiplicity = (np.e*self.q/self.n)**self.n
        self.entropy = k*np.log(self.multiplicity)
        self.bounds = bounds

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

    def impulse(self):
        pass