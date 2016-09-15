# cb2cb
## Cleverbot Chat

This is a script which makes two Cleverbots (http://www.cleverbot.com/) to chat with each other. The script uses Google text to speech (https://github.com/pndurette/gTTS). The chat doesn't make much sense most of times but it can be entertaining.

Requires following modules:
* argparse
* pyglet
* cleverbot
* gtts
* langdetect

example;

```
$ python3.5 cb2cb.py "Who are you?"
001.   	Bot1: Who are you?, en
002.   	Bot2: I don't know., en
003.   	Bot1: Why don't you know?, en
004.   	Bot2: The truth about life., en
005.   	Bot1: Do you enjoy your life?, es
006.   	Bot2: Are you a boy or a girl?, tr
007.   	Bot1: I won't tell you., en
008.   	Bot2: At this point it does not matter multiple possibilities render names useless., en
009.   	Bot1: Probably not. Most things don't., en
010.   	Bot2: Novia perfecta te amoooo., pt
011.   	Bot1: What do you think is a perfecrt night., en
012.   	Bot2: I am not sure right now., en
013.   	Bot1: What do you want me to be?, en
014.   	Bot2: Get Samantha phone number from the phone book., en
```

Tested only on OSX.
