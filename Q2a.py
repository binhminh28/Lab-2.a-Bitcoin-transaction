from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


first_half_suid = 12    # x + y = 12
second_half_suid = 4    # x - y = 4
######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2
Q2a_txout_scriptPubKey = [
    OP_2DUP,        
    OP_ADD,        
    first_half_suid,
    OP_EQUALVERIFY, 
    OP_SUB,        
    second_half_suid,
    OP_EQUAL  
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0001 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '8f3a2585ff47b0f9116cc69da2a35e5605c987c6cacbbae40cb6787d056ffa60')
    utxo_index = 2 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q2a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)

# @binhminh28 ➜ /workspaces/Lab-2.a-Bitcoin-transaction (main) $ python Q2a.py 
# 201 Created
# {
#   "tx": {
#     "block_height": -1,
#     "block_index": -1,
#     "hash": "0eef8dbd8920bb85c9a2aa359b12b2dab6b6141fd2bb5466b590907aedede9a1",
#     "addresses": [
#       "mpqgD4LbdPTvZTVPAH2JhZ6SCunVsDxsGz"
#     ],
#     "total": 10000,
#     "fees": 20008,
#     "size": 173,
#     "vsize": 173,
#     "preference": "high",
#     "relayed_by": "23.97.62.118",
#     "received": "2025-11-10T15:47:11.475893976Z",
#     "ver": 1,
#     "double_spend": false,
#     "vin_sz": 1,
#     "vout_sz": 1,
#     "confirmations": 0,
#     "inputs": [
#       {
#         "prev_hash": "8f3a2585ff47b0f9116cc69da2a35e5605c987c6cacbbae40cb6787d056ffa60",
#         "output_index": 2,
#         "script": "473044022035f50189ede51280120e03a074b89113bd975ce2bdd5e9aad9b42ed43effad5d0220673e06af48820a69cf9998bb26980d03ff5ceaf6d10f057574858a219de6ab8e012103619d3ab10a627c73547a37b4fe54de29d0b1318cac253ad70f4dab8c796ce099",
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
#         "script": "6e935c88945487",
#         "addresses": null,
#         "script_type": "unknown"
#       }
#     ]
#   }
# }