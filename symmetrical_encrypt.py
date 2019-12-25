#!/usr/bin/python3
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Hash import MD5
from Crypto import Random


def transform_secret_key(key):
    h = MD5.new()
    h.update(key.encode())
    return h.hexdigest()

def symmetrical_encrypt(message, key, verbose=True):
    key_md5 = transform_secret_key(key)
    message_hash = SHA256.new(message.encode())
    add_hash = message.encode() + message_hash.hexdigest().encode()
    vector = Random.new().read(AES.block_size)
    cipher = AES.new(key_md5, AES.MODE_CFB, vector)
    encrypted_message = vector + cipher.encrypt(add_hash)
    if verbose:
        print(f'Message was encrypted: {encrypted_message.hex()}')
    return encrypted_message

def symmetrical_decrypt(encrypted_message, key):
    key_md5 = transform_secret_key(key)
    bsize = AES.block_size
    dsize = SHA256.digest_size*2
    vector = Random.new().read(bsize)
    cipher = AES.new(key_md5, AES.MODE_CFB, vector)
    decrypted_message_with_hash = cipher.decrypt(encrypted_message)[bsize:]
    decrypted_message = decrypted_message_with_hash[:-dsize]
    digest = SHA256.new(decrypted_message).hexdigest()
    if digest == decrypted_message_with_hash[-dsize:].decode():
        print(
            f"""
            Encrypted hash: {decrypted_message_with_hash[-dsize:].decode()}\n
            Decripted hash is: {digest}
            """
        )
        return decrypted_message.decode()
    else:
        print(
            f"""
            Encrypted was not correct. Encrypted hash: 
            {decrypted_message_with_hash[-dsize:].decode()}\n
            Decripted hash is: {digest}
            """
        )

