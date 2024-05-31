# Car Price Predictor

This project is a Car Price Predictor application built using Machine Learning. It predicts the price of a car based on various features such as the car's name, company, year of manufacture, kilometers driven, and fuel type.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
The Car Price Predictor uses a machine learning model to estimate the price of a car based on the input features provided by the user. It leverages the Flask web framework for the web interface and provides a simple and user-friendly way to input car details and get the price prediction.

## Installation
To get a local copy up and running follow these simple steps.

### Prerequisites
Make sure you have Python and Git installed on your system.


### Install required packages
Create a virtual environment and install the necessary dependencies:
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Prepare the dataset
Make sure you have the dataset file named `car_data.csv` in the project directory. The CSV file should contain the following columns:
- `name`
- `company`
- `year`
- `Price`
- `kms_driven`
- `fuel_type`

## Usage
1. **Train the model:**
   Run the `train_model.py` script to train the machine learning model on the dataset.
   ```sh
   python train_model.py
   ```

2. **Start the Flask web server:**
   ```sh
   python app.py
   ```

3. **Access the web application:**
   Open your web browser and navigate to `http://127.0.0.1:5000/`. You should see the Car Price Predictor web interface.

4. **Predict car price:**
   Fill in the details of the car (name, company, year, kilometers driven, and fuel type) and click the "Predict" button to get the estimated price of the car.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements
- [Pandas](https://pandas.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [Flask](https://flask.palletsprojects.com/)
- [Jinja2](https://jinja.palletsprojects.com/)
```

