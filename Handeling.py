'''
Each single line use to handle the data
before using in main.py
'''

# import main as mn
#
# # x = [11, 11, 2, 0, 2]
# x_predict = mn.pred_values_GUI(11, 11, 2, 0, 2)
# print(x_predict)
#
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from sklearn.metrics import mean_squared_error


data = pd.read_csv("student-mat.csv", sep =";")
# print(data)
# print(data.head)

data = data[["G1","G2","G3","studytime","failures","absences"]]

predict = "G3"

x = np.array(data.drop([predict],1))
y = np.array(data[predict])

xp = np.array(list(range(1, 11)))
rs = []
max_alpha_value = 0
for i in range(10):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1, random_state=i)
    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    MSR = mean_squared_error(linear.predict(x_test), y_test)
    rs.append(MSR)
    if acc > max_alpha_value:
        max_alpha_value = acc
        print("i is ",i,"acc : ",acc)
# print("max_alpha_value",max_alpha_value)
# print("rs",len(rs))
# prediction = linear.predict(x_test)

# print("xp",len(xp))
plt.plot(xp,rs, '*:r')
plt.title("The MSE in each iteration")
plt.xlabel("Iteration")
plt.ylabel("MSE value ")
plt.show()
# plt.plot(xp, y_test, label="Real Line")
# plt.plot(xp, prediction,label="Prediction Line")

# plt.legend()
# plt.show()