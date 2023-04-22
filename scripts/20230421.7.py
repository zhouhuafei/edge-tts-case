#!/usr/bin/python3

import os

filename = os.path.basename(__file__)
# 股市现状
textStr = '大盘涨我不涨，我与大盘没来往，大盘跌我也跌，我与大盘要衔接。'
voiceArr = ['XiaoxiaoNeural']

for v in voiceArr:
  shell = f'edge-tts --text {textStr} --voice zh-CN-{v} --write-media ./audios/{filename}.{v}.mp3'
  os.system(shell)
