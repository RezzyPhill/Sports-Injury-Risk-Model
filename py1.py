import pandas as pd
import time
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats, commonplayerinfo

active_players = players.get_active_players()
#Convert to dataframe & save
df_active_players = pd.DataFrame(active_players)
df_active_players.to_csv('active_players.csv', index=False)
print("Active players saved to active_players.csv")

#Initialize lists for data
workload_data = []
demographics_data = []

batch_size = 50
# For Loop through active players
for ap, player in enumerate(active_players):
    player_id = player['id']
    
    #Get the workload stats
    try:
        career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
        workload_data.append(career_stats.get_data_frames()[0])
    except Exception as er:
        print(f"Error getting workload for player ID {player_id}: {er}")
        
    #Get demographic info
    try:
        player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
        demographics_data.append(player_info.get_data_frames()[0])
    except Exception as er:
        print(f"Error fetching demographics for player ID {player_id}: {er}")
        
    #Save Progress every batch players 
    if (ap + 1) % batch_size == 0:
        print(f"Processed {ap + 1} players...")
        pd.concat(workload_data).to_csv('workload_partial.csv', index=False)
        pd.concat(demographics_data).to_csv('demographic_partial.csv', index=False)
        
    #To avoid rate limits
    time.sleep(.5)
    
#Save the final datasets
pd.concat(workload_data).to_csv('workload_data.csv', index=False)
pd.concat(demographics_data).to_csv('demographic_data.csv', index=False)
print("Data collection completed!")

