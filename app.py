from flask import Flask ,render_template,request,url_for
import pickle
import test as uday


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/input')
def input():
    return render_template('newcrop.html')

@app.route('/predict',methods=['POST'])
def predict():
    data1 = request.form.get('K')
    data2 = request.form.get('N')
    data3 = request.form.get('P')
    data4 = request.form.get('H')
    data5 = request.form.get('M')
    data6 = request.form.get('R')
    data7 = request.form.get('T')
    data1 = int(data1)
    data2 = int(data2)
    data3 = int(data3)
    data4 = int(data4)
    data5 = int(data5)
    data6 = int(data6)
    data7 = int(data7)
    data = uday.crop_model(data1,data2,data3,data4,data5,data6,data7)
    separator = ', '

    b = separator.join(data)
    
    return render_template('predict.html', predicted_crop=b)

if __name__ == "__main__":
    app.run(debug=True)
