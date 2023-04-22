#!/usr/bin/python3

import os

filename = os.path.basename(__file__)
textStr = '大盘暴涨我微涨！大盘微跌我暴跌！王德发！这个辣鸡股市！气的我原地爆炸！'
voiceArr = ['XiaoxiaoNeural']

for v in voiceArr:
  shell = f'edge-tts --text {textStr} --voice zh-CN-{v} --write-media ./audios/{filename}.{v}.mp3'
  os.system(shell)
