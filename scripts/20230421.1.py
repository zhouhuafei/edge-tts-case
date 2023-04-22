#!/usr/bin/python3

import os

filename = os.path.basename(__file__)
# 如果鲁迅也炒股
textStr = '我家门前有两棵树，一棵是绿枣树，另一棵也是绿枣树。'
voiceArr = ['YunjianNeural']

for v in voiceArr:
  shell = f'edge-tts --text {textStr} --voice zh-CN-{v} --write-media ./audios/{filename}.{v}.mp3'
  os.system(shell)
