#!/usr/bin/python3
"""Diffie-Hellman crypto protocol"""
import random


class KeyPair:
    g = 11
    p = random.randint(2**16, 2**32)

    def __init__(self):
        self.private = random.randint(2**16, 2**18)
        # print('private key: ', self.private)
        self.public = (self.g ** self.private) % self.p
        # print('public key: ', self.public)


class SecretKey:
    p = KeyPair.p

    def __init__(self, private, public):
        self.secret = (public ** private) % self.p


# alice = KeyPair()
# bob = KeyPair()

# alice.secret = SecretKey(alice.private, bob.public)
# print('alice secret key: ', alice.secret.secret)
# bob.secret = SecretKey(bob.private, alice.public)
# print('bob secret key: ', bob.secret.secret)
