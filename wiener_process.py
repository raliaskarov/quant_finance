#This python script runs 30 simulations of daily asset price during 1 year using Wiener process.

import numpy as np
import math
import matplotlib.pyplot as plt


class StochasticProcess:

    def __init__(self, drift, volatility, delta_t, initial_asset_price):
        self.drift = drift
        self.volatility = volatility
        self.delta_t = delta_t
        self.current_asset_price = initial_asset_price
        self.asset_prices = [initial_asset_price]
 
    def time_step(self):
        dW = np.random.normal(0, math.sqrt(self.delta_t))
        dS = self.drift * self.delta_t * self.current_asset_price + self.volatility * self.current_asset_price * dW
        self.asset_prices.append(self.current_asset_price + dS)
        self.current_asset_price = self.current_asset_price + dS


processes = []
for i in range (0,30):
    processes.append(StochasticProcess(.1, .2, 1/252, 100))


for process in processes:
    tenor = 1
    while ((tenor - process.delta_t) > 0):
            process.time_step()
            tenor = tenor - process.delta_t

#print(processes[0].asset_prices)

x = np.arange(0, len(processes[0].asset_prices))
y = processes[0].asset_prices

chart = plt.plot(x,y)
plt.show()
