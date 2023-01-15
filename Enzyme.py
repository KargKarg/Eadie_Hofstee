import matplotlib.pyplot as plt
import numpy as np


class Enzyme:

    def __init__(self, Concentration_substrat,  Vi):
        self.substrat = Concentration_substrat
        self.vi = Vi


    @property
    def Vi_div_sub(self):
        vi_div = []
        for i in range(len(self.vi)):
            vi_div.append((self.vi[i]/self.substrat[i]))
        return vi_div

    @property
    def Km(self):
        return -((self.vi[-1] - self.vi[-2]) / (self.Vi_div_sub[-1] - self.Vi_div_sub[-2]))

    @property
    def Vmax(self):
        z = np.polyfit(self.Vi_div_sub, self.vi, 1)
        p = np.poly1d(z)
        return p(0)

    def graphe(self):
        plt.scatter(self.Vi_div_sub, self.vi, marker='+')
        z = np.polyfit(self.Vi_div_sub, self.vi, 1)
        p = np.poly1d(z)
        plt.plot(self.Vi_div_sub+[0], p(self.Vi_div_sub+[0]), 'm-')
        plt.xlim(left=0)
        plt.xlabel("Vi/[S]")
        plt.ylabel("Vi en µmol/L/min")
        plt.title("Représentation Eadie Hofstee de l'enzyme")
        plt.text(1, 1, f'Km : {self.Km} µmol\nVmax : {self.Vmax : .2f} µmol/L/min', horizontalalignment = 'center', verticalalignment = 'center')
        plt.savefig('Enzyme_Graphe.pdf', format='pdf')
        plt.show()
