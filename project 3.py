import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

data = pd.read_csv('/Users/ghanishtrajoria/Downloads/householdtask3.csv')


print(data.head(10))

#scatter plot with year agaist own 
plt.scatter(data['year'], data[ 'own'])

#Adding title to the plot
plt. title("Scatter Plot")

#Setting the x and y Label
plt.xlabel('year')
plt. ylabel ('own' )
#Showing the result
plt.show()

#Line Chart with year against own 
plt. plot(data['year'])
plt.plot(data[ 'own'])

#Adding title to the plot
plt. title("Line Chart")

#Setting the x and y Label
plt. xlabel('year')
plt. ylabel('own')

#Showing the result 
plt.show()

#Bar chart or bar plot
plt. bar(data['year'], data[ 'own'])

#Adding title to the plot
plt. title("bar chart")

#Setting the x and y Label
plt.xlabel('year')
plt.ylabel( 'own')

#Showing the result
plt.show()

#Histogram
plt.hist(data[ 'income' ])
plt. title("Histogram")
plt. show()