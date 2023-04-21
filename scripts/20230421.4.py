#!/usr/bin/python3

import os

filename = os.path.basename(__file__)
# 道德观察之炒股篇
textStr = '个股持续下跌，账户屡创新低。抄底被割，追高被割，躺平也被割。究竟是人性的泯灭，还是道德的沦丧。'
voiceArr = ['XiaoxiaoNeural']

for v in voiceArr:
  shell = f'edge-tts --text {textStr} --voice zh-CN-{v} --write-media ./audios/{filename}.{v}.mp3'
  os.system(shell)
