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

# Variable global para almacenar los valores
global_values = {}

@app.route('/data', methods=['POST'])
def insert_values():
    #   You can try any number you want, but only 4.....
    value_data = request.get_json()
    a = value_data.get('a', 0)
    b = value_data.get('b', 0)
    c = value_data.get('c', 0)
    d = value_data.get('d', 0)

    # Almacenamos los valores en la variable global
    global global_values
    global_values = {'a': a, 'b': b, 'c': c, 'd': d}

    # Calculamos el total de valores
    total_values = len([a, b, c, d])

    response = {
        "Result": {
            "Values": {
                "Total # of values": total_values
            },
            "status_code": 201,
            "status_message": "Created"
        }
    }
    return jsonify(response)


@app.route('/statistics', methods=['GET'])
def get_statistics():
    global global_values

    # Verificamos si hay datos en global_values
    if not global_values:
        return jsonify({"error": "No data available This is just a Safety method"}), 404


#ChatGPT was used here, lost track with variables names..... Im sorry
    #specialy with this one:
    values_list = list(global_values.values())
    max_value = max(values_list)
    min_value = min(values_list)
    sum_value = sum(values_list)
    average_value = sum_value / len(values_list)
    total_values = len(values_list)

    response = {
        "Result": {
            "Values": global_values,
            "Statistics": {
                "Max": max_value,
                "Min": min_value,
                "Total # of values": total_values,
                "average": average_value,
                "Sum": sum_value,
            },
            "status_code": 200,
            "status_message": "OK"
        }
    }
    return jsonify(response)

@app.route('/square', methods=['GET'])
def get_square():
    global global_values
    if not global_values:
        return jsonify({"error": "No data available This is just a Safety method"}), 404
                #This solution is form StackOverflow, the "key" variable acts just like a Keyword in this case
                #This means that global_values is the key in this case, and will be alternated
    squared_values = {key: value ** 2 for key, value in global_values.items()}
    response = {
        "Result": {
            "squared values": squared_values,
            "original values": global_values,
            "status_code": 200,
            "status_message": "OK"
        }
    }
    return jsonify(response)




@app.route('/raised_by_exponent', methods=['GET'])
def getr_exponent():
    global global_values


    if not global_values:
        return jsonify({"error": "No data available This is just a Safety method"}), 404

    def raised(values):
        return {key: value ** value for key, value in global_values.items()}
    raised_values = raised(global_values)
    response = {
        "Result": {
            "d_elevados": raised_values,
            "d_originales": global_values,
            "status_code": 200,
            "status_message": "OK"
        }
    }
    return jsonify(response)




@app.route('/int/<int:n>', methods=['GET'])
def get_integer_capacity(n):
    # Comprobamos si el valor proporcionado por el usuario es un número válido
    if n <= 0:
        return jsonify({"error": "Number must be more the 0"}), 400

    # Calculamos el rango de valores dependiendo del tamaño en bits
    con_signo = f"-{2**(n*8-1)} to {2**(n*8-1)-1}"
    sin_signo = f"0 to {2**(n*8)-1}"
    n_bits = n * 8

    response = {
        "Result": {
            "with Simbol": con_signo,
            "Without Simbol": sin_signo,
            "Number of bits": n_bits
        },
        "status_code": 200,
        "status_message": "OK"
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='localhost', port=5001)
