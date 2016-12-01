import pickle
import unicodedata

def toString(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')

def FillVector(dict, vector):
    name = dict[u'C']
    if dict[u'RID'] % 2 is 0:
        ##Team "1" won
        didWin = dict[u'IsW']
    else:
        #Team "2" won
        didWin = not (dict[u'IsW'])
    if didWin:
        vector[0] = 1
    else:
        vector[0] = -1
    if name == u'Alarak':
        if didWin:
            vector[1] = 1.0
        else:
            vector[2] = 1.0
    elif name == u'Chromie':
        if didWin:
            vector[3] = 1.0
        else:
            vector[4] = 1.0
    elif name == u'Falstad':
        if didWin:
            vector[5] = 1.0
        else:
            vector[6] = 1.0
    elif name == u'Gall':
        if didWin:
            vector[7] = 1.0
        else:
            vector[8] = 1.0
    elif name == u'Greymane':
        if didWin:
            vector[9] = 1.0
        else:
            vector[10] = 1.0
    elif name == u"Gul'dan":
        if didWin:
            vector[11] = 1.0
        else:
            vector[12] = 1.0
    elif name == u'Illidan':
        if didWin:
            vector[13] = 1.0
        else:
            vector[14] = 1.0
    elif name == u'Jaina':
        if didWin:
            vector[15] = 1.0
        else:
            vector[16] = 1.0
    elif name == u"Kael'thas":
        if didWin:
            vector[17] = 1.0
        else:
            vector[18] = 1.0
    elif name == u'Kerrigan':
        if didWin:
            vector[19] = 1.0
        else:
            vector[20] = 1.0
    elif name == u'Li-Ming':
        if didWin:
            vector[21] = 1.0
        else:
            vector[22] = 1.0
    elif name == u'Lunara':
        if didWin:
            vector[23] = 1.0
        else:
            vector[24] = 1.0
    elif name == u'Nova':
        if didWin:
            vector[25] = 1.0
        else:
            vector[26] = 1.0
    elif name == u'Raynor':
        if didWin:
            vector[27] = 1.0
        else:
            vector[28] = 1.0
    elif name == u'Samuro':
        if didWin:
            vector[29] = 1.0
        else:
            vector[30] = 1.0
    elif name == u'The Butcher':
        if didWin:
            vector[31] = 1.0
        else:
            vector[32] = 1.0
    elif name == u'Thrall':
        if didWin:
            vector[33] = 1.0
        else:
            vector[34] = 1.0
    elif name == u'Tracer':
        if didWin:
            vector[35] = 1.0
        else:
            vector[36] = 1.0
    elif name == u'Tychus':
        if didWin:
            vector[37] = 1.0
        else:
            vector[38] = 1.0
    elif name == u'Valla':
        if didWin:
            vector[39] = 1.0
        else:
            vector[40] = 1.0
    elif name == u'Varian':
        if didWin:
            vector[41] = 1.0
        else:
            vector[42] = 1.0
    elif name == u'Zeratul':
        if didWin:
            vector[43] = 1.0
        else:
            vector[44] = 1.0
    elif name == u"Anub'arak":
        if didWin:
            vector[45] = 1.0
        else:
            vector[46] = 1.0
    elif name == u'Artanis':
        if didWin:
            vector[47] = 1.0
        else:
            vector[48] = 1.0
    elif name == u"Arthas":
        if didWin:
            vector[49] = 1.0
        else:
            vector[50] = 1.0
    elif name == u'Chen':
        if didWin:
            vector[51] = 1.0
        else:
            vector[52] = 1.0
    elif name == u'Cho':
        if didWin:
            vector[53] = 1.0
        else:
            vector[54] = 1.0
    elif name == u'Dehaka':
        if didWin:
            vector[55] = 1.0
        else:
            vector[56] = 1.0
    elif name == u'Diablo':
        if didWin:
            vector[57] = 1.0
        else:
            vector[58] = 1.0
    elif name == u'E.T.C.':
        if didWin:
            vector[59] = 1.0
        else:
            vector[60] = 1.0
    elif name == u'Johanna':
        if didWin:
            vector[61] = 1.0
        else:
            vector[62] = 1.0
    elif name == u'Leoric':
        if didWin:
            vector[63] = 1.0
        else:
            vector[64] = 1.0
    elif name == u'Muradin':
        if didWin:
            vector[65] = 1.0
        else:
            vector[66] = 1.0
    elif name == u'Rexxar':
        if didWin:
            vector[67] = 1.0
        else:
            vector[68] = 1.0
    elif name == u'Sonya':
        if didWin:
            vector[69] = 1.0
        else:
            vector[70] = 1.0
    elif name == u'Stitches':
        if didWin:
            vector[71] = 1.0
        else:
            vector[72] = 1.0
    elif name == u'Tyrael':
        #if korean == autowin
        if didWin:
            vector[73] = 1.0
        else:
            vector[74] = 1.0
    elif name == u'Zarya':
        if didWin:
            vector[75] = 1.0
        else:
            vector[76] = 1.0
    elif name == u'Auriel':
        if didWin:
            vector[77] = 1.0
        else:
            vector[78] = 1.0
    elif name == u'Brightwing':
        if didWin:
            vector[79] = 1.0
        else:
            vector[80] = 1.0
    elif name == u'Kharazim':
        if didWin:
            vector[81] = 1.0
        else:
            vector[82] = 1.0
    elif name == u'Li Li':
        if didWin:
            vector[83] = 1.0
        else:
            vector[84] = 1.0
    elif name == u'Lt. Morales':
        if didWin:
            vector[85] = 1.0
        else:
            vector[86] = 1.0
    elif name == u'Malfurion':
        if didWin:
            vector[87] = 1.0
        else:
            vector[88] = 1.0
    elif name == u'Rehgar':
        if didWin:
            vector[89] = 1.0
        else:
            vector[90] = 1.0
    elif name == u'Tassadar':
        if didWin:
            vector[91] = 1.0
        else:
            vector[92] = 1.0
    elif name == u'Tyrande':
        if didWin:
            vector[93] = 1.0
        else:
            vector[94] = 1.0
    elif name == u'Uther':
        if didWin:
            vector[95] = 1.0
        else:
            vector[96] = 1.0
    elif name == u'Abathur':
        if didWin:
            vector[97] = 1.0
        else:
            vector[98] = 1.0
    elif name == u'Azmodan':
        if didWin:
            vector[99] = 1.0
        else:
            vector[100] = 1.0
    elif name == u'Gazlowe':
        if didWin:
            vector[101] = 1.0
        else:
            vector[102] = 1.0
    elif name == u'Medivh':
        if didWin:
            vector[103] = 1.0
        else:
            vector[104] = 1.0
    elif name == u'Murky':
        if didWin:
            vector[105] = 1.0
        else:
            vector[106] = 1.0
    elif name == u'Nazeebo':
        if didWin:
            vector[107] = 1.0
        else:
            vector[108] = 1.0
    elif name == u'Sgt. Hammer':
        if didWin:
            vector[109] = 1.0
        else:
            vector[110] = 1.0
    elif name == u'Sylvanas':
        if didWin:
            vector[111] = 1.0
        else:
            vector[112] = 1.0
    elif name == u'The Lost Vikings':
        if didWin:
            vector[113] = 1.0
        else:
            vector[114] = 1.0
    elif name == u'Xul':
        if didWin:
            vector[115] = 1.0
        else:
            vector[116] = 1.0
    elif name == u'Zagara':
        if didWin:
            vector[117] = 1.0
        else:
            vector[118] = 1.0
    else:
        print "panicBasket panicBasket panicBasket"
        print name
    pass


replaydata = pickle.load(open("Data/pro_replays.data", "rb"))
vectors = dict()
i = 0

for replay in replaydata:
    vectors[i] = [0.0] * 119
    for player in replay[u'RCs']:
        FillVector(player, vectors[i])
    i += 1
f = open("pro_data.train", "wb")
for vector in vectors.itervalues():
    s = str(vector[0]) + " "
    i = 1
    for feature in vector[1:]:
        if i is 118:
            s += "" + str(i) + ":" + str(feature)
        else:
            s+= "" + str(i) + ":" + str(feature) + " "
        i += 1
    f.write(s)
    f.write('\n')
f.close()







