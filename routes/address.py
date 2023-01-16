from flask import Blueprint, request
from models.address import Address
from logic.handlers import get_all, add_data
from logic.logic_business import create_address


address = Blueprint("address", __name__)


@address.route("/generate-address", methods=["POST"])
def generate_address():
    input_data = request.get_json()
    addr, p_key = create_address(input_data["crypto_type"])
    data = {
        "crypto_type": input_data["crypto_type"],
        "address": addr,
        "p_key": p_key
    }
    add_data(data)
    data_returned = {
        "addres": addr,
        "Private_key": f"{p_key} Please store this value in a safe place, not possible recover this value after"

    }
    return data_returned


@address.route("/list-address", methods=["GET"])
def list_address():

    data = Address.query.all()
    data_returned = get_all(data)
    return data_returned


@address.route("/retrieve-address/crypto-type/<id>", methods=["GET"])
def retrieve_address(id):

    data = Address.query.filter_by(crypto_type=id).all()
    data_returned = get_all(data)
    return data_returned

