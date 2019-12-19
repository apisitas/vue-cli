import sqlite3
import json
from flask_cors import CORS


def cursor():
    sqliteConnection = sqlite3.connect("user.db")
    return sqliteConnection.cursor()


# query = cursor.execute(
#     "INSERT INTO users (first_name,last_name,email,gender,age) VALUES ('John','Cena','john@gmail.com','female','22');"
# )
# sqliteConnection.commit()
# cursor.close()


from flask import Flask

app = Flask(__name__)
CORS(app)


def query(schema):
    cursor = sqlite3.connect("user.db").cursor().execute(schema)
    if cursor.description:
        row_headers = [x[0] for x in cursor.description]
        rv = cursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        cursor.close()
        return json.dumps(json_data)
    return "true"


@app.route("/getByuserId")
def getByuserId():
    return query("select * from users where id = 1")


@app.route("/getByfirstName")
def getByfirstName():
    return query("select * from users where first_name='ernestine';")


@app.route("/getBylastName")
def getBylastName():
    return query("select * from users where last_name='millins';")


@app.route("/getByemail")
def getByemail():
    return query("select * from users where email='garington3@topsy.com';")


@app.route("/getBybetween")
def getBybetween():
    return query("select * from users where age between 15 and 16;")


@app.route("/getBygender")
def getBygender():
    return query("select * from users where gender='female';")


@app.route("/getByInsert")
def getByInsert():
    return query(
        "INSERT INTO users (first_name,last_name,email,gender,age) VALUES ('John','Cena','john@gmail.com','female','22');"
    )
