import BaseEmoji
import hashlib

def hash_string(string):
    """
    Returns hex and binary SHA-256 hash of given string
    """
    h = hashlib.sha256( string.encode('utf-8') )
    return ( h.hexdigest(), h.digest() )

hash_hex, hex_bin = hash_string('some test string to hash')

e = BaseEmoji.anybase()
hash_emoji = e.encode( hex_bin )

print( "hash - hex: {}".format(hash_hex) )
print( "hash - emoji: {}".format(hash_emoji) )