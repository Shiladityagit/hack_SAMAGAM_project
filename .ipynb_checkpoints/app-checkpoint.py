from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('forest.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form
        features = [float(request.form.get('id')),
                    float(request.form.get('week')),
                    float(request.form.get('center_id')),
                    float(request.form.get('meal_id')),
                    float(request.form.get('checkout_price')),
                    float(request.form.get('base_price')),
                    float(request.form.get('emailer_for_promotion')),
                    float(request.form.get('homepage_featured')),
                    # Add more features as needed
                    ]

        # Convert the features to the format expected by your model
        features = [features]  # Convert to a list of lists if necessary

        # Make a prediction
        prediction = model.predict(features)

        # Render the prediction on the HTML template
        return render_template('forest.html', prediction=int(prediction[0]))

    except Exception as e:
        return render_template('forest.html', error=str(e))

if __name__ == '_main_':
    app.run(debug=True)
