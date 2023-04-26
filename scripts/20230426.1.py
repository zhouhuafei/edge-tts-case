#!/usr/bin/python3

import os

filename = os.path.basename(__file__)
# 炒股4年，70还剩41.8。
textStr = f'./texts/{filename}.txt'
voiceArr = ['XiaoxiaoNeural']

for v in voiceArr:
  shell = f'edge-tts --file {textStr} --voice zh-CN-{v} --write-media ./audios/{filename}.{v}.mp3'
  os.system(shell)
