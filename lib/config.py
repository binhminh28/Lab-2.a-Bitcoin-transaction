from bitcoin import SelectParams
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress, CBitcoinAddress

SelectParams('testnet')

faucet_address = CBitcoinAddress('mohjSavDdQYHRYXcS3uS6ttaHP8amyvX78')

network_type = 'btc-test3'

my_private_key = CBitcoinSecret('cT2gHkzAfuc7ikXeD4kstcPykiGCPu3iBoXHiacYLoNqid5SKTLC')
my_public_key = my_private_key.pub
my_address = P2PKHBitcoinAddress.from_pubkey(my_public_key)
