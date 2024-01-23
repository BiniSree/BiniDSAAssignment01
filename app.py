from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/prediction', methods = ['GET','POST'])
def species():
    if request.method == 'POST':
        SL = request.form['SL']
        SW = request.form['SW']
        PL = request.form['PL']
        PW = request.form['PW']
        model = pickle.load(open('iris_model.pkl','rb'))
        Species = model.predict([[float(SL),float(SW),float(PL),float(PW)]])

        return render_template('prediction.html', Species=Species)

if __name__ == '__main__':
    app.run()


