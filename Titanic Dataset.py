import pandas as pd 

# Show all columns without truncation (...)


df=pd.read_csv(r'C:\Users\MSIi\Documents\Data engineer\DataCSV\Titanic-Dataset.csv')
#print(df.isnull().sum())
df['Age']=df['Age'].fillna(df['Age'].mean())
print(df.isnull().sum())
print(df['Cabin'])