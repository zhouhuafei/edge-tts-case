#!/usr/bin/python3

import os

filename = os.path.basename(__file__)
# 如果祥林嫂也炒股
textStr = '我真傻，真的。我单知道股票会跌，没想到股票会一直跌。'
voiceArr = ['XiaoxiaoNeural']

for v in voiceArr:
  shell = f'edge-tts --text {textStr} --voice zh-CN-{v} --write-media ./audios/{filename}.{v}.mp3'
  os.system(shell)
