from tkinter import Label, Tk, Entry, Button, mainloop

import joblib
import pandas as pd


def show_entry():
    p1 = float(e1.get())
    p2 = float(e2.get())
    p3 = float(e3.get())
    p4 = float(e4.get())
    p5 = float(e5.get())
    p6 = float(e6.get())
    p7 = float(e7.get())
    p8 = float(e8.get())
    p9 = float(e9.get())
    p10 = float(e10.get())
    p11 = float(e11.get())

    model = joblib.load('/home/anvndev/Documents/HUTECH/DACN/reloans-prediction-dacn/models/LoansRP_DACN.h5')
    df = pd.DataFrame({
        'Gender': p1,
        'Married': p2,
        'Dependents': p3,
        'Education': p4,
        'Self_Employed': p5,
        'ApplicantIncome': p6,
        'CoapplicantIncome': p7,
        'LoanAmount': p8,
        'Loan_Amount_Term': p9,
        'Credit_History': p10,
        'Property_Area': p11
    }, index=[0])
    result = model.predict(df)

    if result == 1:
        Label(master, text="Loan approved").grid(row=31)
    else:
        Label(master, text="Loan Not Approved").grid(row=31)


master = Tk()
master.title("Loan Status Prediction Using Machine Learning")
Label(master, text="Loan Status Prediction", bg="black",
      fg="white").grid(row=0, columnspan=2)

Label(master, text="Gender [1:Male ,0:Female]").grid(row=1)
Label(master, text="Married [1:Yes,0:No]").grid(row=2)
Label(master, text="Dependents [1,2,3,4]").grid(row=3)
Label(master, text="Education").grid(row=4)
Label(master, text="Self_Employed").grid(row=5)
Label(master, text="ApplicantIncome").grid(row=6)
Label(master, text="CoapplicantIncome").grid(row=7)
Label(master, text="LoanAmount").grid(row=8)
Label(master, text="Loan_Amount_Term").grid(row=9)
Label(master, text="Credit_History").grid(row=10)
Label(master, text="Property_Area").grid(row=11)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)
e8 = Entry(master)
e9 = Entry(master)
e10 = Entry(master)
e11 = Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=6, column=1)
e7.grid(row=7, column=1)
e8.grid(row=8, column=1)
e9.grid(row=9, column=1)
e10.grid(row=10, column=1)
e11.grid(row=11, column=1)

Button(master, text="Predict", command=show_entry).grid()

mainloop()
