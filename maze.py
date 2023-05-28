import random
import time
import sys
sys.setrecursionlimit(10000)
def generatemaze(maze, x, y):
    direction = random.randint(1, 4)
    maze[x][y] = 0
    
    while ((x > 0 and maze[x][y+2] == 1) or (x+2 < m and maze[x+2][y] == 1) or
           (y > 0 and maze[x][y-2] == 1) or (y-2 < n and maze[x-2][y] == 1)):
        direction = random.randint(1, 4)
        
        if direction == 1 and x > 0 and maze[x][y+2] == 1:
            maze[x][y+1] = 0
            maze = generatemaze(maze, x, y+2)
        elif direction == 2 and y-2 < n and maze[x-2][y] == 1:
            maze[x-1][y] = 0
            maze = generatemaze(maze, x-2, y)
        elif direction == 3 and y > 0 and maze[x][y-2] == 1:
            maze[x][y-1] = 0
            maze = generatemaze(maze, x, y-2)
        elif direction == 4 and x+2 < m and maze[x+2][y] == 1:
            maze[x+1][y] = 0
            maze = generatemaze(maze, x+2, y)
    
    return maze

m = int(input("請輸入地圖大小:"))
if m%2 == 0:
    m = m + 1
n = m
maze = [[0] * (n+1) for _ in range(m+1)]
Start_i = 1
Start_j = 1
End_i = m-2
End_j = n-2

for x in range(m):
    for y in range(n):
        if x == 0 or y == 0 or x == m-1 or y == n-1:
            maze[x][y] = 2
        else:
            maze[x][y] = 1

maze = generatemaze(maze, End_i, End_j)
maze[Start_i][Start_j-1] = 0
maze[End_i][End_j+1] = 0

# 輸出迷宮，並產生out.txt的文件
with open("out.txt", "w") as file:
    file.write(f"{m} {n}\n")
    for row in maze[:-1]:
        file.write(" ".join(str(cell) for cell in row[:-1]))
        file.write("\n")


def play_maze_game():
    # 從文件中讀取迷宫
    with open("out.txt", "r") as file:
        lines = file.readlines()

    # 解析迷宫尺寸
    m, n = map(int, lines[0].split())
    
    # 創建迷宫地圖
    maze = []
    for line in lines[1:]:
        row = list(map(int, line.split()))
        maze.append(row)

    # 初始化玩家位置
    player_i, player_j = Start_i, Start_j-1

    #紀錄遊戲開始的時間
    start_time = time.time()

    while True:
        # 打印當前迷宫状態
        for i in range(m):
            for j in range(n):
                if i == player_i and j == player_j:
                    print("P", end=" ")  # 玩家位置
                elif maze[i][j] == 1:
                    print("#", end=" ")  # 牆壁
                elif maze[i][j] == 0:
                    print(".", end=" ")  # 可行路徑
                elif maze[i][j] == 2:
                    print("E", end=" ")  # 外牆
            print()
        
        # 獲取玩家输入
        direction = input("Enter direction (w/a/s/d): ")

        # 根據玩家输入更新位置
        if direction == "w" and maze[player_i-1][player_j] != 1 and maze[player_i-1][player_j] != 2:
            player_i -= 1
        elif direction == "a" and maze[player_i][player_j-1] != 1 and maze[player_i][player_j-1] != 2:
            player_j -= 1
        elif direction == "s" and maze[player_i+1][player_j] != 1 and maze[player_i+1][player_j] != 2:
            player_i += 1
        elif direction == "d" and maze[player_i][player_j+1] != 1 and maze[player_i][player_j+1] !=2:
            player_j += 1

        # 檢查是否到達終點
        if player_i == End_i and player_j == End_j+1:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"666 終於跑完了...你總共花了{elapsed_time:.2f}秒!")
            break

        print()  # 打印空行分開每一輪

play_maze_game()
