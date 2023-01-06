import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np


##### 
##### Load .csv sheets into pandas DataFrames
#####

#change directory where data is
os.chdir('C:/Users/Admin/Coding/tradesheet')

#load summary to begin list of trees
summary = pd.read_csv('summary.csv')

# load all trees
file_list = ['Tree_1', 'Tree_2', 'Tree_3', 'Tree_4', 'Tree_5', 'Tree_6', 'Tree_7', 'Tree_8', 'Tree_9', 'Tree_10']
tree = [summary]

for i in range(len(file_list)):
    temp = pd.read_csv(file_list[i]+'.csv', skiprows = 3, names = ['Entry_Date', 'L/S', 'Qty', 'Description', 'Filled_Qty', 'Entry', 'Entry_Value', 'Exit_Date', 'Exit', 'At_Risk', 'Exit_Value', 'Profit/Loss', '%_Return', 'Total'])
    temp = temp.reset_index(drop=True)
    tree.append(temp)
    

#####
##### Plots 
#####

### Matplotlib.pyplot
# select data
x = tree[9]['Entry_Date']
y = tree[9]['Total']

# create plot
fig, ax = plt.subplots()
ax.plot(x, y, linewidth = 3)
ax.set(xlabel = 'Date', ylabel = 'Total ($USD)', title = 'Tree 9')
plt.show()



### Seaborn
df = tree[9]

sns.lineplot(data = df, x = 'Entry_Date', y = 'Total');






