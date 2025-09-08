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
                    value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], # Columns to melt (I will be referring to them as features from now on)
                    var_name = 'feature', # name of the new column that stores all the variables the were melted
                    value_name='value') # name of the new column that stores the values of each variable

    # Function melt() helps to mold the data into a more useful form, it reshapes data from a wide format to a long format

    # 6
    df_cat = df_cat.value_counts(['cardio', 'feature', 'value']).reset_index(name='total') # I'm counting how many times each combination of (cardio, feature, value) occurs when using the "value_counts()" and then adding a new column named "total" to receive this new data

   
    # 7
    catplot = sns.catplot(data=df_cat, #dataframe used to plot the chart
                            x='feature', # axis x
                            y='total',  # axis y
                            col='cardio', # title of the chart
                            kind='bar', # Type of chart
                            hue='value', # two bars will be created for each variable
                            hue_order=[0, 1]) # set a color to represent "0" and "1"

    # 8
    fig = catplot.fig

    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    df_heat = df[# I'm creating a new dataframe by filtering data of df based on the following criteria:       
        (df['ap_lo'] <= df['ap_hi']) &  # diastolic pressure is lower than systolic
        # Removing outliers of height and weight by using quantile (a method that returns the values that are in the interval you defined)
        
        (df['height'] >= df['height'].quantile(0.025)) & # 2,5% -> very close to the left tail of the distribution 
        (df['height'] <= df['height'].quantile(0.975)) & # 97,5 -> very close to the right tail of the distribuition

        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr() #correlation matrix

    # 13
    mask = np.triu(corr) # mask for the upper triangle

    # 14
    fig, ax = plt.subplots() # matplotlib figure

    # 15
    sns.heatmap(data=corr, #dataset to visualize (must be in a matrix form)

                annot=True, # displays the value in each cell
                fmt=".1f", # controls how numbers are shown: ".1f" means 1 decimal
                annot_kws={'fontsize':6}, # controls the font size of numbers

                linewidth=.5, # width of the lines that will divide each cell
                mask=mask, # hides the upper triangle
                square=False, # heatmap cells are not square-shaped and rectangular cells are allowed

                cbar_kws={"shrink": .7}, # arguments to customize the colorbar. In this case, it will look smaller compared to the heatmap.
                center=0, # set the value at which to center the colormap
                vmax=0.30); # data range that the colormap covers: it sets the maximum value of the color scale and any values ≥ 0.30 will have the same strongest color.

    # 16
    fig.savefig('heatmap.png')
    return fig
