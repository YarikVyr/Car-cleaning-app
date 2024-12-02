from flask import Flask, jsonify, request
import json

app = Flask(__name__)
with open('data.json', 'r') as f:
    data = json.load(f)

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(data['orders']), 200

@app.route('/orders', methods=['POST'])
def add_order():
    new_order = request.get_json()
    max_id = max([order['id'] for order in data['orders']] or [-1]) + 1
    new_order['id'] = max_id
    data['orders'].append(new_order)
   
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
        
    return jsonify({'message': 'Заказ успешно создан'}), 201

if __name__ == '__main__':
    app.run(debug=True)
