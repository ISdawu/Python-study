score = 0
print('guess the animals!')
print('最大的树是什么树？')
guess = input()
if guess == '巨杉谢尔曼将军':
    print('回答正确！！！！！！！！！！')
    score = score + 1
else:
    print('回答错误' + '！！！！！！！！！！')
print('得分：' + str(score))
