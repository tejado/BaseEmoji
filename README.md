# BaseEmoji

BaseEmoji is a python module for encoding any ASCII string or byte object into emoticons and back. It can be used to hide information in text conversations, e.g. chat or twitter or to display hashes in a graphica/more comparable way.  
It supports two codecs: anybase and group256. This module is also the reference implementation of these two codecs.

Made with ❤️ at 36c3!

## Install
```bash
pip install emojibase
```
View on PyPi via [https://pypi.org/project/emojibase/](https://pypi.org/project/emojibase/)

## Usage

### anybase
anybase is a BaseEmoji codec which works by converting the input to the base of the amount of emojis, set by the filter. 

```python
import BaseEmoji

e = BaseEmoji.anybase()
e.encode('giv mee emojiiis'.encode())
# ✴️🥎🐑⛈️🈺🚉‭⚕️🚅🇵🇪🥏🥇📍

e.decode('✴️🥎🐑⛈️🈺🚉‭⚕️🚅🇵🇪🥏🥇📍').decode('ascii')
# giv mee emojiiis

```

### group256
This codec distributes all (filtered) emojis to 256 groups. With this, it can encode any ASCII string to emojis.

```python
import BaseEmoji

e = BaseEmoji.group256()
e.encode('giv mee emojiiis')
# 😸😻💖🤨😿🤖🥔🐢🕢🧅🙈😼🥒🕤💸💌

e.decode('😸😻💖🤨😿🤖🥔🐢🕢🧅🙈😼🥒🕤💸💌')
# giv mee emojiiis

```

### Filters
There are currently three filter options for changing the emojis for en/decoding:
- Groups (e.g. flags)
- Skin Tone Support
- Unicode Version

```python
e.set_filter(['Symbols'], False, 12.0)
e.encode('giv mee symbol emojiiis'.encode())
# 📛⭕✳️⬅️✖️⚜️⚜️⬅️➰‼️✖️⚕️❎✔️⬅️⚜️✖️❎✅⭕⭕⭕➰

e.get_groups()
# {'Smileys & Emotion', 'Travel & Places', 'Activities', 'Flags', 'Animals & Nature', 'Symbols', 'People & Body', 'Objects', 'Food & Drink'}
```

## Roadmap
- Add filter options to encoded data for automatic decoding

## Credits
- Inspired by [CuteUID](https://github.com/alexdredmon/cuteuid)
- Emoji data from [muan](https://github.com/muan/unicode-emoji-json)
- [Jonas](https://github.com/jonas-koeritz)
