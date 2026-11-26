import pandas as pd 
import numpy as np 

#data=pd.Series([1,2,3,4,5])
#data=data.values 
#print(type(data))
#-------------------------

#data=pd.Series([1,2,3,5,6,7])
#print(data[0:3])
#print(data)
#---------------------------------

# Aira = {
#     'Mahkkah':2000,
#     'jeddah':1000,
#     'Mokla':300,
#     'ciaro':2000
# } 

# Population={
# 'Mahkkah':1,
#     'jeddah':2,
#     'Mokla':3,
#     'ciaro':4,
#     'unknown':'atrr'
# }
# dicAira=pd.Series(Aira)
# dicPopulation=pd.Series(Population)

# datafrem = pd.DataFrame({
#     'population':Population,
#     'aira':Aira})

# print(datafrem)

#---------------------------------------

arr=np.arange(1,29).reshape(4,7)
arr=pd.DataFrame(arr,index=[11,22,33,44])
print(arr)