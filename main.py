#!/usr/bin/python3
import rsa
from DiffieHellman import KeyPair, SecretKey
from symmetrical_encrypt import symmetrical_encrypt, symmetrical_decrypt


alice = KeyPair()
bob = KeyPair()

(alice.publicRSA, alice.privateRSA) = rsa.newkeys(512)
(bob.publicRSA, bob.privateRSA) = rsa.newkeys(512)

# alice send her DH public key to bob
encrypted = rsa.encrypt(str(alice.public).encode(), bob.publicRSA) # alice encrypt her public DH key
decrypted = rsa.decrypt(encrypted, bob.privateRSA) # bob decrypt alice's public DH key
bob.secret = SecretKey(bob.private, int(decrypted))

# bob send his DH public key to alice
encrypted = rsa.encrypt(str(bob.public).encode(), alice.publicRSA) # bob encrypt his public DH key
decrypted = rsa.decrypt(encrypted, alice.privateRSA) # alice decrypt bob's public DH key
alice.secret = SecretKey(alice.private, int(decrypted))

message = "Hello Bob"
# alice send message to bob
encrypted_message = symmetrical_encrypt(message, str(alice.secret.secret))
# bob decrypt message
decrypted_message = symmetrical_decrypt(encrypted_message, str(bob.secret.secret))
print(decrypted_message)
