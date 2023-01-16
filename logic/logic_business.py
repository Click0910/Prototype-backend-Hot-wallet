import hashlib, base58, binascii, ecdsa, codecs
from sha3 import keccak_256


def create_address(id):

    if id == "btc":

        ecdsa_private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        ecdsa_public_key = '04' + ecdsa_private_key.get_verifying_key().to_string().hex()
        hash_256_ecdsa_public_key = hashlib.sha256(binascii.unhexlify(ecdsa_public_key)).hexdigest()
        ridemp160_hash_256 = hashlib.new('ripemd160', binascii.unhexlify(hash_256_ecdsa_public_key))
        prepend_network_byte = '00' + ridemp160_hash_256.hexdigest()
        hash = prepend_network_byte
        for x in range(1,3):
            hash = hashlib.sha256(binascii.unhexlify(hash)).hexdigest()
        cheksum = hash[:8]
        append_checksum = prepend_network_byte + cheksum
        bitcoin_address = base58.b58encode(binascii.unhexlify(append_checksum)).decode('utf8')
        return bitcoin_address, ecdsa_private_key.to_string().hex()

    elif id == "eth":

        ecdsa_private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        ecdsa_public_key = '04' + ecdsa_private_key.get_verifying_key().to_string().hex()
        public_key_bytes = codecs.decode(ecdsa_public_key, 'hex')
        eth_address = keccak_256(public_key_bytes).digest()[-20:].hex()
        return eth_address, ecdsa_private_key.to_string().hex()
