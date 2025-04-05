from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import Rule, db
from flask_swagger_ui import get_swaggerui_blueprint
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:////tmp/test.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Rule Validation API"
    }
)
app.register_blueprint(swaggerui_blueprint)

with app.app_context():
    db.create_all()

@app.route('/rules', methods=['GET', 'POST'])
def rules():
    if request.method == 'GET':
        is_active = request.args.get('is_active')
        if is_active is not None:
            try:
                is_active = is_active.lower() == 'true'
            except ValueError:
                return jsonify({'error': 'Invalid value for is_active. Must be true or false.'}), 400
            rules = Rule.query.filter_by(is_active=is_active).all()
        else:
            rules = Rule.query.all()
        return jsonify([{'id': rule.id, 'name': rule.name, 'description': rule.description, 'condition': rule.condition, 'action': rule.action, 'is_active': rule.is_active} for rule in rules])
    elif request.method == 'POST':
        data = request.get_json()
        new_rule = Rule(name=data['name'], description=data['description'], condition=data['condition'], action=data['action'])
        db.session.add(new_rule)
        db.session.commit()
        return jsonify({'message': 'Rule created successfully'}), 201

@app.route('/rules/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def rule(id):
    rule = Rule.query.get_or_404(id)

    if request.method == 'GET':
        return jsonify({'id': rule.id, 'name': rule.name, 'description': rule.description, 'condition': rule.condition, 'action': rule.action, 'is_active': rule.is_active})

    elif request.method == 'PUT':
        data = request.get_json()
        rule.name = data['name']
        rule.description = data['description']
        rule.condition = data['condition']
        rule.action = data['action']
        rule.is_active = data.get('is_active', rule.is_active)
        db.session.commit()
        return jsonify({'message': 'Rule updated successfully'})

    elif request.method == 'DELETE':
        db.session.delete(rule)
        db.session.commit()
        return jsonify({'message': 'Rule deleted successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)