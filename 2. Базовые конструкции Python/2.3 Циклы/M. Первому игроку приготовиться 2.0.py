player_number = int(input())
player_name1 = "яяяяяяяяяяяяяяяяяяяяяяяя"
for i in range(player_number):
    player_name2 = input()
    player_name1 = min(player_name1, player_name2)
print(player_name1)
