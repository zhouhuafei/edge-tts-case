#!/usr/bin/python3

import os

filename = os.path.basename(__file__)
# 谴责上汽集团、海螺水泥、中科电气、中荣股份、赣能股份、杉杉股份的下跌行为
textStr = f'./texts/{filename}.txt'
voiceArr = ['XiaoxiaoNeural']

for v in voiceArr:
  shell = f'edge-tts --file {textStr} --voice zh-CN-{v} --write-media ./audios/{filename}.{v}.mp3'
  os.system(shell)
