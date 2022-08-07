生命值=20

伤害=input('本次伤害值:')
伤害=int(伤害)

生命值=生命值-伤害

if 生命值<=0:
	print('Boss:gg,盒饭get')
	print('玩家:胜利!')
else:
	print('Boss:来啊,互相伤害啊!')


练习：
经验值			段位
0~99			镔铁
100~199			青铜
200~299			白银
300~399			黄金
400~499			钻石

经验值=input('输入经验值:')
经验值=int(经验值)

if 经验值>=0 and 经验值<=99:
	print('镔铁')
elif 经验值>=100 and 经验值<=199:
	print('青铜')
elif 经验值>=200 and 经验值<=299:
	print('白银')
elif 经验值>=300 and 经验值<=399:
	print('黄金')
elif 经验值>=400 and 经验值<=499:
	print('钻石')
else:
	print('非法数据')