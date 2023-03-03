import pandas as pd
import main as mn
import math
import numpy as np
import sklearn



TestingDAta = pd.read_csv("new-student-mat.csv", sep =";")

predict = "G3"

xt = np.array(TestingDAta.drop([predict],1))
yt = np.array(TestingDAta[predict])

x1 = TestingDAta['G1']
x2 = TestingDAta['G2']
x3 = TestingDAta['studytime']
x4 = TestingDAta['failures']
x5 = TestingDAta['absences']

P_NEW_VAL = []
for i in range(len(TestingDAta)):
    P_NEW_VAL.append(mn.pred_values_GUI(x1[i],x2[i],x3[i],x4[i],x5[i]))

# predict

# print("P_NEW_VAL")
# for ii in range(len(P_NEW_VAL)):
#     print(P_NEW_VAL[ii] , yt[ii])
#     if math.floor(P_NEW_VAL[ii]) == yt[ii]:
#         acc = acc + 1
#     if math.ceil(P_NEW_VAL[ii]) == yt[ii]:
#         acc = acc + 1

def compute_accuracy_tuple(y, y_pred):
    y = y.ravel()
    n_labels = len(np.unique(y))
    classes_probabilities = []
    accuracy_classes = []
    for cl in range(n_labels):
        idx = y == cl
        classes_probabilities += [np.mean(idx)]
        accuracy_classes += [
            np.mean((y[idx] == y_pred[idx])) if classes_probabilities[-1] else 0
        ]
        # This is also referred to as the "recall": p = n_true_positive / (n_false_negative + n_true_positive)
        # ( We could also compute the "precision": p = n_true_positive / (n_false_positive + n_true_positive) )
        accuracy_named_tuple = Accuracy(
            unweighted=np.dot(accuracy_classes, classes_probabilities),
            weighted=np.mean(accuracy_classes),
            worst=np.min(accuracy_classes),
            accuracy_classes=accuracy_classes,
        )
    return accuracy_named_tuple
# acc = sklearn.metrics.accuracy_score(P_NEW_VAL, yt)
print("acc is : ", compute_accuracy_tuple(P_NEW_VAL,yt))
