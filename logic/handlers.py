from utils.db import db
from models.address import Address, PKey
from cryptography.fernet import Fernet

key = Fernet.generate_key()


def get_all(data):
    addresses = []

    for item in data:
        info = {
            "crypto_type": item.crypto_type,
            "address": item.address
        }
        addresses.append(info)

    return addresses


def add_data(data):
    p_key_to_rec = data["p_key"]
    encrypted_p_key = Fernet(key).encrypt(bytes(p_key_to_rec, 'utf-8'))
    new_record = PKey(encrypted_p_key)
    db.session.add(new_record)
    db.session.commit()
    last_addr = PKey.query.order_by(PKey.id.desc()).first()
    new_data = Address(data["crypto_type"], data["address"], last_addr.id)
    db.session.add(new_data)
    db.session.commit()
