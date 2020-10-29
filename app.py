from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def calculator():
    return render_template('bmicalc.html')

@app.route('/result', methods=['POST', 'GET'])
def bmi_calculator():
    if request.method == 'POST':
        height = request.form.get('height', type=float)
        weight = request.form.get('weight', type=float)

        print(weight, height)
        bmi = weight / (height**2)

        if bmi < 18.5:
            bmi_result = "Underweight"
        elif 18.5 <= bmi <= 24.9:
            bmi_result = "Healthy"
        elif 25 <= bmi <= 29.9:
            bmi_result = "Overweight"
        elif 30 <= bmi <= 39.9:
            bmi_result = "Obese"
        else:
            bmi_result = "Morbid Obese"

        entry = bmi
        result = bmi_result
        return render_template('bmi_results.html', entry=entry, result=result)

if __name__ == '__main__':
    app.run(debug = True)
