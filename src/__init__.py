import requests
from src.processor import Processor
from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__, static_folder='templates')


@app.route('/', methods =["GET", "POST"])
def cowin():
    if request.method == "POST":
        email = request.form.get("email")
        vaccine = request.form.get("vaccine")
        state = request.form.get("state")
        age = request.form.get("age")
        fees = request.form.get("fees")
        return 'OK'
    if request.method == "GET":
        varanasi = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=696&date=04-06-2021"
        result = requests.get(varanasi).json()
        processor = Processor(result)
        filtered = processor.filter_vaccine(1, 18)
        print(filtered)
        return render_template("form.html", title="Welcome to Covid vaccine poller", result=filtered)


if __name__ == "__main__":
    app.run(debug=True)