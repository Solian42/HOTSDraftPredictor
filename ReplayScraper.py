from bs4 import BeautifulSoup
from dateutil.parser import parse as dateParse
import requests
import unicodedata
import pickle

season2startstr = "9/13/2016"
season2start = dateParse(season2startstr)
url = 'http://www.hotslogs.com/Rankings?GameMode=4'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
player_name = []
player_id = []

table = soup.find()
for tr in soup.find_all('tr')[2:]:
    tds = tr.find_all('td')
    if len(tds) > 1:
        player_id.append(tds[0].text)
        player_name.append(tds[3].text)

replays = set()
i = 0
for id in player_id:
    print "finding replays for", player_name[i], "..."
    url = 'http://www.hotslogs.com/Player/MatchHistory?PlayerID=' + id
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    for tr in soup.find_all('tr')[2:]:
        tds = tr.find_all('td')
        if len(tds) > 1:
            str = tds[10].text
            date = dateParse(str)
            if season2start < date:
                replayID = unicodedata.normalize('NFKD', tds[1].text).encode('ascii', 'ignore')
                replays.add(replayID)
    i += 1
print len(replays)
pickle.dump(replays, open("masters_replays.data", "wb"))

