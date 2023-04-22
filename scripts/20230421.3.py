#!/usr/bin/python3

import os

filename = os.path.basename(__file__)
# 股市里的大傻瓜
textStr = '下雪了，下雪了，股市里来了一群大傻瓜。有人气的头晕，有人张口破骂，有人躺在地上不说话，任由大雪掩埋他。'
voiceArr = ['XiaoxiaoNeural']

for v in voiceArr:
  shell = f'edge-tts --text {textStr} --voice zh-CN-{v} --write-media ./audios/{filename}.{v}.mp3'
  os.system(shell)
