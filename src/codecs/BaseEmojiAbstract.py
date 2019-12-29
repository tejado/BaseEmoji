import regex

class BaseEmojiAbstract(object):

    def __init__(self, emojis):
        self.all_emojis = emojis
        self.filtered_emojis = {}

        self.set_filter()

    def filter_emojis(self, groups, skin_tone_support, version):
        elist = []
        for emoji, emoji_info in self.all_emojis.items():
            if (
                    emoji_info['unicode_version'] <= version and 
                    (not groups or emoji_info['group'] in groups) and
                    (skin_tone_support == True or emoji_info['skin_tone_support'] == False)
               ):
                elist.append(emoji)
        return elist
    
    def get_filter(self):
        return (self.filter_groups, self.skin_tone_support, self.unicode_version)

    def set_filter(self, groups = [], skin_tone_support = False, version = 12.0):
        self.filter_groups = groups
        self.skin_tone_support = skin_tone_support
        self.unicode_version = version

        self.filtered_emojis = self.filter_emojis(self.filter_groups, self.skin_tone_support, self.unicode_version)
        self.init()
    
    def get_groups(self):
        groups = set()
        for emoji in self.all_emojis:
            groups.add( self.all_emojis[emoji]['group'] )
        return groups

    def init(self):
        raise NotImplementedError()

    def get_glyphs(self, string):
        return regex.findall(r'\X', string)

    def encode(self, data):
        raise NotImplementedError()

    def decode(self, data):
        raise NotImplementedError()
    