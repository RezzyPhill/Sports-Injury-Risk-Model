import pandas as pd
import time
from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
from nba_api.stats.static import players
from utils import fetch_with_retries

def fetch_active_players():
    active_players = players.get_active_players()
    df_active_players = pd.DataFrame(active_players)
    df_active_players.to_csv('active_players.csv')
 