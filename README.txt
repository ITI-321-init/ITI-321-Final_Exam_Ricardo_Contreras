================================================================================================
Institute....: Universidad Técnica Nacional
Headquarters.: Pacífico
Career.......: Tecnologías de la Información
Period.......: 3-2024
Document.....: README.txt
Goals........: Information
Professor....: Jorge Ruiz (york)
Student......: Ricardo Contreras
================================================================================================


You must use Postman to get request from the API

HTTP Calls and Methos:

GET http://127.0.0.1:5001/students
POST http://localhost:5001/data
GET http://127.0.0.1:5001/statistics
GET http://localhost:5001/square
GET http://localhost:5001/raised_by_exponent
GET http://localhost:5001/int/2

Expected results:



Students:
{
    "Data": {
        "Student": {
            "Id": 604740958,
            "Last Name": "Contreras Ocampo",
            "Level": "Jr. ",
            "Mail": "jcontreraso@est.utn.ac.cr",
            "Name": "Jose Ricardo",
            "Phone Number": 88290961
        },
        "status_code": 200,
        "status_message": "OK"
    }
}



Data:
Input via JSON:
{
    "a": 3,
    "b": 2,
    "c": 7,
    "d": 4
}

Output:
{
    "Result": {
        "Values": {
            "Total # of values": 4
        },
        "status_code": 201,
        "status_message": "Created"
    }
}




Statistics:
{
    "Result": {
        "Values": {
            "a": 3,
            "b": 2,
            "c": 7,
            "d": 4
        },
        "Statistics": {
            "Max": 7,
            "Min": 2,
            "Sum": 16,
            "Total # of values": 4,
            "average": 4.0
        },
        "status_code": 200,
        "status_message": "OK"
    }
}



Square:
{
    "Result": {
        "original values": {
            "a": 3,
            "b": 2,
            "c": 7,
            "d": 4
        },
        "squared values": {
            "a": 9,
            "b": 4,
            "c": 49,
            "d": 16
        },
        "status_code": 200,
        "status_message": "OK"
    }
}



Raised By Exponet:
{
    "Result": {
        "d_elevados": {
            "a": 27,
            "b": 4,
            "c": 823543,
            "d": 256
        },
        "d_originales": {
            "a": 3,
            "b": 2,
            "c": 7,
            "d": 4
        },
        "status_code": 200,
        "status_message": "OK"
    }
}



Int:
{
    "Result": {
        "Number of bits": 16,
        "Without Simbol": "0 to 65535",
        "with Simbol": "-32768 to 32767"
    },
    "status_code": 200,
    "status_message": "OK"
}

