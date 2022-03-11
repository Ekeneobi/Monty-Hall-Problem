"""
Created on Sat Dec 12 14:01:10 2020
@author: Ekene Obi
Student Id: 31-03-030-20-2
Email: ekene.obi.2020@student.ism.de
"""

'''
Question 3.2 solution
'''

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# importing the dataset using pandas
# Load the dataset and describe it 
#(also show a covariance or correlation Matrix).
diamonds = pd.read_csv(r'C:/Users/diamonds.csv')

df = pd.DataFrame(diamonds,columns=['x','y','z']) # retrieve x,y,z values fro table

covMatrix = pd.DataFrame.cov(df)
print (covMatrix,"covarince matrix")


len(diamonds)       
diamonds.shape     
diamonds.info()  

#Create three new variables “carat_root” and “log_price”, “cut_num” giving
# the square root value of the “carat” variable, the natural logarithm of the 
#“price” variable and a numerical value for the “cut” variable
# (use the numbers 0,1,2,…) respectively.
diamonds["carat_root"] = diamonds["carat"].transform('sqrt')
diamonds["log_price"] = diamonds["price"].transform('log')
diamonds["cut_num"] = diamonds["cut"].replace({'Fair': 0, 'Good': 1, 'Very Good': 2, 'Ideal': 3, 'Premium': 4})

#Plot “carat_root” versus “log_price” in a scatter plot also by coloring the
# different cut labels. Show the names of the “cut” labels in the legend of 
#the plot.
mapscatter_fair = diamonds.query('cut_num == 0')
mapscatter_good = diamonds.query('cut_num == 1')
mapscatter_very_good = diamonds.query('cut_num == 2')
mapscatter_ideal = diamonds.query('cut_num == 3')
mapscatter_premium = diamonds.query('cut_num == 4')


plt.scatter(mapscatter_fair["carat_root"], mapscatter_fair["log_price"], c='purple', label='Fair',alpha=0.2)
plt.scatter(mapscatter_good["carat_root"], mapscatter_good["log_price"], c='yellow', label='Good',alpha=0.2)
plt.scatter(mapscatter_very_good["carat_root"], mapscatter_very_good["log_price"], c='green', label='Very Good',alpha=0.2)
plt.scatter(mapscatter_ideal["carat_root"], mapscatter_ideal["log_price"], c='red', label='Ideal',alpha=0.2)
plt.scatter(mapscatter_premium["carat_root"], mapscatter_premium["log_price"], c='blue', label='Premium',alpha=0.2)


#Define the independent variable (X) as “carat_root” and dependent
# variable (Y) as
#“log_price”.
plt.xlabel('carat_root')
plt.ylabel('log_price')

x = diamonds["carat_root"].values

x = x.reshape(-1, 1)

y = diamonds["log_price"].values

plt.title('Comparing carat_root (X) and log_price (Y) by also differentiating them by the cut type (cut_num)')

plt.show()

#Split your dataset into train and test data (use a 40% train/test ratio).

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.6)


#Use a linear model to explain the impact of X on Y.
#Use the test value of X to predict the test values of Y and compare the 
#predicted testvalues with the actual test values of Y by displaying both
# variables in a histogram.
lm = LinearRegression()

lm.fit(x_train, y_train) 

print(lm.intercept_)    # intercept
print(lm.coef_)         # slope
Y_test_pred = lm.predict(x_test)
                      
plt.hist(Y_test_pred, bins=50, label='predicted values', alpha=0.5)
plt.hist(y_test, bins=50, label='test values', alpha=0.5)
plt.xlabel('Values')
plt.ylabel('Frequenices')
plt.legend(loc='best')
plt.show()


#Use an adequate measure (e.g. R^2) to display the goodness of fit of the 
#underlying model.
lm.score(x_train, y_train)
lm.score(x_test, y_test)

X = diamonds[["carat_root", "cut_num"]].values

X_train, X_test, y_train2, y_test2 = train_test_split(X,y, test_size = 0.6)



lm.fit(X_train, y_train2)
print(lm.intercept_)
print(lm.coef_)


lm.score(X_train, y_train2)
lm.score(X_test, y_test2)

#Does the regression improve by adding “carat_num” as second independent 
#variable.
'''
Yes the regression improves by adding cara_num because it adds to the power
of the previous model
'''