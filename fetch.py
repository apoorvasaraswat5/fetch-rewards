from flask import Flask, request, Response, jsonify
from utility import calculate_points, generate_unique_id

app = Flask(__name__)


points_storage = {}

@app.route('/receipts/process', methods=['POST'])
def process_receipts():
    receipt_data = request.json

    points = calculate_points(receipt_data)

    receipt_id = generate_unique_id()
    points_storage[receipt_id] = points

    return jsonify({'id': receipt_id})


@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_points_for_receipt(receipt_id):

    if receipt_id not in points_storage:
        # return jsonify({'description': "Invalid receipt id!"})
        return Response("Invalid receipt Id!", status=404)

    points = points_storage[receipt_id]
    return jsonify({'points': points})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000,debug=True)
