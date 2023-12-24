#!/usr/bin/python3

import os

filename = os.path.basename(__file__)
# 哪有什么避风港
textStr = f'./texts/{filename}.txt'
# voiceArr = ['XiaoxiaoNeural', 'XiaoyiNeural', 'YunjianNeural', 'YunxiaNeural', 'YunxiNeural', 'YunyangNeural']
# 女声推荐 XiaoxiaoNeural
# 男声推荐 YunjianNeural
voiceArr = ['YunjianNeural']

for v in voiceArr:
  shell = f'edge-tts --file {textStr} --voice zh-CN-{v} --write-media ./audios/{filename}.{v}.mp3'
  os.system(shell)
