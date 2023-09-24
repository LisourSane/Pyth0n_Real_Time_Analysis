# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plp
import random
import time
import scipy.stats as stats

cols = ["Stock_1", "Stock_2", "Stock_3", "Stock_4", "Strange Stock_5"]
#stock_data = pd.DataFrame([list([50, 50, 50, 50, 50])], columns=cols)
#print(stock_data)
#correlation matrix
A = np.array([[1, 0.8, 0.6, 0.3, 0], [0.8, 1, 0.4, 0.7, 0], [0.6, 0.4, 1, 0.2, 0], [0.3, 0.7, 0.2, 1, 0], [0, 0, 0, 0, 1]])
chol_A = np.linalg.cholesky(A)

#Function which simulates randomly changing stock in real time.
def print_random():
    stock_data = pd.read_csv("C:\\Users\\DANUSIA\\Desktop\\Projekty\\Python_Real_Time_Analysis\\stock_data.csv", usecols=cols)
    while True:
        second = stats.norm.rvs(0, 0.01, 5)
        stock_correlated = np.dot(chol_A, second) + np.array([0.001, 0.001, 0.001, 0.001, 0.001])
        stock_data.loc[len(stock_data)] = stock_correlated + stock_data.loc[len(stock_data)-1]
        #print(stock_data)
        #df = pd.DataFrame(stock_data)
        stock_data.to_csv('stock_data.csv', sep=',')
        time.sleep(1)
print_random()
#np.savetxt("stock_dat.cvs", stock_data, delimiter=",")
#df = pd.read_csv("C:\\Users\\DANUSIA\\Desktop\\Projekty\\Python_Real_Time_Analysis\\stock_data.csv")
#df = pd.read_csv("stock_dat.csv")
#print(df)
#np.array[0.001, 0.001, 0.001, 0.001, 0.001]+
# np.array(stock_data.loc[len(stock_data)-1])
