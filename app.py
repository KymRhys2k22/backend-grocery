from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

grocery_items = []
item_id = 1


@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(grocery_items)


@app.route("/items", methods=["POST"])
def add_item():
    global item_id
    data = request.json
    item = {
        "id": item_id,
        "name": data["name"],
        "quantity": data["quantity"],
        "price": data["price"]
    }
    grocery_items.append(item)
    item_id += 1
    return jsonify(item), 201


if __name__ == "__main__":
    app.run()
