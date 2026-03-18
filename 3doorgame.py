import random as rd

def main():
    controlList = []
    for i in range(1000):
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
    ## Phase 0: Setup
    doors = ['1','2','3']
    winner_door = rd.choice(doors)
    #print('winner_door: ', winner_door)

    ## Phase 1: Player Chooses the first door
    #print('------------ Phase 1: Player Chooses the first door --------------------')
    player_door = rd.choice(doors)
    #print('player_door: ', player_door)

    remaining_doors = [door for door in doors if door != player_door]
    #print('remaining_doors: ', remaining_doors)
    remaining_not_winning_doors = [door for door in remaining_doors if door != winner_door]
    #print('remaining_not_winning_doors: ', remaining_not_winning_doors )

    ## Phase 2: Gameshow opens one of remaining door which is not winner door
    #print('------------ Phase 2: Gameshow opens one of remaining door which is not winner door --------------------')
    host_door_opened = rd.choice(remaining_not_winning_doors)
    #print('host_door_opened: ',host_door_opened)

    remaining_choice_door = [door for door in remaining_doors if door != host_door_opened][0]
    #print('remaining_choice_door: ', remaining_choice_door)

    ## Phase 3: Player decides if he wants to change the door
    #print('------------ Phase 3: Player decides if he wants to change the door --------------------')
    player_decision = rd.choice(['stay','change'])
    #print('Player Decision: ', player_decision)

    if player_decision == 'change':
        player_door = remaining_choice_door
    #print('final decision Player door: ', player_door)

    ## Phase 4: We see if Player wins
    #print('------------ Phase 4: We see if Player wins --------------------')
    win_or_lose = 'win'
    if player_door == winner_door:
        #print('Player has won')
        win_or_lose = 'win'
    else:
        #print('Player has lost')
        win_or_lose = 'lose'
    return player_decision, win_or_lose

#----------------------------------------------------------------------------------------------------------------

main()
