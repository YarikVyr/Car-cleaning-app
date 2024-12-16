
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
import json

app = Flask(name)

@app.route('/orders', methods=['POST'])
def add_order():
    try:
        data = request.get_json()
        validate_data(data)
        save_to_db(data)  # Здесь должна быть логика сохранения данных в базу данных
        return jsonify({'message': 'Order added successfully'}), 201
    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        app.logger.error(f'Internal server error: {str(e)}')
        return jsonify({'error': 'Internal server error'}), 500

def validate_data(data):
    required_fields = ['carModel', 'washType']
    for field in required_fields:
        if field not in data or not data[field]:
            raise BadRequest(f'Missing required field: {field}')

    valid_wash_types = ['обычная', 'глубокая', 'полировка']
    if data['washType'] not in valid_wash_types:
        raise BadRequest(f'Invalid wash type: {data["washType"]}. Valid types are: {", ".join(valid_wash_types)}.')

def save_to_db(data):
    # Логика сохранения данных в базе данных
    pass

if name == 'main':
    app.run(debug=True)
