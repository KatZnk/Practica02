def competition(rounds):
    
    leaderboard_rounds = {name: {'total': 0, 'wins': 0, 'best_round': 0} for name in rounds[0]['scores']}

    for i, round in enumerate(rounds, 1):
        max_points = -1
        winner = ""
        
        for name, judges in round['scores'].items():
            points = sum(judges.values())

            leaderboard_rounds[name]['total'] += points
    
            if points > leaderboard_rounds[name]['best_round']:
                leaderboard_rounds[name]['best_round'] = points
            
            if points > max_points:
                max_points = points
                winner = name

        leaderboard_rounds[winner]['wins'] += 1

        print(f"\n\nRonda {i} - {round['theme']}:")
        print(f"{'':<2}Ganador: {winner} ({max_points} pts)")
        print(f"{'':<8}{'~'*23}")
        print(f"{'':<8}{'Cocinero':<12} | {'Puntaje':^7}")
        print(f"{'':<8}{'-'*23}")
        
        leaderboard_org = sorted(leaderboard_rounds.items(), key=lambda x: x[1]['total'], reverse=True)

        for name, data in leaderboard_org:
            print(f"{'':<8}{name:<12} | {data['total']:^7}")

    print("\n\nTABLA DE POSICIONES FINAL: \n")
    
    print(f"{'':<8}{'Cocinero':<12} | {'Total':^7} | {'Victorias':^14} | {'Mejor Ronda':^11} | {'Promedio':^8}")
    print(f"{'':<8}{'-'*67}")
    
    for name, data in leaderboard_org:
        promedio = data['total'] / len(rounds)
        print(f"{'':<8}{name:<12} | {data['total']:^7} | {data['wins']:^14} | {data['best_round']:^11} | {promedio:^8.1f}")