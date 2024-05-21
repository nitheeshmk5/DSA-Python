def winner(arr):
    counts = {}

    for name in arr:
        if name in counts:
            counts[name] += 1
        else:
            counts[name] = 1

    max_vote = max(counts.values())
    
    winners_list = {key : value for key, value in counts.items() if value == max_vote}
    
    min_name = min(winners_list.keys())
    winner = {key:value for key,value in winners_list.items() if key == min_name}
    for name in winner.keys():
        winner_name = name
    final_winner = [winner_name,max_vote]

    return final_winner

    
    
    


print(winner(['john','johnny','jackie','johnny','john','jackie','jamie','jamie','john','johnny','jamie','johnny','john']))