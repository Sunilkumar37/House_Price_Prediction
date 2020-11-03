from flask import Flask, request, render_template
import joblib
import numpy as np 

app = Flask(__name__)
model = joblib.load("modelHPP.pkl")

@app.route("/")
def hello():
    return render_template("indexHPP.html")

@app.route('/predict',methods = ['POST'])
def result():
    if request.method == 'POST':
        SQUARE_FT = request.form["SQUARE_FT"]
        SQUARE_FT = int(SQUARE_FT)
        print(SQUARE_FT)
        BHK_NO = request.form["BHK_NO."]
        BHK_NO = int(BHK_NO)
        print(BHK_NO)
        LONGITUDE = request.form["LONGITUDE"]
        LONGITUDE = float(LONGITUDE)
        print(LONGITUDE)
        LATITUDE = request.form["LATITUDE"]
        LATITUDE = float(LATITUDE)
        print(LATITUDE)
        list1 = [[SQUARE_FT,BHK_NO,LONGITUDE,LATITUDE]]
        print(list1)
        price = np.abs(model.predict(list1))

    return render_template('indexHPP.html',
                        prediction_text = "Price in Lakhs = {}".format(price))

if __name__ == "__main__":
    app.run()