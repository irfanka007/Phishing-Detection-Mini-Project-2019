import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
from sklearn.metrics import precision_score

a=pd.read_csv("train_bill.csv")
a.dropna(axis=0, inplace=True)

b=pd.read_csv("test_bill1.csv")
b.dropna(axis=0, inplace=True)

x=a[['Variance','Skewness','Curtosis','Entropy']]
y=a[['Class']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)

clf=SVC()
clf.fit(x_train,y_train) #machine learn by fit-Training
y_pred=clf.predict(x_test)#predict the result

#print(y_pred)#predicted result
#print(y_test)#actual result

print("accuracy score is : ",accuracy_score(y_test, y_pred))
print("precision is",precision_score(y_test, y_pred, average='macro'))
#print(confusion_matrix(y_test, y_pred))
#print(classification_report(y_test, y_pred))

z=clf.predict(b)

print(z)#predict our actual test data


