import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2

overweight_list = [] # Create an empty List that will receive all the values related to overweight

bmi = df['weight']/((df['height']/100)**2) # calculus of ibm and adjustment of unit of measure for height

for i in bmi: # Since ibm returns a list with index and value, now I do an iteration to classify each bmi in 0 or 1 based on the criteria defined in the question and add this information in the overweight_list 
    if i > 25:
        overweight_list.append(1) #1 for overweight
    else:
        overweight_list.append(0) #0 for not overweight

df['overweight'] = overweight_list # finally, I add a new column by: declaring a new column name with the binary list: overweight_list

# 3


# 4
def draw_cat_plot():
    # 5
    df_cat = None


    # 6
    df_cat = None
    

    # 7



    # 8
    fig = None


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
