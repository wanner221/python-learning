import random


# 生成一个指定范围内的随机数字
def create_number(number_range):
    number = random.randint(1, number_range)
    return number


# 显示游戏标题
def show_title():
    print("===================")
    print("     猜数字游戏     ")
    print("===================")


# 获取玩家名称
def player_info():
    name=input("请输入玩家名称：")
    return name


# 显示本局游戏的基本信息
def welcome(name, number_range, times):
    print(f"你好，{name}，欢迎来到猜数字游戏！")
    print(f"我已经想好了一个1~{number_range}的数字")
    print(f"你总共有{times}次猜测机会")


# 获取玩家选择的游戏难度，并检查输入是否合法
def get_level_choice():
    while True:
        try:
            choice = int(input("请选择难度：1.简单 2.普通 3.困难  输入："))

            # 只有输入1、2、3才算合法
            if choice in [1,2,3]:
                return choice
            else:
                print("请输入1~3")

        # 如果输入的不是数字，提示重新输入
        except ValueError:
            print("请输入数字！")


# 根据玩家选择的难度返回对应的游戏参数
# 返回值依次为：数字范围、猜测次数、基础分数
def choose_level(choice):
    if choice == 1:
        return 50, 10, 100
    elif choice == 2:
        return 100, 7, 200
    else:
        return 1000, 5, 300


# 获取玩家猜测的数字，并检查输入是否合法
def get_number_input():
    while True:
        try:
            number = int(input("请输入一个数："))
            return number

        # 如果输入的不是数字，提示重新输入
        except ValueError:
            print("请输入数字！")


# 判断玩家是否猜中数字
def check_number(number, times):
    count = 0

    # 在规定的次数内不断让玩家进行猜测
    while count < times:

        guess = get_number_input()

        count += 1

        if guess > number:
            print(f"偏大，你还有{times - count}次机会")
        elif guess < number:
            print(f"偏小，你还有{times - count}次机会")
        else:
            print(f"猜对了，你一共猜了{count}次")
            # 返回游戏结果和猜测次数
            return True, count

    # 如果循环结束仍然没有猜中，说明游戏失败
    print(f"机会已用完，正确答案为{number}")
    return False, count


# 显示本局游戏结果和最终得分
def result_game(result,name,score):
    if result:
        print("游戏胜利")
        print(f"玩家：{name}")
        print(f"最终得分：{score}")
    else:
        print("游戏失败")


# 询问玩家是否重新开始游戏
def restart_game():
    while True:
        again = input("是否重新开始游戏：1.是 2.否 输入：")

        if again == "1":
            return True
        elif again == "2":
            return False
        else:
            print("输入错误，请重新输入！")


# 根据基础分数和猜测次数计算最终得分
def calculate_score(base_score,count,result):
    if result:
        # 猜中的那一次不扣分，每猜错一次扣10分
        score=base_score-(count-1)*10

        # 防止分数低于0分
        if score<0:
            score=0
        return score
    else:
        # 游戏失败时得0分
        return 0