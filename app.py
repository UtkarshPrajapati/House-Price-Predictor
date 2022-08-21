from flask import Flask,render_template,request
from flask_cors import CORS, cross_origin
import pandas as pd
import pickle
app=Flask(__name__)
cors=CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
data=pd.read_csv("Clean_Data_Price.csv")
pipe=pickle.load(open("RidgeModel.pkl","rb"))
@app.route('/')
@cross_origin()
def index():

    locations=sorted(data["location"].unique())
    return render_template("index.html",locations=locations)

@app.route("/predict",methods=["POST"])
@cross_origin()
def predict():
    locations=request.form.get("location")
    bhk=request.form.get("bhk")
    bath=request.form.get("bath")
    sqft=request.form.get("sqft")
    print(locations,bhk,bath,sqft)
    input=pd.DataFrame([[locations,sqft,bath,bhk]],columns=["location","total_sqft","bath","bhk"])
    prediction=pipe.predict(input)[0]*1e5
    if prediction>0:
        return str(round(prediction,2))
    else:
        return -1
if __name__=="__main__":
    app.run()