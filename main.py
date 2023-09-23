# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plp
import random
import time
import scipy.stats as stats
stock_data = np.array([])
print(stock_data)
#Function which simulates randomly changing stock in real time.
def print_random():
    stock_data = np.array([50])
    while True:
        second = stats.norm.rvs(0, 0.01)
        stock_data = np.append(stock_data, second)
        print(np.cumsum(stock_data))
        #df = pd.DataFrame(stock_data)
        np.savetxt("stock_data.csv", np.cumsum(stock_data), delimiter=",")
        time.sleep(1)
print_random()
#np.savetxt("stock_dat.cvs", stock_data, delimiter=",")
#df = pd.read_csv("C:\\Users\\DANUSIA\\Desktop\\Projekty\\Python_Real_Time_Analysis\\stock_data.csv")
#df = pd.read_csv("stock_dat.csv")
#print(df)

