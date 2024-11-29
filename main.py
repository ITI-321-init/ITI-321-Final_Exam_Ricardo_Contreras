"""================================================================================================
Institute....: Universidad Técnica Nacional
Headquarters.: Pacífico
Career.......: Tecnologías de la Información
Period.......: 3-2024
Document.....: main.py
Goals........: Connection with a API REST
Professor....: Jorge Ruiz (york)
Student......: Ricardo Contreras
================================================================================================"""

from flask import Flask, jsonify, request


#   Student data

app = Flask(__name__)
@app.route('/students', methods=['GET'])
def get_students():
    student_data = {
        "Data": {
            "Student": {
                "Last Name": "Contreras Ocampo",
                "Phone Number": 88290961,
                "Mail": "jcontreraso@est.utn.ac.cr",
                "Id": 604740958,
                "Level": "Jr. ",
                "Name": "Jose Ricardo"
            },
            "status_code": 200,
            "status_message": "OK"
        }
    }
    return jsonify(student_data)

@app.route('/data', methods=['POST'])
def inster_values():
    data = request.get_json()
    a = data.get('a', 0)
    b = data.get('b', 0)
    c = data.get('c', 0)
    d = data.get('d', 0)

    total_values = len([a, b, c, d])

    response = {
        "Result": {
            "Values": {
                "Toltal # of values": total_values
            },
            "status_code": 201,
            "status_message": "Created"
        }
    }
    return jsonify(response)




if __name__ == '__main__':
    app.run(host='localhost', port=5001)

