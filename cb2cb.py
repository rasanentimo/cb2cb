import time
import argparse
import pyglet
import os
from cleverbot import Cleverbot
from gtts import gTTS
from langdetect import detect

cb1 = Cleverbot()
cb2 = Cleverbot()
bot1 = 'Bot1'
bot2 = 'Bot2'

parser = argparse.ArgumentParser()
parser.add_argument('fq', help="The first question for the discussion")
args = parser.parse_args()  
statement = str(args.fq)

lang_list = ['af', 'ar', 'bn', 'ca', 'cs', 'cy', 'da', 'de', 'el', 'en', 
'en-au', 'en-uk', 'en-us', 'eo', 'es', 'es-es', 'es-us', 'fi', 'fr', 'hi',
'hr', 'hu', 'hy', 'id', 'is', 'it', 'ja', 'ko', 'la', 'lv', 'mk','nl', 'no',
'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'sq', 'sr', 'sv', 'sw', 'ta', 'th', 
'tr', 'vi', 'zh', 'zh-cn','zh-tw', 'zh-yue']

i = 1
try:
    while True:
        try:
            lang_detect = detect(statement)
        except:
            lang_detect = 'en'
            pass
        if lang_detect not in lang_list:
            lang_detect = 'en'
        file = 'temp.mp3'
        tts = gTTS(text=statement, lang=lang_detect)
        tts.save(file)
        speech = pyglet.media.load(file)
        speech.play()
        print('{0:03d}.\t{1}: {2}, {3}'.format(i, bot1, statement, lang_detect))
        statement = cb2.ask(statement)
        cb1, cb2 = cb2, cb1
        bot1, bot2 = bot2, bot1
        time.sleep(3)
        i+=1
        os.remove(file)
except KeyboardInterrupt:
    os.remove(file)
    exit