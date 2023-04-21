#!/usr/bin/python3

import os

filename = os.path.basename(__file__)
# 蜀道难
textStr = './texts/蜀道难.txt'
voiceArr = ['XiaoxiaoNeural']

for v in voiceArr:
  shell = f'edge-tts --file {textStr} --voice zh-CN-{v} --write-media ./audios/{filename}.{v}.mp3'
  os.system(shell)
