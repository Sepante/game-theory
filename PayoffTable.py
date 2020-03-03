import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

#troop_cost = 6
#total_resource = 60
#conflict_cost = 30
#win_ratio = 0.666

levels = 3


total_resource = float(1)
troop_cost = total_resource * 0.02
#conflict_cost = total_resource * 0.50
conflict_cost = total_resource * 0.45
win_ratio = 0.7


def get_reward( our_troops, their_troops, winner_pays = False, total_resource = total_resource ):
    conflict_num = min( our_troops, their_troops )
    excessive_troops = max( our_troops, their_troops ) - conflict_num

    if not winner_pays:
        total_resource = total_resource - ( conflict_num * conflict_cost  ) - (excessive_troops * troop_cost)
    
        if our_troops > their_troops:
            return total_resource * win_ratio
        elif our_troops < their_troops:
            return total_resource * (1 - win_ratio)
        else:
            return total_resource / 2
    else: #winner_pays
        total_resource = total_resource - ( conflict_num * conflict_cost  )
        if our_troops > their_troops:
            return (total_resource * win_ratio) -(excessive_troops * troop_cost)
        elif our_troops < their_troops:
            return total_resource * (1 - win_ratio)
        else:
            return (total_resource / 2) - (excessive_troops * troop_cost)

    
reward_arr = np.zeros( (levels , levels) , float )
for i in range(levels):
    for j in range(levels):
        reward_arr[i,j] = get_reward(i,j, 1)

fig, ax = plt.subplots()
im = ax.matshow(reward_arr)
for (i, j), z in np.ndenumerate(reward_arr):
    ax.text(j, i, '{:0.3f}'.format(z), ha='center', va='center')
#fig.colorbar(im)


fig.savefig( str(win_ratio) +".png", dpi = 300, bbox_inches='tight')
