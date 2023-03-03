'''
This code is a GD {random_state = 134067} to predict the student performance
for Advance Machine Learning course at BZU
to see the simulation for result RUN 'mainGUI.py'
by.
Ali Hamoudeh - 1215263
'''
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


x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x,y, test_size=0.1 , random_state=139067)
# clf = DecisionTreeClassifier(random_state=139067)
# path = clf.cost_complexity_pruning_path(x_train, y_train)
# ccp_alphas, impurities = path.ccp_alphas, path.impurities
# fig, ax = plt.subplots()
# ax.plot(ccp_alphas[:-1], impurities[:-1], marker="o", drawstyle="steps-post")
# ax.set_xlabel("effective alpha")
# ax.set_ylabel("total impurity of leaves")
# ax.set_title("Total Impurity vs effective alpha for training set")
# plt.show()
linear = linear_model.LinearRegression()

linear.fit(x_train,y_train)

acc = linear.score(x_test, y_test)

print("Tha accuracy is :",acc)
# print("ccp_alpha, ",linear._)
print("co:",linear.coef_)
print("intersept:",linear.intercept_)
# print("intersept:",linear.)

prediction = linear.predict(x_test)

# # mymodel = np.poly1d(np.polyfit(prediction, y_test, 3))
# # myline = np.linspace(0, 20, 395)
# xp = np.array(list(range(1, 41)))
# # print(len(xp),";",len(prediction))
# plt.plot(xp, y_test, label="Real Line")
# plt.plot(xp, prediction,label="Prediction Line")
# plt.title("Prediction")
# plt.xlabel("N")
# plt.ylabel("G3")
# plt.legend()
# plt.show()

x1 = data['G1']
x2 = data['G2']
x3 = data['studytime']
x4 = data['failures']
x5 = data['absences']

# plt.plot(y, x5)
# plt.plot(xp, y,label="2 Line")
# plt.title("Prediction")
# plt.xlabel("N")
# plt.ylabel("G3")
# plt.legend()
# plt.show()

print("The MSE is :",mean_squared_error(prediction, y_test))

for x in range(len(prediction)):
    print(prediction[x], x_test[x], y_test[x])

# for x in range(len(prediction)):
#     print(prediction[x])

# This function to use to GUI
def pred_values_GUI( G1, G2, studytime, failures, absences):
    theta_0 = linear.coef_[0]
    theta_1 = linear.coef_[1]
    theta_2 = linear.coef_[2]
    theta_3 = linear.coef_[3]
    theta_4 = linear.coef_[4]
    # theta_5 = theta[5]/
    return theta_0 * G1 + theta_1 * G2 + theta_2 * studytime + theta_3 * failures + theta_4 * absences


