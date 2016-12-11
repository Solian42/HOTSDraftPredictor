import csv, pickle

replays = dict()
with open('datasets/Replays.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for rows in reader:
        replays[rows[0]] = list()
        replays[rows[0]].append(rows)

with open('datasets/ReplayCharacters.csv', mode='r') as infile:
    reader = csv.reader(infile)
    i = 0
    for rows in reader:
        replays[rows[0]].append(rows)
hl = list()
for index in replays.iterkeys():

    #if replays[index][0][1] is '3':
     #   qm.append(replays[index])
    if replays[index][0][1] is '4':
        hl.append(replays[index])
    #elif replays[index][0][1] is '5':
     #   tl.append(replays[index])
    #elif replays[index][0][1] is '6':
     #   ud.append(replays[index])
print "HL:", len(hl)
pickle.dump(hl, open("hl_list.data", "wb"))
vectors = dict()
i = 0