from flask import Flask, jsonify, request,make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os 


def create_app():
    # Start the Flask app
    app = Flask(__name__)

    # Set configs
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI")

    #"sqlite:///dbdatabase.db"
    #


    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Instantiate db object
    db = SQLAlchemy(app)

    # Create marshmallow object
    ma = Marshmallow(app)

    # Create database
    class Person(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(200), nullable=False)
        details = db.Column(db.String(400), nullable=False)

        def __init__(self, name, details):
            self.name = name
            self.details = details

    # Create schema
    class PersonSchema(ma.Schema):
        class Meta:
            fields = ('id', 'name', 'details')

    # Create an instance of the schema
    person_schema = PersonSchema()
    persons_schema = PersonSchema(many=True)

    # error handeling


    @app.errorhandler(400)
    def handle_400_error(_error):
        """Return a http 400 error to client"""
        return make_response(jsonify({'error': 'Misunderstood'}), 400)


    @app.errorhandler(401)
    def handle_401_error(_error):
        """Return a http 401 error to client"""
        return make_response(jsonify({'error': 'Unauthorised'}), 401)


    @app.errorhandler(404)
    def handle_404_error(_error):
        """Return a http 404 error to client"""
        return make_response(jsonify({'error': 'Not found'}), 404)


    @app.errorhandler(500)
    def handle_500_error(_error):
        """Return a http 500 error to client"""
        return make_response(jsonify({'error': 'Server error'}), 500)



    # Use the Flask application context
    with app.app_context():
        # Create all the database tables
        db.create_all()

    @app.route('/api', methods=['POST'])
    def create_person():
        try:
            name = request.json['name']
            details = request.json['details']

            new_person = Person(name=name, details=details)

            db.session.add(new_person)
            db.session.commit()

            return person_schema.jsonify(new_person)

        except Exception as e:
            return jsonify({"Error": "Invalid request."})


    #view all persons 
    @app.route('/api', methods=['GET'])
    def get_persons():
        persons = Person.query.all()
        result_set = persons_schema.dump(persons)
        return jsonify(result_set)

    #view one person

    @app.route('/api/<int:id>', methods=['GET'])
    def get_person(id):
        person = Person.query.get_or_404(int(id))
        return person_schema.jsonify(person)


    #update one person

    @app.route('/api/<int:id>', methods=['PUT'])
    def update_person(id):
        person = Person.query.get_or_404(int(id))


        name = request.json['name']
        details = request.json['details']

        person.name = name
        person.details = details
        db.session.commit()

        return person_schema.jsonify(person)

    #delete one person 

    @app.route('/api/<int:id>', methods=['DELETE'])
    def delete_person(id):
        person = Person.query.get_or_404(int(id))
        db.session.delete(person)
        db.session.commit()
        return jsonify({"success": "person has been removed"})



        

    return app.run(host='0.0.0.0', port=10000, debug=True)

