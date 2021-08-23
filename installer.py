import os
import csv
import zipfile
import requests

library = '/Users/trevorvansaun/PS1/'

# takes file url and downloads it
def download_url(url, save_name, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_name, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)


# Read csv into dictionary
games = {}
reader = csv.reader(open('game_list.csv', 'r'))

for k, v in reader:
    games[k] = v
print('Game list loaded.')

# Accept search input
print('Enter the name of the game you would like to install: ')
search = input()
print()

# Find potential matches
matches = []
for k in games.keys():
    if search in str(k):
        matches.append((k, games[k]))

# Display matches and allow user to select
selection = 0
if len(matches) > 1:

    print('Search results:')
    for i in range(0, len(matches)):
        print('[%d] %s' % (i, matches[i][0]))

    print()
    print('Enter the [number] of the correct game: ')
    selection = int(input())

# Validate selection
game_sel = matches[selection][0]
print()
print('You selected "%s", is this correct? [Y/n]: ' % game_sel)
res = input()
print()
if res == 'n':
    print('Oops, please restart script!')
    exit()
print('OK, dowloading your game now (this could take awhile)...')


# Call the download link
url = matches[selection][1]
zip_f = game_sel + '.zip'
download_url(url, zip_f)
print('Successfully downloaded zip file...')

# Create the folder
path = os.path.join(library, game_sel)
os.mkdir(path)
print('Successfully created game folder...')

# Extract contents to folder
with zipfile.ZipFile(zip_f, 'r') as zip_ref:
    zip_ref.extractall(path)
print('Successfully extracted files to game folder...')

# Tell user to refresh emulator
print()
print('Game installed! Refresh your gamelist in your emulator.')
