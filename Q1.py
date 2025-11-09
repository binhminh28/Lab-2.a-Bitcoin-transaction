from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)


def P2PKH_scriptPubKey(address):
    ######################################################################
    # TODO: Complete the standard scriptPubKey implementation for a
    # PayToPublicKeyHash transaction
    return [
        OP_DUP,
        OP_HASH160,
        address,
        OP_EQUALVERIFY,
        OP_CHECKSIG
    ]
    ######################################################################


def P2PKH_scriptSig(txin, txout, txin_scriptPubKey, private_key, public_key):
    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             private_key)
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was sent to you
    # in the PayToPublicKeyHash transaction.
    return [
        signature,
        public_key
    ]
    ######################################################################

def send_from_P2PKH_transaction(amount_to_send,
                                txid_to_spend,
                                utxo_index,
                                txout_scriptPubKey,
                                sender_private_key,
                                network):

    sender_public_key = sender_private_key.pub
    sender_address = P2PKHBitcoinAddress.from_pubkey(sender_public_key)

    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin_scriptPubKey = P2PKH_scriptPubKey(sender_address)
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = P2PKH_scriptSig(txin, txout, txin_scriptPubKey,
        sender_private_key, sender_public_key)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx, network)


if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0002 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '8f3a2585ff47b0f9116cc69da2a35e5605c987c6cacbbae40cb6787d056ffa60')
    utxo_index = 0 # index of the output you are spending, indices start at 0
    ######################################################################

    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)
    response = send_from_P2PKH_transaction(
        amount_to_send,
        txid_to_spend,
        utxo_index,
        txout_scriptPubKey,
        my_private_key,
        network_type,
    )
    print(response.status_code, response.reason)
    print(response.text)


# 201 Created
# {
#   "tx": {
#     "block_height": -1,
#     "block_index": -1,
#     "hash": "40ea98c0160d3cc65f98ad615a39b86fa43887c0734bdc78fb5f339c23b3fc25",
#     "addresses": [
#       "mpqgD4LbdPTvZTVPAH2JhZ6SCunVsDxsGz",
#       "mohjSavDdQYHRYXcS3uS6ttaHP8amyvX78"
#     ],
#     "total": 20000,
#     "fees": 10008,
#     "size": 191,
#     "vsize": 191,
#     "preference": "low",
#     "relayed_by": "23.97.62.116",
#     "received": "2025-11-09T18:29:07.541520446Z",
#     "ver": 1,
#     "double_spend": false,
#     "vin_sz": 1,
#     "vout_sz": 1,
#     "confirmations": 0,
#     "inputs": [
#       {
#         "prev_hash": "8f3a2585ff47b0f9116cc69da2a35e5605c987c6cacbbae40cb6787d056ffa60",
#         "output_index": 0,
#         "script": "47304402206122029e541969937174a4e809a3c9cb46b21359d179edf6924039c721b1449802203afc1b06eb3ed3dea2fe958d6e0cda90811f62060a637c37d7169df11908c44c012103619d3ab10a627c73547a37b4fe54de29d0b1318cac253ad70f4dab8c796ce099",
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
#         "value": 20000,
#         "script": "76a91459cada50314c829e19f5a7786f8ee0d4987f429d88ac",
#         "addresses": [
#           "mohjSavDdQYHRYXcS3uS6ttaHP8amyvX78"
#         ],
#         "script_type": "pay-to-pubkey-hash"
#       }
#     ]
#   }
# }