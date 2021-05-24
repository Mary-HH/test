# i=1
# while i<=10:
# 	if i%2==0:
# 		print('{}是偶数：'.format(i))
# 	else:
# 		print('{}不是偶数'.format(i))
# 	i+=1


# i=1
# while i < 10:
# 	i+=1
# 	if i % 2 > 0:
# 		continue
# 	print(i)

# i=1
# while True:
# 	print(i)
# 	i+=1
# 	if i >11:
# 		break

import random
print('*'*30,'欢迎进入澳门赌场','*'*30)
username = input('请输入用户名：')
money = 0
answer = input('确认进入游戏吗（y/n）?')
if answer == 'y':
	while money<2:
		n=int(input('金币不足，请充值（100块钱30币，充值必须是100的倍数）'))
		if n%100==0 and n>0:
			money=(n//100)*30
		print('当前游戏币是{}，玩一局游戏扣除2个币'.format(money))
		print('---进入游戏---')

		while True:

			t1=random.randint(1,10)
			t2=random.randint(1,10)
			money-=2

			print('洗牌完毕，请猜大小：')
			guess=input('输入大或者输入小：')

			if ((t1+t2)>6 and guess == '大') or ((t1+t2)<=6 and guess == '小'):
				print('恭喜{}！本局游戏获奖励1个游戏币！当前游戏币剩余{}'.format(username,money))
				money+=1
			else:
				print('很遗憾！本局游戏输了！')
			answer = input('是否继续再来一局游戏，要扣除2枚游戏币？（y/n）')
			if answer!='y' or money<2:
				print('退出游戏啦！当前剩余{}游戏币'.format(money))
				break 