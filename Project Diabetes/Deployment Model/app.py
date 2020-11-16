from flask import Flask, render_template, request
from cleaning_data import data_case
from prediction import prediction_data
from additional import additional_data
from plots import bar1,bar2,bar3,bar4

## Initialize
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index_prediction():
    if request.method == "POST":
        data = request.form ## immutablemultidict
        data = data.to_dict()
        data['systolic'] = int(data['systolic'])
        data['bmi'] = float(data['bmi'])
        data['arm_circumference'] = float(data['arm_circumference'])
        data['WH_ratio'] = float(data['WH_ratio'])
        #hasil = data.to_dict()
        hasil = prediction_data(data)
        return render_template('result.html', hasil_prediction=hasil)
        #return render_template('result.html', hasil_prediction=data)
    return render_template('prediction.html', )

@app.route('/additional', methods=['GET','POST'])
def index_additional():
    if request.method == "POST":
        data2 = request.form ## immutablemultidict
        data2 = data2.to_dict()
        data2['systolic'] = int(data2['systolic'])
        data2['bmi'] = float(data2['bmi'])
        data2['WH_ratio'] = float(data2['WH_ratio'])
        data2['glucose_mg/dL'] = int(data2['glucose_mg/dL'])
        #hasil = data.to_dict()
        hasil = additional_data(data2)
        return render_template('result_add.html', hasil_additional=hasil)
        #return render_template('result.html', hasil_prediction=data)
    return render_template('additional.html', )

@app.route('/about')
def about():
    data3 = bar1()
    data4 = bar2()
    data5 = bar3()
    data6 = bar4()
    return render_template('about.html',data3=data3,data4=data4,data5=data5,data6=data6)
#    return render_template('about.html',)

if __name__ == '__main__':
    app.run(debug=True, port=3333)