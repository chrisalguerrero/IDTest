# Import all libraries needed for the tutorial
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

dataframe = pd.read_csv('ID_Test_plot2.txt', sep = "\s+", names=['Time (sec)', 'Upstream Mtr Actual (cts)', 'Upstream Mtr Cmd (cts)', 'Downstream Mtr Actual (cts)', 'Downstream Mtr Cmd (cts)', 'Upstream Mtr Fol Error', 'Downstream Mtr Fol Error'], skiprows=1 )

fig, ax = plt.subplots()
ax2 = ax.twinx()
plot = dataframe.plot(x='Time (sec)', y=['Upstream Mtr Actual (cts)', 'Upstream Mtr Cmd (cts)', 'Downstream Mtr Actual (cts)', 'Downstream Mtr Cmd (cts)'], ax=ax,figsize=(15, 10))
plot = dataframe.plot(x='Time (sec)', y=['Upstream Mtr Fol Error', 'Downstream Mtr Fol Error'], ax=ax2)

plt.savefig('plot.png')
