players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}
team_a_rest = [player['name'] for player in players_dict.values() if player['team'] == 'A' and player['status'] == 'Rest']
print(f'Все члены команды А, которые отдыхают: {", ".join(team_a_rest)}')
team_b_training = [player['name'] for player in players_dict.values() if player['team'] == 'B' and player['status'] == 'Training']
print(f'Все члены команды B, которые тренируются: {', '.join(team_b_training)}')
team_c_travel = [player['name'] for player in players_dict.values() if player['team'] == 'C' and player['status'] == 'Travel']
print(f'Все члены команды C, которые путешествуют: {', '.join(team_c_travel)}')

