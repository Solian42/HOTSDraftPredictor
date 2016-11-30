import csv
replays = dict()
with open('Data/Replays.csv', mode='r') as infile:
    reader = csv.reader(infile)
    i = 0
    for rows in reader:
        replays[i] = rows
        i+=1
replayCharacters = dict()
with open('Data/ReplayCharacters.csv', mode='r') as infile:
    reader = csv.reader(infile)
    i = 0
    for rows in reader:
        replays[i] = rows
        i+=1
qm = list()
hl = list()
tl = list()
ud = list()
for index in replays.iterkeys():

    if replays[index][1] is '3':
        qm.append(replays[index])
    elif replays[index][1] is '4':
        hl.append(replays[index])
    elif replays[index][1] is '5':
        tl.append(replays[index])
    elif replays[index][1] is '6':
        ud.append(replays[index])
print "QM:", len(qm)
print "HL:", len(hl)
print "TL:", len(tl)
print "UD:", len(ud)