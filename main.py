import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.nba.com/stats'

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

def extract_player_data(card):
    data = []
    title = card.find('h2', class_='LeaderBoardCard_lbcTitle___WI9J').text.strip()

    table = card.find('table', class_='LeaderBoardPlayerCard_lbpcTable__q3iZD')
    if table:
        rows = table.find_all('tr', class_='LeaderBoardPlayerCard_lbpcTableRow___Lod5')

        for row in rows:
            rank = row.find('td', class_='LeaderBoardPlayerCard_lbpcTableCell__SnM1o').text.strip()
            player_link = row.find('a', class_='Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL')
            player_name = player_link.text.strip()
            team_abbr = row.find('span', class_='LeaderBoardPlayerCard_lbpcTeamAbbr__fGlx3').text.strip()
            value_td = row.find('td', class_='LeaderBoardWithButtons_lbwbCardValue__5LctQ')
            value_link = value_td.find('a', class_='Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL', attrs={'data-has-children': 'false'})
            value = value_link.text.strip()

            data.append({
                'title': title,
                'rank': rank,
                'player_name': player_name,
                'team_abbr': team_abbr,
                'value': value
            })

    return data

def extract_team_data(card):
    data = []
    title = card.find('h2', class_='LeaderBoardCard_lbcTitle___WI9J').text.strip()

    table = card.find('table', class_='LeaderBoadTeamCard_lbtcTable__gmmZz')
    if table:
        rows = table.find_all('tr', class_='LeaderBoadTeamCard_lbtcTableRow__pJljn')

        for row in rows:
            rank = row.find('td', class_='LeaderBoadTeamCard_lbtcTableCell__RJFMA').text.strip()
            team_link = row.find('a', class_='Anchor_anchor__cSc3P LeaderBoadTeamCard_lbtcTableLink__LyoJz')
            team_name = team_link.text.strip()
            value = row.find('td', class_='LeaderBoardWithButtons_lbwbCardValue__5LctQ').text.strip()

            data.append({
                'title': title,
                'rank': rank,
                'team_name': team_name,
                'value': value
            })

    return data

cards = soup.find_all('div', class_='LeaderBoardCard_lbcWrapper__e4bCZ LeaderBoardWithButtons_lbwbCardGrid__Iqg6m LeaderBoardCard_leaderBoardCategory__vWRuZ')

player_data = []
team_data = []

for card in cards:
    player_data.extend(extract_player_data(card))
    team_data.extend(extract_team_data(card))

players = pd.DataFrame(player_data)
teams = pd.DataFrame(team_data)

print(players)
print(teams)
# Save data to Excel file with different sheets
with pd.ExcelWriter('nba_stats.xlsx') as writer:
    players.to_excel(writer, sheet_name='Players', index=False)
    teams.to_excel(writer, sheet_name='Teams', index=False)