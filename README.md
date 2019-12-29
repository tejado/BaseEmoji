# BaseEmoji

Encode any data to emojis

Inspired by [CuteUID](https://github.com/alexdredmon/cuteuid).  
Emoji data by [muan](https://github.com/muan/unicode-emoji-json).

## Usage

### anybase
```python
import baseemoji

e = BaseEmoji.anybase()
print( e.encode('giv mee emojiiis'.encode()) )
# ✴️🥎🐑⛈️🈺🚉‭⚕️🚅🇵🇪🥏🥇📍

print( e.decode('✴️🥎🐑⛈️🈺🚉‭⚕️🚅🇵🇪🥏🥇📍').decode('ascii') )
# giv mee emojiiis

```

### group256
```python
import baseemoji

e = BaseEmoji.group256()
print( e.encode('giv mee emojiiis') )
# 😸😻💖🤨😿🤖🥔🐢🕢🧅🙈😼🥒🕤💸💌

print( e.decode('😸😻💖🤨😿🤖🥔🐢🕢🧅🙈😼🥒🕤💸💌'))
# giv mee emojiiis

```

### Filters
There are currently three filter options for changing the emojis for en/decoding:
- Groups (e.g. flags)
- Skin Tone Support
- Unicode Version

```python
e.set_filter(['Flags'], False, 12.0)
print( e.encode('giv mee emojiiis'.encode()) )
# 🇪🇬🇦🇬🇬🇷🇭🇺🇨🇽🇦🇲🇰🇵🇰🇳⁣🇪🇨🇲🇵🇮🇳🇧🇱🇪🇷🇦🇱🇨🇭🏴󠁧󠁢󠁷󠁬󠁳󠁿

print( e.decode('🇪🇬🇦🇬🇬🇷🇭🇺🇨🇽🇦🇲🇰🇵🇰🇳⁣🇪🇨🇲🇵🇮🇳🇧🇱🇪🇷🇦🇱🇨🇭🏴󠁧󠁢󠁷󠁬󠁳󠁿').decode('ascii') )
# giv mee emojiiis

e.get_groups()
# {'Smileys & Emotion', 'Travel & Places', 'Activities', 'Flags', 'Animals & Nature', 'Symbols', 'People & Body', 'Objects', 'Food & Drink'}
```

## Roadmap
- Change filter settings
- Add filter options to encoded data for automatic decoding