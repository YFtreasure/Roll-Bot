import random
import psutil

from khl import Message, Bot

# init Bot
bot = Bot(token='xxxxxxxxxxxxxxxxx‘)


@bot.on_startup
async def _(_):
    print("机器人启动成功！Bot is ready!")
    print("指令加载成功-PythonCommand")

@bot.command(name='roll')
async def roll(msg: Message, min: int = 1, max: int = 100, c: int = 1):
    print("The Command 'roll' is run now.")
    result = [random.randint(min, max) for i in range(c)]
    await msg.reply(f'您抽到了: {result}')

@bot.command(name='hi')
async def world(msg: Message):
    await msg.reply('hello，我是 积分助手！')

@bot.command(name='inf')
async def Inf(msg: Message):
    await msg.reply('Points assistant\nVersion:1.2.0\nVersion Number:1.2.0kook-Python\nBot invite:[Link](http://s6e.cn/yj0jQ)\nThanks:Nixer\n       Wind Afeng\n       [Duanlianjie](https://duanlianjie.net/)\n---\nBot SDK:Khl.py(Python)')

@bot.command(name="chinese-inf")
async def ChineseInf(msg: Message):
    await msg.reply('```python''\n积分助手\n```\n版本:v1.2.0KOOK\n机器人邀请链接：[Link](http://s6e.cn/yj0jQ)\n开发者：\n```java\nNixer #6666;Wind阿风;```\n机器人SDK(API):khl.py')

@bot.command(name='感谢')
async def world(msg: Message):
    print ("Thanks a lot")
    await msg.ctx.channel.send(f"感谢：\n```python\nWind阿风-为机器人提供了许多建议，在1.2.1版本中重写代码\n```")
          
@bot.command(name='cpu')
async def world(msg: Message):
    print ('CPU...')
    await msg.reply(f'当前Bot负载{psutil.cpu_percent()}%\n使用cpu:Intel(R) Pentium(R) CPU G3240 @ 3.10GHz   3.10 GHz\n系统版本：Windows10专业版22H2\ncpu频率:{psutil.cpu_freq()}\ncpu核心：{psutil.cpu_count(logical=False)}\n数据来源：psutil库')

@bot.command(name='help')
async def Help(msg: Message,page:int = 4):
    dic = {1: "/roll <最小值> <最大值> <数量> 抽奖",
           2: "/cpu 占用",
           3: "/inf Bot数据",
           4: "/help <页数> 本帮助，共5个",
           5: "/hi 你好信息"}
    try:
        await msg.ctx.channel.send(dic[page])
        print ("HELP")
    except:
        await msg.ctx.channel.send("未找到该help页数")

@bot.command(name='info')
async def world(msg: Message):
    await msg.reply('''Python\n 
                    积分助手v1.2.2
                    更新：在代码中添加print
                          优化inf
                   ''')

@bot.command(name='生日快乐')
async def world(msg: Message,body:Message):
    await msg.reply(f'祝{body}生日快乐！')


import logging
logging.basicConfig(level='INFO')
bot.run()
