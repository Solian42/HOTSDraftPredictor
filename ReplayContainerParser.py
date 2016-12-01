from bs4 import BeautifulSoup
import requests
import pickle
import unicodedata

def toFloat(s):
    x = s[-4:]
    if x[0] == 'l':
            avgLvl = float(x[-1])
    elif x[0] == ':':
            avgLvl = float(x[-2:])
    elif x[0] == ' ':
            avgLvl = float(x[-3:])
    else:
            avgLvl = float(x)

    return avgLvl

def toString(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')



replay_ids = pickle.load(open("Data/masters_replaysIDS.data", "rb"))
vectorDict = dict()
i = 1
length = len(replay_ids)
for replay in replay_ids:
    print "Replay", i, "out of", length
    print (i * 100.0) / length , "% complete."
    url = 'http://www.hotslogs.com/Player/MatchSummaryContainer?ReplayID=' + replay
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    players = dict()
    vectorDict[replay] = list()
    currList = vectorDict[replay]
    for div in soup.find_all('div'):
        h3 = div.find_all('h3')
        if len(h3) is 1 and len(currList) is 0:
            currList.append(toString(h3[0].text))

    for tr in soup.find_all('tr')[2:]:
        tds = tr.find_all('td')
        if len(tds) is 2 and ("MMR" in tds[1].string):
            string = tds[1].string
            mmr = int(string[9:13])
            currList.append(mmr)
            herolvl = toFloat(string)
            currList.append(herolvl)

        elif len(tds) is 24:
            player = list()
            #player name
            player.append(toString(tds[2].text))
            #hero name
            player.append(toString(tds[4].text))
            #hero level
            player.append(toString(tds[5].text))
            #Talents
            player.append(toString(tds[13].text))
            player.append(toString(tds[14].text))
            player.append(toString(tds[15].text))
            player.append(toString(tds[16].text))
            player.append(toString(tds[17].text))
            player.append(toString(tds[18].text))
            player.append(toString(tds[19].text))
            #Victory
            player.append(toString(tds[20].text))
            #MMR
            player.append(toString(tds[21].text))
            #MMR Delta
            player.append(toString(tds[22].text))
            currList.append(player)
        elif len(tds) is 27:
            player = list()
            #Player name
            player.append(toString(tds[0].text))
            #hero name
            player.append(toString(tds[1].text))
            #victory
            player.append(toString(tds[2].text))
            #score %
            #player.append(toString(tds[3].text))
            #Takedowns
            player.append(toString(tds[16].text))
            #Kills
            player.append(toString(tds[17].text))
            #Assists
            player.append(toString(tds[18].text))
            #Deaths
            player.append(toString(tds[19].text))
            #Time spent dead
            player.append(toString(tds[20].text))
            #Hero Damage
            player.append(toString(tds[21].text))
            #Siege Damage
            player.append(toString(tds[22].text))
            #Healing
            player.append(toString(tds[23].text))
            #Self-Healing
            player.append(toString(tds[24].text))
            #Damage taken
            player.append(toString(tds[25].text))
            #Xp Soaked
            player.append(toString(tds[26].text))
            currList.append(player)
    i += 1
print len(vectorDict)
pickle.dump(vectorDict, open("masters_replays.data", "wb"))

