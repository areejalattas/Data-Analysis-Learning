import numpy as np
#import pandas as pd


#df = pd.read_csv(r"C:\Users\MSIi\Documents\Data engineer\numpy\500_Person_Gender_Height_Weight_Index.csv")



#data = df.iloc[:, -3:].values
#print(data)


#print('the sahpe', data.shape)
#print('the size ',data.size)
#print('the dimntion ', data.ndim )
#print('the data type ',data.dtype)
#print(data[::3,:])
#print(data.h)

#clm1=data[:,0]
#clm2=data[:,-1]
#print (1)
#print(2)

#print((np.hstack((clm1.reshape(500,1),clm2.reshape(500,1)))))
#print('the mine array : ')
#print(data.all)
#print('the array after reverse the rows : ')
#print(data[::-1])
#hights= data [:,0]

#print('the array og hights : ')
#print(hights.max())
#----------------------------------------------
#print('the wights : ')
#wights =data[:,1]
#print (wights)
#print('the max wights is ',wights.max()," the min wights ",wights.min())
#-------------------------------------------------------
#hights= data [:,0]

#sumofallhights =hights.sum()
#meanhights=sumofallhights//500 
#print("the mean ", meanhights)
#print(np.mean(hights))
#------------------------------------------------------------
#means=np.mean(hights )
#print(means)
#s=np.std(hights)
#print(s)
#---------------------------------------------
#extract every three observation 
#print(data[::3,:])
#------------------------------------------
# extract first and last features 
#featuresfirstRow =data[::,0] 
#featuresSecendtRow=data[::,-1]
#print(featuresfirstRow)
#print(featuresSecendtRow)
#allfeatures=np.hstack([featuresfirstRow.reshape(-1,1),featuresSecendtRow.reshape(-1,1)])
#print (allfeatures)
#-------------------------------------
#ٌReverse the array 
#print(data[::-1])
#---------------------------------------
#hights = data[::,0]
#maxHights=hights.max()
#minHights=hights.min()

#print(maxHights)
#print(minHights)
#-------------------------------------------
#weights=data[::,1]
#maxx=weights.max()
#minn=weights.min()
#print(maxx)
#print(minn)
#--------------------------------------------
#percentile
#hights = data[::,0]
#P=np.percentile(hights,[25,50,75])
#print(P)
#---------------------------------------------------
#find the percentile and the midian for the wights 
#wights=data[::,1]
#print(wights)
#P=np.percentile(wights,[25,50,75])
#print(P)
#---------------------------------------------------
#find the Normalization
#hights=data[::,0]
#means=np.mean(hights)
#stdd=np.std(hights)
#normaliztion=(hights-means)/stdd
#print(normaliztion)
#---------------------------------
#array=np.arange(1,13) # 10-1 =9 elements 
#array=array.reshape((2,6))
#print(array)
#array=np.arange(0,12).reshape((3,2,2))
#print(array)
#print(array.ndim)
b = np.arange(3)[np.newaxis, np.newaxis, :]
print(b.shape)  

b = np.arange(3)[:, np.newaxis, np.newaxis]
print(b.shape)  

b = np.arange(3)[np.newaxis, :, np.newaxis]
print(b.shape)  