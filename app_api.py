from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Computer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    hard_drive = db.Column(db.VARCHAR(100))
    processor = db.Column(db.VARCHAR(100))
    ram_amount = db.Column(db.Float)
    maximum_ram = db.Column(db.Float)
    hard_drive_space = db.Column(db.VARCHAR(100))
    form_factor = db.Column(db.VARCHAR(100))

    def __init__(self, name, hard_drive, processor, ram_amount, maximum_ram, hard_drive_space, form_factor):
        self.name = name
        self.hard_drive = hard_drive
        self.processor = processor
        self.ram_amount = ram_amount
        self.maximum_ram = maximum_ram
        self.hard_drive_space = hard_drive_space
        self.form_factor = form_factor

class ComputerSchema(ma.Schema):
    class Meta:
        fields = ('id','name','hard_drive', 'processor', 'ram_amount', 'maximum_ram', 'hard_drive_space', 'form_factor')

computer_schema = ComputerSchema(strict=True)
computers_schema = ComputerSchema(many=True, strict=True)

@app.route('/computer', methods=['POST'])
def add_computer():
    name = request.json['name']
    hard_drive = request.json['hard_drive']
    processor = request.json['processor']
    ram_amount = request.json['ram_amount']
    maximum_ram = request.json['maximum_ram']
    hard_drive_space = request.json['hard_drive_space']
    form_factor = request.json['form_factor']
    

    new_computer = Computer(name, hard_drive, processor, ram_amount, maximum_ram, hard_drive_space, form_factor)
    db.session.add(new_computer)
    db.session.commit()

    return computer_schema.jsonify(new_computer)

@app.route('/computer', methods=['GET'])
def get_computers():
    all_computers = Computer.query.all()
    result = computers_schema.dump(all_computers)
    return jsonify(result.data)

@app.route('/computer/<id>', methods=['GET'])
def get_computer(id):
    computer = Computer.query.get(id)
    # result = computers_schema.dump(all_computers)
    return computer_schema.jsonify(computer)

@app.route('/computer/<id>', methods=['PUT'])
def update_computer(id):
    computer = Computer.query.get(id)

    name = request.json['name']
    hard_drive = request.json['hard_drive']
    processor = request.json['processor']
    ram_amount = request.json['ram_amount']
    maximum_ram = request.json['maximum_ram']
    hard_drive_space = request.json['hard_drive_space']
    form_factor = request.json['form_factor']

    computer.name = name
    computer.hard_drive = hard_drive
    computer.processor = processor
    computer.ram_amount = ram_amount
    computer.maximum_ram = maximum_ram
    computer.hard_drive_space  = hard_drive_space
    computer.form_factor = form_factor
    
    db.session.commit()

    return computer_schema.jsonify(computer)

@app.route('/computer/<id>', methods=['DELETE'])
def delete_computer(id):
    computer = Computer.query.get(id)
    db.session.delete(computer)
    db.session.commit()
    # result = computers_schema.dump(all_computers)
    return computer_schema.jsonify(computer)

if __name__ =='__main__':
    app.run(debug=True)