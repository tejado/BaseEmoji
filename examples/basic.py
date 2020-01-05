import BaseEmoji

example_string = 'giv mee emojiiis'

e = BaseEmoji.anybase()
emoji_encoded = e.encode( example_string.encode('utf-8') )
emoji_decoded = e.decode(emoji_encoded)
print( "anybase encoded: {}".format(emoji_encoded) )
print( "anybase decoded: {}".format(emoji_decoded.decode('ascii')) )
print()


e = BaseEmoji.group256()
emoji_encoded = e.encode( example_string )
emoji_decoded = e.decode(emoji_encoded)
print( "group256 encoded: {}".format(emoji_encoded) )
print( "group256 decoded: {}".format(emoji_decoded) )
print()


e.set_filter(['Symbols'], False, 12.0)
emoji_encoded_symbols = e.encode('giv mee symbol emojiiis')
print( "group256 encoded - symbols only: {}".format(emoji_encoded_symbols) )
print( "all emoji groups: {}".format(e.get_groups()) )