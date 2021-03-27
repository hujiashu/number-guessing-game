import random

def guess_number():
    answer = random.randint(1, 1000)
    sequence = answer - 1
    numbers = [i for i in range(1, 1001)]
    numbers[sequence] = f'{answer}'
    back = 1000
    init = 1
    times_count = 0
    x = input('我想了一个1~1000之间的整数，你猜猜是多少：')

    while True:
        if x.isdigit():
            x = int(x)
            if x >= 1 and x <= 1000:
                if numbers[x - 1] == f'{answer}':
                    print(f'你用了{times_count + 1}次才猜对！')
                    input('********按任意键退出********')
                    break

                times_count += 1
                numbers[x - 1] = ''
                try:
                    b = numbers[answer - 1:1000:1].index('') + answer - 1 #向1000方向找最小的''
                except ValueError:
                    b = 999
                try:
                    a = answer - 1 - numbers[answer - 1:0:-1].index('') #向0方向找最大的''
                except ValueError:
                    a = 0
                back = b + 1
                init = a + 1

                x = input(f'恭喜！你把范围缩小到了{init}~{back}，再猜猜看：')
            else:
                x = input('请输入1~1000的整数： ')
        else:
            x = input('请输入1~1000的整数： ')

guess_number()
