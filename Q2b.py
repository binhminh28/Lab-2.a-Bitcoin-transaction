from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import P2PKH_scriptPubKey
from Q2a import Q2a_txout_scriptPubKey


######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.00008 # amount of BTC in the output you're sending minus fee
txid_to_spend = (
        '0eef8dbd8920bb85c9a2aa359b12b2dab6b6141fd2bb5466b590907aedede9a1')
utxo_index = 0 # index of the output you are spending, indices start at 0
######################################################################

txin_scriptPubKey = Q2a_txout_scriptPubKey
######################################################################
# TODO: implement the scriptSig for redeeming the transaction created
# in  Exercise 2a.
txin_scriptSig = [
        8,  # x
        4 # y
]
######################################################################
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network_type)
print(response.status_code, response.reason)
print(response.text)


# @binhminh28 ➜ /workspaces/Lab-2.a-Bitcoin-transaction (main) $ python Q2b.py 
# 201 Created
# {
#   "tx": {
#     "block_height": -1,
#     "block_index": -1,
#     "hash": "7f7564f715fbd6f927e8a7cc983e17542e97f327fe6e71f5fc1532925fcc83b8",
#     "addresses": [
#       "mohjSavDdQYHRYXcS3uS6ttaHP8amyvX78"
#     ],
#     "total": 8000,
#     "fees": 2000,
#     "size": 87,
#     "vsize": 87,
#     "preference": "low",
#     "relayed_by": "23.97.62.118",
#     "received": "2025-11-10T15:48:04.335096252Z",
#     "ver": 1,
#     "double_spend": false,
#     "vin_sz": 1,
#     "vout_sz": 1,
#     "confirmations": 0,
#     "inputs": [
#       {
#         "prev_hash": "0eef8dbd8920bb85c9a2aa359b12b2dab6b6141fd2bb5466b590907aedede9a1",
#         "output_index": 0,
#         "script": "5854",
#         "output_value": 10000,
#         "sequence": 4294967295,
#         "script_type": "unknown",
#         "age": 0
#       }
#     ],
#     "outputs": [
#       {
#         "value": 8000,
#         "script": "76a91459cada50314c829e19f5a7786f8ee0d4987f429d88ac",
#         "addresses": [
#           "mohjSavDdQYHRYXcS3uS6ttaHP8amyvX78"
#         ],
#         "script_type": "pay-to-pubkey-hash"
#       }
#     ]
#   }
# }