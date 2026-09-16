from game import *


# 游戏主程序，负责控制整个游戏流程
def main():
    # 创建排行榜，用来保存玩家名称和得分
    leaderboard = []

    show_title()

    # 获取玩家名称
    name = player_info()

    # 不断进行游戏，直到玩家选择退出
    while True:

        # 获取玩家选择的难度
        choice = get_level_choice()

        # 根据难度获取游戏参数
        number_range, times, base_score = choose_level(choice)

        # 显示本局游戏信息
        welcome(name, number_range, times)

        # 随机生成答案
        number = create_number(number_range)

        # 开始猜数字游戏
        result, count = check_number(number, times)

        # 根据游戏结果计算最终得分
        score = calculate_score(base_score, count, result)

        # 显示本局游戏结果
        result_game(result, name, score)

        # 只有游戏胜利才将玩家加入排行榜
        if result:
            leaderboard.append([name, score])

        # 按照分数从高到低对排行榜进行排序
        sorted_leaderboard = sorted(leaderboard, key=lambda player: player[1], reverse=True)

        print("=======排行榜=======")

        # enumerate()同时获取排名和玩家信息
        for i, (player_name, player_score) in enumerate(sorted_leaderboard):
            print(f"{i+1}. {player_name}--{player_score}分")

        # 如果玩家选择不重新开始，就结束游戏
        if restart_game() == False:
            print("游戏结束")
            break


# 只有直接运行 main.py 时，才执行主程序
if __name__ == "__main__":
    main()