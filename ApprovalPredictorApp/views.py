from django.http import HttpResponse
from django.shortcuts import render
import joblib
import sklearn
import xgboost
import pandas as pd

def index(request):
    return render(request,"index.html")

def result(request):
    classifier=joblib.load("model.sav")
    input=[]
    input.append(int(request.GET["age"]))
    input.append(int(request.GET["debt"])//1000)
    input.append(int(request.GET["bankCustomer"]))
    input.append(int(request.GET["yearsEmployed"]))
    input.append(int(request.GET["priorDefault"]))
    input.append(int(request.GET["employed"]))
    input.append(int(request.GET["creditScore"]))
    input.append(int(request.GET["driversLicense"]))
    input.append(int(request.GET["citizen"]))
    input.append(int(request.GET["income"]))
    res=classifier.predict(pd.DataFrame([input],columns=['Age', 'Debt', 'BankCustomer', 'YearsEmployed', 'PriorDefault',
       'Employed', 'CreditScore', 'DriversLicense', 'Citizen', 'Income']))
    if(res==1):
        res="The chances of your credit card application getting approved are high"
    else:
        res="The chances of your credit card application getting approved are low improve your credit score and apply again "



    return render(request,"result.html",{"res":res})

