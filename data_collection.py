import pandas as pd
import time
from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
from nba_api.stats.static import players
from utils import fetch_with_retries

def fetch_active_players():
    active_players = players.get_active_players()
    df_active_players = pd.DataFrame(active_players)
    df_active_players.to_csv('data/active_players.csv', index=False)
    print("Active players saved to active_players.csv")
    return active_players

def collect_player_data(active_players, batch_size=50):
    workload_data = []
    demographics_data = []

    for ap, player in enumerate(active_players):
        player_id = player['id']
        try:
            career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
            workload_data.append(career_stats.get_data_frames()[0])
        except Exception as er:
            print(f"Error fetching workload for player {player_id}: {er}")
        
        try:
            player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
            demographics_data.append(player_info.get_data_frames()[0])
        except Exception as er:
            print(f"Error fetching demographics for player {player_id}: {er}")

        if (ap + 1) % batch_size == 0:
            pd.concat(workload_data).to_csv('data/workload_partial.csv', index=False)
            pd.concat(demographics_data).to_csv('data/demographics_partial.csv', index=False)
            print(f"Processed {ap + 1} players...")

        time.sleep(2)
    
    pd.concat(workload_data).to_csv('data/workload_data.csv', index=False)
    pd.concat(demographics_data).to_csv('data/demographics_data.csv', index=False)
    print("Data collection complete!")