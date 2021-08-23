import csv
import requests
from bs4 import BeautifulSoup


# Retrieve HTML from the ROM repository and make soup
repo = "https://archive.org/download/Sony-Playstation-USA-Redump.org-2019-05-27/"
r = requests.get(repo)
soup = BeautifulSoup(r.text, 'html.parser')

# Initalize empty dictionary where key=name of game and value=link
games = {}

# Counter, bc they're helpful
cnt = 0

# Get each link from the table and put in games dictionary
for game in soup.find('tbody').find_all('a'):

    if(cnt == 0):  # first link is not a game, so we skip
        cnt += 1
        continue

    title = game.text[:-4].lower().replace(',', '')
    link = repo + game.get('href')

    games[title] = link

    cnt += 1
print('%d games loaded' % cnt)


# Write dictionary to csv
with open('game_list.csv', 'w') as f:
    for key in games:
        f.write("%s,%s\n" % (key, games[key]))
    f.close()
