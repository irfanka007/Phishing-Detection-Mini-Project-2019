import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
from sklearn.metrics import precision_score


a=pd.read_csv("train_bill.csv")
a.dropna(axis=0, inplace=True)

b=pd.read_csv("test_bill1.csv")
b.dropna(axis=0, inplace=True)

print(b)

x=a[['Variance','Skewness','Curtosis','Entropy']]
y=a[['Class']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)

clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(x_train,y_train)

pred=clf.predict(b)
print(b)
print(pred)



#Predict the response for test dataset
y_pred = clf.predict(x_test)
#print(y_pred)
print("\n")
print("Accuracy : ",accuracy_score(y_test, y_pred))
print("precision is",precision_score(y_test, y_pred, average='macro'))





