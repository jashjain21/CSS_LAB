from Crypto.PublicKey import RSA

key = RSA.generate(2048)

binPrivKey = key.exportKey('DER')
binPubKey =	key.publickey().exportKey('DER')

print(binPrivKey[:100])

print(binPubKey[:100])
