import flask
import requests
import flask_marshmallow
from flask import request, jsonify
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource , reqparse
import os

app = flask.Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/data_sql'+ os.path.join(basedir,'db.postgresql')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
api = Api(app)
Computers = [
    {
        "id" : 0,
        "computer_name" : "Dell",
        "hard_drive" : "Dell 500GB 7,200 RPM SATA 2.5in Hard Drive",
        "processor" : "Intel Core i9 processor",
        "ram_amount" : 8,
        "maximum_ram" : 8,
        "hard_drive_space" : "512GB",
        "form_factor" : "18.3 cm (7.2 in)"
    },
     {
         "id" :1,
        "computer_name" : "LG",
        "hard_drive" : "HDD",
        "processor" : "Intell Pentium II 350Hz processor",
        "ram_amount" : 60,
        "maximum_ram" : 512,
        "hard_drive_space" : "2000GB",
        "form_factor" : "63.5 cm"
    }
]
 
class Computer_api(Resource):
    def get(self, name): # READ
        for Computer in Computers:
            if(name == Computer["computer_name"]):
                return Computer,200
        return "Computer not found" ,404


    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    @app.route('/', methods=['GET'])
    def home():
        return '''<h1>Computers</h1>
        <p>A prototype API for Umuzi Computers.</p>'''

    @app.route('/api/v1/resources/Computers/all', methods=['GET'])
    def api_all(): 
        conn = sqlite3.connect('Computers.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()
        all_Computers = cur.execute('SELECT * FROM Computers;').fetchall()

        return jsonify(all_Computers)

    def read():
        # Create the list of people from our data
        return [Computers[key] for key in sorted(Computer.keys())]

    def post(self, name): # Create
        parser  = reqparse.RequestParser()
        parser.add_argument("hard_drive")
        parser.add_argument("processor")
        parser.add_argument("ram_amount")
        parser.add_argument("maximum_ram")
        parser.add_argument("hard_drive_space")
        parser.add_argument("form_factor")
        args = parser.parse_args()


        for Computer in Computers:
             if(name == computer["computer_name"]):
                Computer["hard_drive"] = args["hard_drive"]
                Computer["processor"] = args["processor"]
                Computer["ram_amount"] = args["ram_amount"]
                Computer["maximum_ram"] = args["maximum_ram"]
                Computer["hard_drive_space"] = args["hard_drive_space"]
                Computer["form_factor"] = args["form_factor"]
                return Computer, 200

        Computer = {
            "computer_name" : name,
            "hard_drive" : args["hard_drive"],
            "processor" : args["processor"],
            "ram_amount" : args["ram_amount"],
            "maximum_ram" : args["maximum_ram"],
            "hard_drive_space" : args["hard_drive_space"],
            "form_factor" : args["form_factor"]
        }
        Computers.append(computer)
        return computer, 201

    def put(self, name): # Update
        parser  = reqparse.RequestParser()
        parser.add_argument("hard_drive")
        parser.add_argument("processor")
        parser.add_argument("ram_amount")
        parser.add_argument("maximum_ram")
        parser.add_argument("hard_drive_space")
        parser.add_argument("form_factor")
        args = parser.parse_args()


        for Computer in Computers:
            if(name == computer["computer_name"]):
                Computer["hard_drive"] = args["hard_drive"]
                Computer["processor"] = args["processor"]
                Computer["ram_amount"] = args["ram_amount"]
                Computer["maximum_ram"] = args["maximum_ram"]
                Computer["hard_drive_space"] = args["hard_drive_space"]
                Computer["form_factor"] = args["form_factor"]
                return computer, 200

        Computer = {
            "computer_name" : name,
             "hard_drive" : args["hard_drive"],
             "processor" : args["processor"],
             "ram_amount" : args["ram_amount"],
             "maximum_ram" : args["maximum_ram"],
             "hard_drive_space" : args["hard_drive_space"],
             "form_factor" : args["form_factor"]
        }
        Computers.append(Computer)
        return Computer, 201

    def delete(self, name): # Delete
        global Computers
        Computers = [Computer for Computer in Computers if Computer["computer_name"] != name]
        return "<h1>404</h1><p>The resource could not be found.</p>", 404

    @app.route('/api/v1/resources/Computers', methods=['GET'])
    def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
        if 'id' in request.args:
            id = int(request.args['id'])
        else:
            return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
        results = []

        for Computer in Computers:
            if Computer['id'] == id:
                results.append(Computer)
        return jsonify(results)

app.run()
api.add_resource(Computer_api, "/Computer/<string:name>")
app.run(debug=True)
