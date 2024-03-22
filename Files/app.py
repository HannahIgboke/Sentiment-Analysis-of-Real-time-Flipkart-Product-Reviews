from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# First route - the home page
@app.route('/')
def home():
    return render_template('home.html')

# Second route - the prediction page
@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    reviewer = request.form.get("reviewer name")
    product = request.form.get('product name')
    
    if request.method == 'POST':
        review = request.form.get("review")

        if not review:
            message = 'Enter review.'
            return render_template('home.html', message=message)
        else:
            model = joblib.load('model/naive_bayes.pkl')
            prediction = model.predict([review])[0]
            return render_template('output.html', prediction=prediction)
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

