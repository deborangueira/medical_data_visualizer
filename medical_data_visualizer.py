import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2

overweight_list = [] # Create an empty List that will receive all the binary values related to overweight

bmi = df['weight']/((df['height']/100)**2) # calculus of ibm and adjustment of unit of measure for height

for i in bmi: # Since ibm returns a list with index and value, now I do an iteration to classify each bmi in 0 or 1 based on the criteria defined in the question and add this information in the overweight_list 
    if i > 25:
        overweight_list.append(1) #1 for overweight
    else:
        overweight_list.append(0) #0 for not overweight

df['overweight'] = overweight_list # finally, I add a new column by: declaring a new column name with the binary list: overweight_list

# 3

df['cholesterol'] = df['cholesterol'].apply(lambda x:0 if x ==1 else 1)
df['gluc'] = df['gluc'].apply(lambda x:0 if x ==1 else 1)

# Beforehand I duble-checked the datatype of those two columns using "print(df.dtypes)", and saw that they were intergers. 
# Then in the argument (left side, before the =) I defined the column that will be overwritten
# In the expression (right side, after the =), I defined the column that has the values that interest me, then I used apply() which allows me to pass a function (in this case lambda) and run it to every single cell


# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt(id_vars=['cardio'], # Columns to keep 
                    value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], # Columns to melt
                    var_name = 'health factor', # name of the new column that stores all the variables the were melted
                    value_name='value') # name of the new column that stores the values

    # Function melt() helps to mold the data into a more useful form, it reshapes data from a wide format to a long format

    print(df_cat)

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
