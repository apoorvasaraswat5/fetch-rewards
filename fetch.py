from flask import Flask, request, Response, jsonify
from utility import calculate_points, generate_unique_id

app = Flask(__name__)

# storing receipts point data in memory
points_storage = {}

@app.route('/receipts/process', methods=['POST'])
def process_receipts():
    """
    This endpoint processes receipts and calculates
    points for the receipt based on some business rules
    :return: unique id for the receipt
    """
    receipt_data = request.json

    points = calculate_points(receipt_data)

    receipt_id = generate_unique_id()
    points_storage[receipt_id] = points

    return jsonify({'id': receipt_id})


@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_points_for_receipt(receipt_id):
    """
    This endpoint returns the points based on
    receipt's unique id, and throws error if
    the id does not exist
    :param receipt_id: unique id of receipt
    :return: points for the receipt id
    """

    if receipt_id not in points_storage:
        return Response("Invalid receipt Id!", status=404)

    points = points_storage[receipt_id]
    return jsonify({'points': points})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000,debug=True)
