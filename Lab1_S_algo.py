import pandas as pd 
import numpy as np

# to read the data in the csv file
data=pd.read_csv("data.csv") 
print(data)

# making array of all the attributes
concepts=np.array(data)[:,:-1]
print("The attributes are:", d)

# segragating the target that has positive and negative examples
target=np.array(data)[:,-1]
print("The target is:", target)

# training function to implement find s-algorithm
def train(con,tar):
    for i,val in enumerate(tar):
        if val=="yes":
            specific_h=con[i].copy()
            break
            
    for i,val in enumerate(con):
        if tar[i]=="yes":
            for x in range(len(specific_h)):
                if val[x]!=specific_h[x]:
                    specific_h[x]='?'
                else:
                    pass
    return specific_h
    
 # obtaining the final hypothesis
 print(train(concepts,target))
