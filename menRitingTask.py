
import pandas as pd 
import numpy as np
df=pd.read_csv(r"C:\Users\MSIi\Documents\Data engineer\DataCSV\ramen-ratings.csv")                    # to import the data
#print(df.head(10))                                                                                   # to get the 5 elemnt ot head(10) to ten ..

#print(df['Country'])   #to get the coloumns 
#print(df.iloc[0,:])     # to get the Row by index or [0]
#print(df.iloc[:,0])
#print(df.iloc[0:3,:]) # to get slizing row
#print(df.iloc[:,-1])   # to get the last column 
#print(df.iloc[[1,3,15],:]) # to get deffrent rows 
#print(df.loc[:, ['Review #','Brand','Top Ten']])  # to get the row by name of columns 

#print(df.iloc[1:4])  # 3 rows 1,2,3
#print(df.loc[1:4]) # 4 rows 1,2,3,4


#print(df.set_index('Review #'))  # to set col like index 
#print(df.loc[df.Country=='Taiwan'])
#------------------------------------------------------------ Lesson 4 >> Conditional Selection & Assigning data <<
#print(df.loc[df.Stars>=2.5])                                                   # can't compare str with float 
#print (df.loc[df.Stars=='Unrated'])                                            # to get the data that has Unrated as str
#df=df.loc[df.Stars!='Unrated']                                                 # to delete from the data 
#print (df.loc[df.Stars.astype(float)>=2.5])                                    # to change the data type then compare float with float :-)
#----------------------------------------------------
# get all dishes in Taiwan that have a rating above average 2.5
#df=df.loc[df.Stars!='Unrated']                                                  # clean the data 
#print (df.loc[(df.Country=='Taiwan')& (df.Stars.astype(float)>2.5)])           # add the AND operation 
#---------------------------------------------------

# get only the brand and the style 
#print (df.loc[(df.Country=='Taiwan')& (df.Stars.astype(float)>2.5),['Brand','Style']])     # Rows vs columns 
# ------------------------------------------------------

# Have a look at the dishes served in both Finland and Sweden
#print(df[df.Country.isin(['Finland','Sweden'])])                                # isin()==> to get these values in this data 
#----------------------------------------------------------------

#
#print(df[~df['Top Ten'].isnull()])                                               # isnull() ==> to get the NULL values 
#df['Brand'] = 'Everyone'                                                         # to assign a value to the whole column 
#print(df)         

#------------------------------------
#df.loc[:, 'Review #'] = range(1, 2578)                                           # Tr. Ons's way by getting the number of rows manually 
#df.loc[:, 'Review #'] = range(1, len(df) + 1)                                     # (len(df)+1) ==> the same result without needing to calculate the rows 
#print(df)


#------------------------------------------------------------ Lesson 5 >> Handling Missing Values <<
#print(df.notnull())                        # notnull() => checks for non-missing (valid) values and returns True
#print(df.isnull().sum(axis=0))             # isnull() => checks for missing (NaN) values and returns True; sum(axis=0 for rows, 1 for columns) counts them
#print(df.shape)                            # returns the dimensions of the DataFrame (rows, columns)

#print(df.shape)                            # check shape before dropping missing values
#df = df.dropna()                           # drops all rows that contain any missing (NaN) value
#print(df.shape)                            # check shape after dropping missing values

#df = df.dropna(axis='columns')             # drops any column that contains at least one missing (NaN) value
#print(df)

#df.dropna(axis='columns', inplace=True)    # inplace=True saves the modification directly to 'df' in memory
# Best Practice: Always save modified versions separately before training a model, so you can revert changes without touching the original CSV data.

#df = df.dropna(subset=['Style'])           # subset=['Style'] => drops rows only if 'Style' has a missing (NaN) value

#df = df.fillna(0)                          # fills all missing (NaN) values in the DataFrame with 0

#df = df.loc[df['Style'].isnull()]          # filters and returns only the rows where 'Style' is missing (NaN)

#df = df.fillna({'Top Ten': -1, 'Style': 'Not available'})  # fills missing values with specific custom values per column

#df.bfill()                                 # Backward Fill (bfill): fills missing values using the NEXT (lower) value
#df.ffill()                                 # Forward Fill (ffill): fills missing values using the PREVIOUS (upper) value

#print(df['Stars'].value_counts())          # value_counts() => counts unique values as objects (e.g., string '5' != '5.00'); avoid overwriting 'df' here

#df['Stars'] = df['Stars'].replace('Unrated', np.nan)   # replaces the string 'Unrated' with a proper NaN missing value
#print(df['Stars'].value_counts())

import pandas as pd

# ------------------------------------------------------------ Sample DataFrames for Practice

# 1. DataFrames for pd.merge() and .join() (with overlapping column 'name' and different key names)
left = pd.DataFrame({
    'key_left': [1, 2, 3, 4],
    'name': ['Ramen', 'Noodles', 'Soup', 'Pasta'],
    'price': [10, 15, 12, 20]
})

right = pd.DataFrame({
    'key_right': [2, 3, 4, 5],
    'name': ['Chicken', 'Beef', 'Seafood', 'Spicy'],   # Overlapping column name ('name') to test suffixes
    'stock': [50, 30, 0, 100]
})

# 2. DataFrames for pd.concat() (same columns for vertical stacking)
df1 = pd.DataFrame({
    'brand': ['Nissin', 'Samyang'],
    'stars': [4.5, 5.0]
})

df2 = pd.DataFrame({
    'brand': ['Indomie', 'Maruchan'],
    'stars': [4.8, 3.75]
})

# ------------------------------------------------------------ Quick Test Examples
print(left , right)
# Test 1: Merge with different key names & custom suffixes
print("--- 1. Merge (left_on / right_on + suffixes) ---")
print(pd.merge(left, right, how='inner', left_on='key_left', right_on='key_right', suffixes=('_from_left', '_from_right')).drop(columns=['key_right']))


# Test 2: Join based on Index
print("\n--- 2. Join (on Index with lsuffix / rsuffix) ---")
print(left.join(right, how='outer', lsuffix='_from_left', rsuffix='_from_right'))

