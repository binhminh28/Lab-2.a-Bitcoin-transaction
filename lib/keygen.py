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
