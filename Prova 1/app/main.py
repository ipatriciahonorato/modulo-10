from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Memória para armazenar os pedidos
orders = []
order_id_counter = 1

# Endpoint para criar um novo pedido
@app.route("/novo", methods=["POST"])
def create_order():
    global order_id_counter
    data = request.json
    if not data or not all(key in data for key in ("name", "email", "description")):
        return jsonify({"error": "Invalid input data"}), 400

    order = {
        "id": order_id_counter,
        "name": data["name"],
        "email": data["email"],
        "description": data["description"]
    }
    orders.append(order)
    order_id_counter += 1
    return jsonify({"id": order["id"]}), 201

# Endpoint para obter todos os pedidos
@app.route("/pedidos", methods=["GET"])
def get_orders():
    return jsonify(orders), 200

# Endpoint para obter um pedido por ID
@app.route("/pedidos/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = next((order for order in orders if order["id"] == order_id), None)
    if order is None:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order), 200

# Endpoint para atualizar um pedido por ID
@app.route("/pedidos/<int:order_id>", methods=["PUT"])
def update_order(order_id):
    data = request.json
    if not data or not all(key in data for key in ("name", "email", "description")):
        return jsonify({"error": "Invalid input data"}), 400

    order = next((order for order in orders if order["id"] == order_id), None)
    if order is None:
        return jsonify({"error": "Order not found"}), 404

    order["name"] = data["name"]
    order["email"] = data["email"]
    order["description"] = data["description"]
    return jsonify(order), 200

# Endpoint para deletar um pedido por ID
@app.route("/pedidos/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    global orders
    order = next((order for order in orders if order["id"] == order_id), None)
    if order is None:
        return jsonify({"error": "Order not found"}), 404

    orders = [order for order in orders if order["id"] != order_id]
    return jsonify({"message": "Order deleted successfully"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)
