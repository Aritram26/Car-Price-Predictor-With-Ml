from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and encoders
model = joblib.load('car_price_model.pkl')
label_encoder_name = joblib.load('label_encoder_name.pkl')
label_encoder_company = joblib.load('label_encoder_company.pkl')
label_encoder_fuel_type = joblib.load('label_encoder_fuel_type.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    name = request.form['name']
    company = request.form['company']
    year = int(request.form['year'])
    kms_driven = int(request.form['kms_driven'])
    fuel_type = request.form['fuel_type']

    name_encoded = label_encoder_name.transform([name])[0]
    company_encoded = label_encoder_company.transform([company])[0]
    fuel_type_encoded = label_encoder_fuel_type.transform([fuel_type])[0]

    features = np.array([[name_encoded, company_encoded, year, kms_driven, fuel_type_encoded]])
    prediction = model.predict(features)[0]

    return render_template('index.html', prediction_text=f'Estimated Car Price: {prediction:.2f}')

if __name__ == '__main__':
    app.run(debug=True)
