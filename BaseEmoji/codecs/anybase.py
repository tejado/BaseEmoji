"""
BaseEmoji
Copyright (c) 2019 tjado <https://github.com/tejado>

anybase codec
Emoji encoding/decoding by base conversion
"""

from .BaseEmojiAbstract import BaseEmojiAbstract

class anybase(BaseEmojiAbstract):
    def __init__(self, emojis):
        super(anybase, self).__init__(emojis)

    def init(self):
        self.block_size = 8
        self.emoji_base = len(self.filtered_emojis)
        self.delimiters = ['\u200b', '\u200c', '\u200d', '\u200e', '\u202a', '\u202c', '\u202d', '\u2062', '\u2063', '\uFEFF']

    def base(self, number, base_input, base_output):
        if not isinstance(number, list):
            number = list(int(i) for i in str(number))
        return self.from_base10(self.to_base10(number, base_input), base_output)

    def from_base10(self, number, base_output):
        digits = []
        while number:
            number, r = divmod(number, base_output)
            digits.append(r)

        if base_output == 10:
            return ''.join(map(str,digits[::-1]))
        return digits[::-1]

    def to_base10(self, numbers, base_input):
        if not isinstance(numbers, list):
            raise TypeError('numbers must be a list')
        return sum(v * base_input ** k for k, v in enumerate(numbers[::-1]))
    
    def pad(self, data_to_pad):
        padding_len = (self.block_size - len(data_to_pad)) % self.block_size
        padding = chr(padding_len) * padding_len
        return data_to_pad + padding.encode()

    def unpad(self, padded_data):
        pdata_len = len(padded_data)
        if pdata_len % self.block_size:
            raise ValueError("Input data is not padded.")

        padding_len = padded_data[-1]
        if padding_len < 1 or padding_len > min(self.block_size, pdata_len):
            return padded_data
        if padded_data[-padding_len:] != (chr(padding_len) * padding_len).encode():
            raise ValueError("Padding is incorrect.")

        return padded_data[:-padding_len]

    def encode(self, data):
        if not isinstance(data, bytes):
            raise TypeError("data must be a byte-object")

        output = ''
        data = self.pad(data)

        for i in range(0, len(data), self.block_size):
            block = data[i:i + self.block_size]
            converted_block = self.base(int.from_bytes(block, "big"), 10, self.emoji_base)
            
            # if this fails, we neeed more unicode zero-width chars in self.delimiters
            output += self.delimiters[len(converted_block)]
            for j in converted_block:
                output += self.filtered_emojis[j]

        return output

    def decode(self, data):
        glyphs = self.get_glyphs(data)
        output = b''

        chunks = []
        num_emojis = 0

        for glyph in glyphs:
            if glyph in self.delimiters:
                num_emojis = self.delimiters.index(glyph)
            else:
                chunks.append(self.filtered_emojis.index(glyph))

            if len(chunks) == num_emojis:
                block = b''
                if len(chunks) > 0:
                    base10_block = self.base(chunks, self.emoji_base, 10)
                    block = int(base10_block).to_bytes(8, 'big')

                block = block.rjust(self.block_size, b'\x00')
                output += block
                chunks = []
        
        output = self.unpad(output)
        return output
    