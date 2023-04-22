#!/usr/bin/python3

import os

filename = os.path.basename(__file__)
# 你可以躲在角落选择沉默
textStr = '你可以躲在角落选择沉默，但是不要嘲笑甚至诋毁比你勇敢的人，因为他们争取到的光明也会照耀到你。今日我若冷眼旁观，他日祸临己身，则无人为我摇旗呐喊。'
voiceArr = ['YunjianNeural']

for v in voiceArr:
  shell = f'edge-tts --text {textStr} --voice zh-CN-{v} --write-media ./audios/{filename}.{v}.mp3'
  os.system(shell)
