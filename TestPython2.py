import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn; seaborn.set_theme()

df = pd.read_csv(r"C:\Users\MSIi\Documents\Data engineer\numpy\seattleWeather_1948-2017.csv", parse_dates=[0])[['DATE', 'PRCP']]

rainfall = df[df['DATE'].dt.year == 2016]['PRCP'].values

#print("Shape:", rainfall.shape)

#plt.hist(rainfall, bins=30)
#plt.title('Rainfall')
#plt.xlabel('PRCP')
#plt.ylabel('Frequency')
#plt.show()

#------------------------------
#print(np.sum(rainfall==0))
#print('the number of days without rine ' ,np.sum(rainfall==0))
#---------------------------------
#the day with rain 
#print(rainfall!=0)
#print('the day with rain :',sum(rainfall!=0))
#---------------------------------------
#find the number of days with more than 0,5 inches
#print(rainfall>0,5)
#print("the number of days with more than 0,5 inches ", sum(rainfall>0.5))
#---------------------------------------------
#arr=np.array([[1,4,1],[1,1,6],[7,1,9]]).reshape(3,3)
#print(arr)
#print(arr[arr>5])
#----------------------------------------------
#ٍSummer days 
#arr=np.arange(366)
#print((arr>172)&(arr<172+90))
#------------------------------
more=rainfall[rainfall>0]
print('the mean ',more.mean())
