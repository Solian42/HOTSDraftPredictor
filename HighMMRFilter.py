import pickle

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

hl = pickle.load(open("datasets/hl_list.data", "rb"))
highmmr = []
i = 0
noPotato = 0
for replay in hl:

    Team1AvgMMR = 0.0
    Team2AvgMMR = 0.0
    for player in replay[1:11]:
        if str2bool(player[4]):
            Team1AvgMMR += int(player[5]) if player[5] is not '' else 0
        else:
            Team2AvgMMR += int(player[5]) if player[5] is not '' else 0
    Team2AvgMMR = (Team2AvgMMR / 5)
    Team1AvgMMR = (Team1AvgMMR / 5)
    if (Team1AvgMMR > 3200 and Team2AvgMMR > 3200):
        highmmr.append(replay)
pickle.dump(highmmr, open("datasets/hl_highmmr_list.data", "wb"))