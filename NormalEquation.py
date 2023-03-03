'''
Normal Equation Theory
y = x0 + t1x1 + t2x2 .... etc
Theta = (x^.x)' X^.y      , {^} mean Transpose and {'} mean invers
then y be y_predect
so i dont wanna alpha or learning rate,
to see the simulation for result RUN 'NormalEquationGUI.py'
by.
Ali Hamoudeh - 1215263
'''

import pandas as pd
import numpy as np
import main as mn

data = pd.read_csv("student-mat.csv", sep =";")
# print(data)
# print(data.head)

data = data[["G1","G2","G3","studytime","failures","absences"]]

predict = "G3"

x = np.array(data.drop([predict], axis=1))  # 1 means drop colomn, 0 for row
y = np.array(data[predict])

# print(x.shape) ==> 135, 5

x1 = data['G1']
x2 = data['G2']
x3 = data['studytime']
x4 = data['failures']
x5 = data['absences']

# Average Calling Methould
def cal_avg(num):
    sum_sun = 0
    for t in num:
        sum_sun = sum_sun + t
    return sum_sun / len(num)

# Feature scaling
def Feature_Scaling(num):
    AVG_num = cal_avg(num)
    Max_num = max(num)
    Min_num = min(num)
    for i in range(len(num)):
        num[i] = (num[i]-AVG_num) / (Max_num - Min_num)
    return num

# adding bias to data
n = len(x1)
x_bais = np.ones((n,1))
x_new = np.append(x_bais, x, axis=1)

# making x^
x_new_transpose = np.transpose(x_new)

# (x^.x)
x_new_transpose_dot_x_new = x_new_transpose.dot(x_new)

# invers
the_invers = np.linalg.inv(x_new_transpose_dot_x_new)

#x^ . y
x_new_transpose_dot_y = x_new_transpose.dot(y)

# theta
theta = the_invers.dot(x_new_transpose_dot_y)

# theta = [ 0, 0.14637499, 0.98353126, -0.18637608, -0.43632021, 0.04585303]

theta_0 = theta[0]
theta_1 = theta[1]
theta_2 = theta[2]
theta_3 = theta[3]
theta_4 = theta[4]
theta_5 = theta[5]

#making a function to make the prediction
def pred_values(theta_0, theta_1, theta_2, theta_3, theta_4, theta_5, G1, G2, studytime, failures, absences):
    return theta_0 + theta_1 * G1 + theta_2 * G2 + theta_3 * studytime + theta_4 * failures + theta_5 * absences

# This function to use to GUI
def pred_values_GUI( G1, G2, studytime, failures, absences):
    theta_0 = theta[0]
    theta_1 = theta[1]
    theta_2 = theta[2]
    theta_3 = theta[3]
    theta_4 = theta[4]
    theta_5 = theta[5]
    return theta_0 + theta_1 * G1 + theta_2 * G2 + theta_3 * studytime + theta_4 * failures + theta_5 * absences

# Accuracy_score = (TP+TN)/(TP+TN+FP+FN)
def Accuracy_score(num_1,num_2):
    temp_reg = 0
    for i in range(len(num_1)):
        if int(num_1[i]) == int(num_2[i]):
            temp_reg = temp_reg + 1
            print("Temp Regester : ",temp_reg)
    return temp_reg / len((num_1))

y_pred_array = []

# print(len(x_new))
for x in range(len(x_new)):
    y_pred = pred_values(theta_0, theta_1, theta_2, theta_3, theta_4, theta_5, x1[x], x2[x], x3[x], x4[x], x5[x])
    y_pred_array.append(y_pred)
    print("The predected is ", int(y_pred), "The y is ", y[x])

y_pred_array = np.array(y_pred_array)

print("The accuracy is : ", Accuracy_score(y_pred_array,y))
# print(theta)
# print(mn.acc)