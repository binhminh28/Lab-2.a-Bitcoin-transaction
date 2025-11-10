from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


cust1_private_key = CBitcoinSecret(
    'cNrDvCDrJrmpnjVMhZSLonyGdXUymruk2gHS45ZRWgvQjoWzw9rg')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cPjhAaUck8jhLWbECpYVR3woXkzNiTj8zxYWwmtqHbghPJoTarTA')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cTg9dN3RxmpVfkBCUmHQ7fz12jNy4PuwUoqLD4tCP5QBRFYQn8qz')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

Q3a_txout_scriptPubKey = [
        # fill this in!
        my_public_key,
        OP_CHECKSIGVERIFY,
        OP_1,             
        cust1_public_key, 
        cust2_public_key, 
        cust3_public_key, 
        OP_3,            
        OP_CHECKMULTISIG  
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0001 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '8f3a2585ff47b0f9116cc69da2a35e5605c987c6cacbbae40cb6787d056ffa60')
    utxo_index = 4 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, 
        utxo_index, Q3a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)

# @binhminh28 ➜ /workspaces/Lab-2.a-Bitcoin-transaction (main) $ python Q3a.py 
# 201 Created
# {
#   "tx": {
#     "block_height": -1,
#     "block_index": -1,
#     "hash": "54480c1b10eed54d6cf2eed6c7609e41fbe3af91e37f64f7039902c5af844ca0",
#     "addresses": [
#       "mpqgD4LbdPTvZTVPAH2JhZ6SCunVsDxsGz",
#       "zPAaS6VMLTihpuH69rpyMUNrn9z6N3nTbp"
#     ],
#     "total": 10000,
#     "fees": 20008,
#     "size": 306,
#     "vsize": 306,
#     "preference": "medium",
#     "relayed_by": "23.97.62.118",
#     "received": "2025-11-10T15:59:43.968408129Z",
#     "ver": 1,
#     "double_spend": false,
#     "vin_sz": 1,
#     "vout_sz": 1,
#     "confirmations": 0,
#     "inputs": [
#       {
#         "prev_hash": "8f3a2585ff47b0f9116cc69da2a35e5605c987c6cacbbae40cb6787d056ffa60",
#         "output_index": 4,
#         "script": "47304402200f322984aa3034a601107b3ab6e5be5a33392f1b1e4149ac91fc688adcb699d10220103cda5d9354419467d8eb6e86c57c1b35f5b3a8e778e90138c0da1b1bb2e3c1012103619d3ab10a627c73547a37b4fe54de29d0b1318cac253ad70f4dab8c796ce099",
#         "output_value": 30008,
#         "sequence": 4294967295,
#         "addresses": [
#           "mpqgD4LbdPTvZTVPAH2JhZ6SCunVsDxsGz"
#         ],
#         "script_type": "pay-to-pubkey-hash",
#         "age": 4755705
#       }
#     ],
#     "outputs": [
#       {
#         "value": 10000,
#         "script": "2103619d3ab10a627c73547a37b4fe54de29d0b1318cac253ad70f4dab8c796ce099ad5121023f715ff6bc6f1ae3cb994966e3a5f4b6e2dd7a09996dafc35b13d110de1fc91621023ba8b0914f1e4736e7e48ba2bbace61d5d94d0dd89e03f38318f41e439e791fe2102cc8264033d3d77b64493b5eeafeadec254ffe82a30c81f472cdc3997eab3142853ae",
#         "addresses": [
#           "zPAaS6VMLTihpuH69rpyMUNrn9z6N3nTbp"
#         ],
#         "script_type": "pay-to-multi-pubkey-hash"
#       }
#     ]
#   }
# }