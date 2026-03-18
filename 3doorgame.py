import random as rd

def main(n_sim = 1000):
    controlList = []
    for i in range(n_sim):
        player_decision, win_or_lose = doorgame()
        controlList.append([i,player_decision, win_or_lose])

    ### Auswertung
    stays = []
    changes =[]
    for result in controlList:
        if result[1] == 'stay':
            stays.append(result[2])
        if result[1] == 'change':
            changes.append(result[2])

    stay_win_percentage = stays.count('win')/len(stays)
    print('stay_win_percentage: ',round(stay_win_percentage*100,2),'%')

    changes_win_percentage = changes.count('win')/len(changes)
    print('changes_win_percentage: ',round(changes_win_percentage*100,2),'%')

def doorgame():

    doors = ['1','2','3']
    winner_door = rd.choice(doors)
    player_door = rd.choice(doors)
    
    remaining_doors = [door for door in doors if door != player_door]
    remaining_not_winning_doors = [door for door in remaining_doors if door != winner_door]
    
    host_door_opened = rd.choice(remaining_not_winning_doors)
    remaining_choice_door = [door for door in remaining_doors if door != host_door_opened][0]
    
    player_decision = rd.choice(['stay','change'])
    
    if player_decision == 'change':
        player_door = remaining_choice_door
    
    win_or_lose = 'win'
    if player_door == winner_door:
        win_or_lose = 'win'
    else:
        win_or_lose = 'lose'

    #----------------- For Course of Play Simulation in Console: --------------------------
    #print('winner_door: ', winner_door)
    #print('player_door: ', player_door)
    #print('remaining_doors: ', remaining_doors)
    #print('remaining_not_winning_doors: ', remaining_not_winning_doors )
    #print('host_door_opened: ',host_door_opened)
    #print('remaining_choice_door: ', remaining_choice_door)
    #print('Player Decision: ', player_decision)
    #print('final decision Player door: ', player_door)
    #print('Outcome for player: ', win_or_lose)

    return player_decision, win_or_lose

#----------------------------------------------------------------------------------------------------------------

main()
