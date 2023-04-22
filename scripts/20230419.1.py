#!/usr/bin/python3

import os

filename = os.path.basename(__file__)
# 超级导购是国内一款针对服装鞋帽行业终端系统培训和管理的移动APP
textStr = '超级导购是国内一款针对服装鞋帽行业终端系统培训和管理的移动APP。它融合多方面的培训课件，拥有便捷的信息交互功能，并具备改变总部对销售终端的管理、培训、知识分享的功能。'
# voiceArr = ['XiaoxiaoNeural', 'XiaoyiNeural', 'YunjianNeural', 'YunxiaNeural', 'YunxiNeural', 'YunyangNeural']
voiceArr = ['XiaoxiaoNeural']

for v in voiceArr:
  shell = f'edge-tts --text {textStr} --voice zh-CN-{v} --write-media ./audios/{filename}.{v}.mp3'
  os.system(shell)
