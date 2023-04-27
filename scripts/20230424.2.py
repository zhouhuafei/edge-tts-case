#!/usr/bin/python3

import os

filename = os.path.basename(__file__)
# 我只是想搏一搏首付结果却输的那么彻底
textStr = f'./texts/{filename}.txt'
voiceArr = ['XiaoxiaoNeural']

for v in voiceArr:
  shell = f'edge-tts --file {textStr} --voice zh-CN-{v} --write-media ./audios/{filename}.{v}.mp3'
  os.system(shell)