import os
import sys
import json
from .codecs import *
from collections import OrderedDict

class BaseEmoji:

    def __init__(self):
        self.emoji_file = '{}/data/emojis.json'.format(os.path.dirname(__file__))
        self.all_emojis = self.load_emojis(self.emoji_file)

    def load_emojis(self, file): 
        with open(self.emoji_file, encoding='utf-8') as fs:
            emoji_json = json.load(fs, object_pairs_hook=OrderedDict)
        return emoji_json

    def __getattr__(self, func):
        def function():
            r = globals()[func]
            return getattr(r, func)( self.all_emojis )

        if 'BaseEmoji.codecs.{}'.format(func) in  sys.modules:
            return function
        else:
            raise AttributeError

sys.modules[__name__] = BaseEmoji()