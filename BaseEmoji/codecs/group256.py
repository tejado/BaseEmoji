"""
BaseEmoji
Copyright (c) 2019 tjado <https://github.com/tejado>

group256 codec
Emoji encoding/decoding by grouping all emojis into ascii range
"""

from .BaseEmojiAbstract import BaseEmojiAbstract

class group256(BaseEmojiAbstract):
    def __init__(self, emojis):
        super(group256, self).__init__(emojis)

    def init(self):
        self.emap = {}
        self.num_chunks = 256

        for chunk in range(0, self.num_chunks):
            self.emap[chunk] = self.filtered_emojis[chunk::self.num_chunks]
        
    def encode(self, data):
        if not isinstance(data, str):
            raise TypeError("data must be a string")

        dedup = [0] * self.num_chunks
        output = ''

        for char in data:
            char = ord(char)
            if char > 256:
                raise TypeError('group256 codec only supports ascii (found char "{}")'.format(char))

            output += self.emap[char][dedup[char]]
            dedup[char] += 1
            
            # start from beginning if all emojis are used from chunk
            if dedup[char] >= len(self.emap[char]):
                dedup[char] = 0
            
        return output

    def decode(self, data):
        glyphs = self.get_glyphs(data)
        output = ''
        for glyph in glyphs:
            found = False
            for id, chunk in self.emap.items():
                if glyph in chunk:
                    output += chr(id)
                    found = True
                    break
            
            if not found:
                print('Error: {} not found'.format(glyph))
        
        return output
    