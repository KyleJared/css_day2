# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:42:58 2024

@author: Jared
"""

import pandas as pd

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= column_names)

df2 = pd.read_json("student_data.json")

"""
Right click on file to copy file path:
    C:/Users/Jared/CSS_Day2/country_data_index.csv
    country_data_index.csv
"""

#To specify an index column
df3 = pd.read_csv("data_02/country_data_index.csv")
df3 = pd.read_csv("data_02/country_data_index.csv",index_col=0)

#To skip some empty rows
#df4 = pd.read_csv("data_01/insurance_data.csv")
df4 = pd.read_csv("data_02/insurance_data.csv",skiprows=5)

#Specify the delimiter if it is not a comma
#df5 = pd.read_csv("data_02/Geospatial Data.txt")
df5 = pd.read_csv("data_02/Geospatial Data.txt",sep=";")

#A file which has inconsistant names and types
df6 = pd.read_excel("data_02/residentdoctors.xlsx")
#print(df6.info())
# Step 1: Extract the lower end of the age range (digits only)
# Read a number (the lower limit) and stop at the -
df6['LOWER_AGE'] = df6['AGEDIST'].str.extract('(\d+)-')
df6['UPPER_AGE'] = df6['AGEDIST'].str.extract('-(\d+)')
# Specify new column data type as a float
df6['LOWER_AGE'] = df6['LOWER_AGE'].astype(int)
# Trying to convert 'other' status to some int value. It was not successful in this code (yet...)
#df6['MARITALSTATUS'] = df6['MARITALSTATUS'].astype(int)

"""
Working with dates
"""

df7 = pd.read_csv("data_02/time_series_data.csv",index_col=0)
#df7.info()
#Variable explorer is handy
# Convert the 'Date' column to datetime
df7['Date'] = pd.to_datetime(df7['Date'], format='%Y-%m-%d')
#df7.info()
# Split the 'Date' column into separate columns for year, month, and day
df7['Year'] = df7['Date'].dt.year
df7['Month'] = df7['Date'].dt.month
df7['Day'] = df7['Date'].dt.day

"""
NaN's and wrong formats
"""

df8 = pd.read_csv("data_02/patient_data_dates.csv")
# Allows you to see all rows
pd.set_option('display.max_rows',None)
#df8.info()

#Removing certain columns, in this case an index column
df8.drop(['Index'],inplace=True,axis=1)

# Filling empty spaces in calories column: use .fillna()
#Replaces empty values with an average
x8 = df8["Calories"].mean()
df8["Calories"].fillna(x8, inplace = True)
#df8.info()

df8.drop(index = 26, inplace=True)
df8.drop(index = 22, inplace=True)
#print(df8["Date"])
df8["Date"] = pd.to_datetime(df8['Date'])
df8.loc[7, 'Duration'] = 45
df8.drop_duplicates(inplace = True)
df8 = df8.reset_index(drop=True)

"""
Regular expressions:
    Look this up
    \d - digit
    + - ? positive, multiple numbers
    - - stop here
"""

"""
RSE - Research Software Engineer
- Have some research background/understanding
- Work to advance research
- Potential of tenure

Keynote: Research software engineers and academia

Can help with:
    1) Review of code prior to publication
    2) Help with poor quality code, which is difficult to understand or maintain
    3) Help with lack of coding skills
    
Advantages:
    1) www.software.ac.uk
    
Look at RSE@SUN (rse.sun.ac.za)

kcmartin@sun.ac.za
rsse.africa/ community free to join
society-rse.org slack
"""

"""
Applying data transformations
"""

#print(df)

col_names = df.columns.to_list()

#print(col_names)

df['sepal_length_sq'] = df['sepal_length']*df['sepal_length'] #df["sepal_length_sq"] = df["sepal_length"].apply(lambda x: x**2)
#print(df['sepal_length_sq'])

grouped = df.groupby("class")

# Calculate mean, sum, and count for the squared values

mean_squared_values = grouped['sepal_length_sq'].mean()
sum_squared_values = grouped['sepal_length_sq'].sum()
count_squared_values = grouped['sepal_length_sq'].count()

# Display the results
#print("Mean of Sepal Length Squared:")
#print(mean_squared_values)

#print("\nSum of Sepal Length Squared:")
#print(sum_squared_values)

#print("\nCount of Sepal Length Squared:")
#print(count_squared_values)

"""
Append and merge
"""

# Read the CSV files into dataframes
df9_1 = pd.read_csv("data_02/person_split1.csv")
df9_2 = pd.read_csv("data_02/person_split2.csv")

# Concatenate the dataframes
df9 = pd.concat([df9_1, df9_2], ignore_index=True)

df10_1 = pd.read_csv('data_02/person_education.csv')
df10_2 = pd.read_csv('data_02/person_work.csv')

## inner join
df_merge = pd.merge(df10_1,df10_2,on='id', how="inner")

"""
Filtering 
"""

# Filtering data
print(df3[df3['Age'] > 30])
print(df[df['sepal_length'] > 5])

# Filter data for females (class == 'Iris-versicolor')
iris_versicolor = df[df['class'] == 'Iris-versicolor']

# Calculate the average iris_versicolor_sep_length
avg_iris_versicolor_sep_length = iris_versicolor['sepal_length'].mean()
print(avg_iris_versicolor_sep_length)
df['class'] = df['class'].str.replace('Iris-', '')
iris_virginica = df[df['class'] == 'virginica']
print(iris_virginica)

"""
Load
"""

df.to_csv("Iris_data_virginica_mt_5_sepal_length.csv")





