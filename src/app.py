from flask import Flask
from flask import request, make_response
from io import StringIO
import csv
import json


from utils import get_risk, get_bmi


app = Flask(__name__)


@app.route('/calculateBmi', methods=['POST', 'GET'])
def calculateBmi():
    string_io = StringIO()
    csv_writer = csv.writer(string_io)
    input_data = request.data
    if input_data:
        input_data = json.loads(request.data)
    else:
        input_data = []
    csv_writer.writerow(["Gender", "HeightCm", "WeightCm", "BMI", "Risk"])
    for person in input_data:
        bmi = get_bmi(
                person.get("WeightKg", 0),
                person.get("HeightCm", 0)
            )
        csv_writer.writerow(
            [
                person.get("Gender", ""),
                person.get("HeightCm", 0),
                person.get("WeightKg", 0),
                bmi,
                get_risk(bmi)
            ]
        )
    output = make_response(string_io.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"

    return output


if __name__ == '__main__':
    app.run(port=3000, debug=True)
