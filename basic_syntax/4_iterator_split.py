players = ['charles', 'martin', 'john', 'jack', 'paul']
print(players[0:3])

# 切片的语法中，冒号左右都可以省略

# 负数索引时，0表示列表之外的索引，-1才是最后一位索引
print(players[-3:])

for player in players[-3:]:
    print(player)

backPlayers = players[:]
print(backPlayers)