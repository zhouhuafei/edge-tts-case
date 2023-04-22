#!/usr/bin/python3

import os

filename = os.path.basename(__file__)
# 超级导购是一个品牌零售数字化智能化运营平台
textStr = '超级导购是一个品牌零售数字化智能化运营平台，公司开发了一款为品牌零售企业设计的业务运营SAAS平台，专注于零售业务领域的人、货、场的精细化运营研究，基于大数据的算法，形成从数据分析、规则建立到行动指令生成的自动化决策支持系统，通过使用手机APP将总部平台跟终端平台连在一起，帮助零售连锁企业加强组织强化连接能力、认知能力和运营能力。'
voiceArr = ['XiaoxiaoNeural', 'XiaoyiNeural', 'YunjianNeural', 'YunxiaNeural', 'YunxiNeural', 'YunyangNeural']

for v in voiceArr:
  shell = f'edge-tts --text {textStr} --voice zh-CN-{v} --write-media ./audios/{filename}.{v}.mp3'
  os.system(shell)
