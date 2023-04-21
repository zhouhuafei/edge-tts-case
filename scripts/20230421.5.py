#!/usr/bin/python3

import os

filename = os.path.basename(__file__)
# 70还剩44
textStr = '70入市，到如今还剩44。不知和各位相比，我这算不算惨？'
voiceArr = ['XiaoxiaoNeural']

for v in voiceArr:
  shell = f'edge-tts --text {textStr} --voice zh-CN-{v} --write-media ./audios/{filename}.{v}.mp3'
  os.system(shell)
