Flask Prototype wallet.

This project is a wallet prototype for technical assessment. Please consider the next points:

1. This is just a prototype and cannot be considered as a real hot wallet, is just for tech assessment.
2. The project store data in postgres database, one table store the  private keys encrypted. take into account that in
   a real wallet store a private key is the most crucial part, we need to consider things like advance encrypting, 
   two-factor authentication, cold storage, os variable environments, valuts  and other aspects relevan to crypto fields that would take more time than just 3
   days for implementation. Even though professionals in this field recommend hardware wallets or even paper wallets.
3. There is a script for implementation of seed phrases, but the private keys are not generated using the seed phrase. 
   This is because this is my first contact with the crypto world and to implement a full total wallet would take more 
   than 3 days, specially because some topics are new for me.
4. As I mentioned before, this project is just as prototype for tech assessment, however is possible continue working on 
   this repo to get a real hot wallet app.

--------------------------

Endpoints:

The project have 3 endpoints:

1. http://127.0.0.1:5000/address/generate-address [POST] payload: {
    "crypto_type": "btc"
} Is supported also "crypto_type": "eth"

2. http://127.0.0.1:5000/address/list-address [GET]
3. http://127.0.0.1:5000/address/retrieve-address/crypto-type/eth [GET]

Swagger documentation in progress, although at the moment is tiny.

-------------------

Installation:

this project requires:

1. Python 3
2. PostgresSQL

Note: If you get some problems with python interpreter use python 3.8

before run the app you must create the following environment variables:

POSTGRESQL_USER=
POSTGRESQL_PASSWORD=
POSTGRESQL_DATABASE=
POSTGRESQL_HOST=
POSTGRESQL_PORT=
ENTROPY= 

Note: You should generate your own entropy (this is related with the seed phrase)

Run de project:


1. pip install -r requirements.txt
2. python index.py

