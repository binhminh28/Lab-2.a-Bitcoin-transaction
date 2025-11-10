from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import P2PKH_scriptPubKey
from Q3a import (Q3a_txout_scriptPubKey, cust1_private_key, cust2_private_key,
                  cust3_private_key)


def multisig_scriptSig(txin, txout, txin_scriptPubKey):
    bank_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             my_private_key)
    cust1_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust1_private_key)
    cust2_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust2_private_key)
    cust3_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust3_private_key)
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was locked in the
    # multisig transaction created in Exercise 3a.
    return [
        OP_0, 
        cust1_sig,
        bank_sig
    ]
    ######################################################################


def send_from_multisig_transaction(amount_to_send, txid_to_spend, utxo_index,
                                   txin_scriptPubKey, txout_scriptPubKey, network):
    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = multisig_scriptSig(txin, txout, txin_scriptPubKey)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx, network)

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00008 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '54480c1b10eed54d6cf2eed6c7609e41fbe3af91e37f64f7039902c5af844ca0')
    utxo_index = 0 # index of the output you are spending, indices start at 0
    ######################################################################

    txin_scriptPubKey = Q3a_txout_scriptPubKey
    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

    response = send_from_multisig_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        txin_scriptPubKey, txout_scriptPubKey, network_type)
    print(response.status_code, response.reason)
    print(response.text)

# @binhminh28 ➜ /workspaces/Lab-2.a-Bitcoin-transaction (main) $ python Q3b.py 
# 201 Created
# {
#   "tx": {
#     "block_height": -1,
#     "block_index": -1,
#     "hash": "5b4771342206583b2cfa150bdaa082e31ecc4a266b80fc2e2a9ceedb83d2a8b8",
#     "addresses": [
#       "zPAaS6VMLTihpuH69rpyMUNrn9z6N3nTbp",
#       "mohjSavDdQYHRYXcS3uS6ttaHP8amyvX78"
#     ],
#     "total": 8000,
#     "fees": 2000,
#     "size": 230,
#     "vsize": 230,
#     "preference": "low",
#     "relayed_by": "23.97.62.118",
#     "received": "2025-11-10T16:04:07.743534987Z",
#     "ver": 1,
#     "double_spend": false,
#     "vin_sz": 1,
#     "vout_sz": 1,
#     "confirmations": 0,
#     "inputs": [
#       {
#         "prev_hash": "54480c1b10eed54d6cf2eed6c7609e41fbe3af91e37f64f7039902c5af844ca0",
#         "output_index": 0,
#         "script": "004730440220275dfc5a8962faecb6331ea67d5dba387aa2c3bf28a98f96385d59483d4aac8702204f6adf693ad90adff4a89ab72b3b4f716ae4cebb1637f9343a360d6ecdf7ce2a014730440220225a0151b04d0ee203e7c2f2c4302096992cf6176c250d16495054d291c58c56022059a10ef543d4eef455af61a7986a79c29229db3ca3802f17153cc99ae00d6abd01",
#         "output_value": 10000,
#         "sequence": 4294967295,
#         "addresses": [
#           "zPAaS6VMLTihpuH69rpyMUNrn9z6N3nTbp"
#         ],
#         "script_type": "pay-to-multi-pubkey-hash",
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