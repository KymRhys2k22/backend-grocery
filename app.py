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

@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.json
    for item in grocery_items:
        if item["id"] == item_id:
            item["name"] = data["name"]
            item["quantity"] = data["quantity"]
            item["price"] = data["price"]
            return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global grocery_items
    grocery_items = [item for item in grocery_items if item["id"] != item_id]
    return '', 204

if __name__ == "__main__":
    app.run()
