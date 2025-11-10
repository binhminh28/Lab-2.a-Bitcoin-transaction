from os import urandom
from bitcoin import SelectParams
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

SelectParams('testnet')

seckey = CBitcoinSecret.from_secret_bytes(urandom(32))

print("Private key: %s" % seckey)
print("Address: %s" %
      P2PKHBitcoinAddress.from_pubkey(seckey.pub))


# @binhminh28 ➜ /workspaces/Lab-2.a-Bitcoin-transaction (main) $ python lib/keygen.py 
# Private key: cT2gHkzAfuc7ikXeD4kstcPykiGCPu3iBoXHiacYLoNqid5SKTLC
# Address: mpqgD4LbdPTvZTVPAH2JhZ6SCunVsDxsGz
# Transaction: d44c0c67f0d1292e711b0e075537102f205c07b2f79190dfee246f281f68a155


# 1
# @binhminh28 ➜ /workspaces/Lab-2.a-Bitcoin-transaction (main) $ python lib/keygen.py 
# Private key: cNrDvCDrJrmpnjVMhZSLonyGdXUymruk2gHS45ZRWgvQjoWzw9rg
# Address: msgUcdXE1spqadAswyUobizkTZFZX2pRsh

# 2
# @binhminh28 ➜ /workspaces/Lab-2.a-Bitcoin-transaction (main) $ python lib/keygen.py 
# Private key: cPjhAaUck8jhLWbECpYVR3woXkzNiTj8zxYWwmtqHbghPJoTarTA
# Address: n2HSfDyK4qQQZcJbrCzgAAv2CBsT19gLCF

# 3
# @binhminh28 ➜ /workspaces/Lab-2.a-Bitcoin-transaction (main) $ python lib/keygen.py 
# Private key: cTg9dN3RxmpVfkBCUmHQ7fz12jNy4PuwUoqLD4tCP5QBRFYQn8qz
# Address: mmoM9YhyP56wTsCpCup1mhRuYeqdEnsP8Q