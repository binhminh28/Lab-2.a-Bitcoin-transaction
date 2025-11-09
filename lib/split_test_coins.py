# lib/split_test_coins.py
from bitcoin import SelectParams
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from bitcoin.core import CMutableTransaction, COIN
from bitcoin.core.script import CScript, SignatureHash, SIGHASH_ALL
from bitcoin.core.scripteval import VerifyScript, SCRIPT_VERIFY_P2SH

from config import my_private_key, my_public_key, my_address, network_type
from utils import create_txin, create_txout, broadcast_transaction

def split_coins(total_input_satoshi, txid_to_spend, utxo_index, n, network, fee_satoshi=500):

    if total_input_satoshi <= fee_satoshi:
        raise ValueError("UTXO quá nhỏ so với phí!")

    amount_per_output_satoshi = (total_input_satoshi - fee_satoshi) // n
    if amount_per_output_satoshi <= 0:
        raise ValueError("Số lượng output quá nhiều so với số tiền trong UTXO!")

    amount_per_output_btc = amount_per_output_satoshi / COIN 

    txin = create_txin(txid_to_spend, utxo_index)

    txout_scriptPubKey = my_address.to_scriptPubKey()
    txout_list = [create_txout(amount_per_output_btc, txout_scriptPubKey) for _ in range(n)]

    tx = CMutableTransaction([txin], txout_list)

    txin_scriptPubKey = my_address.to_scriptPubKey() 
    
    sighash = SignatureHash(txin_scriptPubKey, tx, 0, SIGHASH_ALL)
    txin.scriptSig = CScript([
        my_private_key.sign(sighash) + bytes([SIGHASH_ALL]),
        my_public_key
    ])

    VerifyScript(txin.scriptSig, txin_scriptPubKey, tx, 0, (SCRIPT_VERIFY_P2SH,))

    print("Đang broadcast giao dịch...")
    response = broadcast_transaction(tx, network)
    print(response.status_code, response.reason)
    print(response.text)


if __name__ == '__main__':
    SelectParams('testnet')

    total_input_satoshi = 150_548
    txid_to_spend = 'd44c0c67f0d1292e711b0e075537102f205c07b2f79190dfee246f281f68a155'
    utxo_index = 0
    n = 5
    fee_satoshi = 500 

    split_coins(total_input_satoshi, txid_to_spend, utxo_index, n, network_type, fee_satoshi)



# 201 Created
# {
#   "tx": {
#     "block_height": -1,
#     "block_index": -1,
#     "hash": "8f3a2585ff47b0f9116cc69da2a35e5605c987c6cacbbae40cb6787d056ffa60",
#     "addresses": [
#       "mpqgD4LbdPTvZTVPAH2JhZ6SCunVsDxsGz"
#     ],
#     "total": 150040,
#     "fees": 508,
#     "size": 327,
#     "vsize": 327,
#     "preference": "low",
#     "relayed_by": "23.97.62.116",
#     "received": "2025-11-09T18:11:20.976433857Z",
#     "ver": 1,
#     "double_spend": false,
#     "vin_sz": 1,
#     "vout_sz": 5,
#     "confirmations": 0,
#     "inputs": [
#       {
#         "prev_hash": "d44c0c67f0d1292e711b0e075537102f205c07b2f79190dfee246f281f68a155",
#         "output_index": 0,
#         "script": "47304402206b4103c9fedd34aa9f89299243cf2a8222dbe1e5c1f7a7b1419b15004fe77b7802201396fed72db64f9982b4391e4f899dc093fe1cb45125ae24c93e892b8ad453f7012103619d3ab10a627c73547a37b4fe54de29d0b1318cac253ad70f4dab8c796ce099",
#         "output_value": 150548,
#         "sequence": 4294967295,
#         "addresses": [
#           "mpqgD4LbdPTvZTVPAH2JhZ6SCunVsDxsGz"
#         ],
#         "script_type": "pay-to-pubkey-hash",
#         "age": 4755702
#       }
#     ],
#     "outputs": [
#       {
#         "value": 30008,
#         "script": "76a91466439b781840806d0e92547e83f309838d1de45488ac",
#         "addresses": [
#           "mpqgD4LbdPTvZTVPAH2JhZ6SCunVsDxsGz"
#         ],
#         "script_type": "pay-to-pubkey-hash"
#       },
#       {
#         "value": 30008,
#         "script": "76a91466439b781840806d0e92547e83f309838d1de45488ac",
#         "addresses": [
#           "mpqgD4LbdPTvZTVPAH2JhZ6SCunVsDxsGz"
#         ],
#         "script_type": "pay-to-pubkey-hash"
#       },
#       {
#         "value": 30008,
#         "script": "76a91466439b781840806d0e92547e83f309838d1de45488ac",
#         "addresses": [
#           "mpqgD4LbdPTvZTVPAH2JhZ6SCunVsDxsGz"
#         ],
#         "script_type": "pay-to-pubkey-hash"
#       },
#       {
#         "value": 30008,
#         "script": "76a91466439b781840806d0e92547e83f309838d1de45488ac",
#         "addresses": [
#           "mpqgD4LbdPTvZTVPAH2JhZ6SCunVsDxsGz"
#         ],
#         "script_type": "pay-to-pubkey-hash"
#       },
#       {
#         "value": 30008,
#         "script": "76a91466439b781840806d0e92547e83f309838d1de45488ac",
#         "addresses": [
#           "mpqgD4LbdPTvZTVPAH2JhZ6SCunVsDxsGz"
#         ],
#         "script_type": "pay-to-pubkey-hash"
#       }
#     ]
#   }
# }