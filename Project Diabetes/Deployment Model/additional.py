import pickle
import pandas as pd

from pandas import DataFrame, get_dummies

model = pickle.load(open('finalized_model2.sav', 'rb'))
one_hot_columns = pickle.load(open('x_dummies_column2.sav','rb'))

def additional_data(data):
    df = DataFrame(data,index=[0])
    df = get_dummies(df)
    df = df.reindex(columns=one_hot_columns, fill_value=0)
    hasil = model.predict_proba(df)

    x = []
    if hasil[0,1] < 0.3:
        x.append('You are in Low Risk Prediabetes/ Undiagnose Diabetes')
    elif hasil[0,1] < 0.6:
        x.append('You are in Moderate Risk Prediabetes/ Undiagnose Diabetes')
    else:
        x.append('You are in High Risk Prediabetes/ Undiagnose Diabetes')


    return x[0] + ' with probability ' + str(round(hasil[0,1],2) *100) + '%'  
    