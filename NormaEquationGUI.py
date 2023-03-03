import NormalEquation as neq
from tkinter import *
top = Tk()
top.title("Student Marks Prediction Project")
top.minsize(300,300)

G1_text = Label(text = "Enter The First Mark")
G1_text.pack()

G1_Entry = Entry()
G1_Entry.pack()

G2_text = Label(text = "Enter The Secound Mark ")
G2_text.pack()

G2_Entry = Entry()
G2_Entry.pack()

studytime_text = Label(text = "Enter Your Studey Time Mark")
studytime_text.pack()

studytime_Entry = Entry()
studytime_Entry.pack()

failures_text = Label(text = "Failures Time's ")
failures_text.pack()

failures_Entry = Entry()
failures_Entry.pack()

absences_text = Label(text = "Absences")
absences_text.pack()

absences_Entry = Entry()
absences_Entry.pack()

def predict():
    G1 = int(G1_Entry.get())
    G2 = int(G2_Entry.get())
    studytime = int(studytime_Entry.get())
    failures = int(failures_Entry.get())
    absences = int(absences_Entry.get())

    res = neq.pred_values_GUI(G1, G2, studytime, failures, absences)
    print("res is : ",res)
    resulLable = Label(text="The Prediction is : " + str(res))
    resulLable.pack()

but = Button(text = "Calculate the final prediction", command = predict)
but.pack()

top.mainloop()