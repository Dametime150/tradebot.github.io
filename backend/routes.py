from flask import Blueprint, jsonify, request
from mexc_bot import MEXCTradingBot

api_routes = Blueprint("api", __name__)
bot = MEXCTradingBot()

@api_routes.route("/account", methods=["GET"])
def get_account_info():
    data = bot.get_account_info()
    return jsonify(data)

@api_routes.route("/trade", methods=["POST"])
def trade():
    data = request.json
    response = bot.place_order(data["symbol"], data["side"], data["quantity"], data["price"])
    return jsonify(response)
