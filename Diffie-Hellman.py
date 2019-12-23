#!/usr/bin/python3
"""Diffie-Hellman crypto protocol"""
import random


class KeyPair:
    g = 11
    p = random.randint(2**16, 2**32)

    def __init__(self):
        self.private = random.randint(2**16, 2**18)
        print('private key: ', self.private)
        self.public = self.get_mod
        print('public key: ', self.public)

    @property
    def get_mod(self):
        return (self.g ** self.private) % self.p

class SecretKey:
    p = KeyPair.p

    def __init__(self, private, public):
        self.secret = (public ** private) % self.p


alice = KeyPair()
bob = KeyPair()

alice.secret = SecretKey(alice.private, bob.public)
print('alice secret key: ', alice.secret.secret)
bob.secret = SecretKey(bob.private, alice.public)
print('bob secret key: ', bob.secret.secret)

print(alice.secret.secret == bob.secret.secret)
exit(0)
