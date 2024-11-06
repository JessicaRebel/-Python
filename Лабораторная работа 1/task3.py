list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
amount_of_players = len(list_players)
mid_index = amount_of_players // 2
first_team = list_players[:mid_index]
second_team = list_players[mid_index:]
print(first_team)
print(second_team)
