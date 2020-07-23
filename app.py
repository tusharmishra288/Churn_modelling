from flask import Flask, render_template, request
import jsonify
import numpy as np
import joblib
app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
        to_predict_list = request.form.to_dict() 
        to_predict_list = list(to_predict_list.values()) 
        to_predict_list = list(map(float, to_predict_list)) 
        to_predict = np.array(to_predict_list).reshape(1, 17) 
        model = joblib.load('project_f') 
        prediction = model.predict(to_predict) 
        if prediction==1:
            return render_template('index.html',prediction_text="Customer's Balance will be churned")
        else:
            return render_template('index.html',prediction_text="Customer's Balance will not be churned")
      

if __name__=="__main__":
    app.run(debug=True)            
