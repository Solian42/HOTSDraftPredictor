import pickle
import unicodedata
import random

def toString(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

def FillVector(dict, vector, ID):
    name = dict[1]
    win = str2bool(dict[2])
    if int(ID) % 2 is 0:
        ##Team "1" won
        didWin = win
    else:
        #Team "2" won
        didWin = not(win)
    if didWin:
        vector[0] = 1
    else:
        vector[0] = -1
    if name == 'Alarak':
        if didWin:
            vector[1] = 1.0
        else:
            vector[2] = 1.0
    elif name == 'Chromie':
        if didWin:
            vector[3] = 1.0
        else:
            vector[4] = 1.0
    elif name == 'Falstad':
        if didWin:
            vector[5] = 1.0
        else:
            vector[6] = 1.0
    elif name == 'Gall':
        if didWin:
            vector[7] = 1.0
        else:
            vector[8] = 1.0
    elif name == 'Greymane':
        if didWin:
            vector[9] = 1.0
        else:
            vector[10] = 1.0
    elif name == "Gul'dan":
        if didWin:
            vector[11] = 1.0
        else:
            vector[12] = 1.0
    elif name == 'Illidan':
        if didWin:
            vector[13] = 1.0
        else:
            vector[14] = 1.0
    elif name == 'Jaina':
        if didWin:
            vector[15] = 1.0
        else:
            vector[16] = 1.0
    elif name == "Kael'thas":
        if didWin:
            vector[17] = 1.0
        else:
            vector[18] = 1.0
    elif name == 'Kerrigan':
        if didWin:
            vector[19] = 1.0
        else:
            vector[20] = 1.0
    elif name == 'Li-Ming':
        if didWin:
            vector[21] = 1.0
        else:
            vector[22] = 1.0
    elif name == 'Lunara':
        if didWin:
            vector[23] = 1.0
        else:
            vector[24] = 1.0
    elif name == 'Nova':
        if didWin:
            vector[25] = 1.0
        else:
            vector[26] = 1.0
    elif name == 'Raynor':
        if didWin:
            vector[27] = 1.0
        else:
            vector[28] = 1.0
    elif name == 'Samuro':
        if didWin:
            vector[29] = 1.0
        else:
            vector[30] = 1.0
    elif name == 'The Butcher':
        if didWin:
            vector[31] = 1.0
        else:
            vector[32] = 1.0
    elif name == 'Thrall':
        if didWin:
            vector[33] = 1.0
        else:
            vector[34] = 1.0
    elif name == 'Tracer':
        if didWin:
            vector[35] = 1.0
        else:
            vector[36] = 1.0
    elif name == 'Tychus':
        if didWin:
            vector[37] = 1.0
        else:
            vector[38] = 1.0
    elif name == 'Valla':
        if didWin:
            vector[39] = 1.0
        else:
            vector[40] = 1.0
    elif name == 'Varian':
        if didWin:
            vector[41] = 1.0
        else:
            vector[42] = 1.0
    elif name == 'Zeratul':
        if didWin:
            vector[43] = 1.0
        else:
            vector[44] = 1.0
    elif name == "Anub'arak":
        if didWin:
            vector[45] = 1.0
        else:
            vector[46] = 1.0
    elif name == 'Artanis':
        if didWin:
            vector[47] = 1.0
        else:
            vector[48] = 1.0
    elif name == "Arthas":
        if didWin:
            vector[49] = 1.0
        else:
            vector[50] = 1.0
    elif name == 'Chen':
        if didWin:
            vector[51] = 1.0
        else:
            vector[52] = 1.0
    elif name == 'Cho':
        if didWin:
            vector[53] = 1.0
        else:
            vector[54] = 1.0
    elif name == 'Dehaka':
        if didWin:
            vector[55] = 1.0
        else:
            vector[56] = 1.0
    elif name == 'Diablo':
        if didWin:
            vector[57] = 1.0
        else:
            vector[58] = 1.0
    elif name == 'E.T.C.':
        if didWin:
            vector[59] = 1.0
        else:
            vector[60] = 1.0
    elif name == 'Johanna':
        if didWin:
            vector[61] = 1.0
        else:
            vector[62] = 1.0
    elif name == 'Leoric':
        if didWin:
            vector[63] = 1.0
        else:
            vector[64] = 1.0
    elif name == 'Muradin':
        if didWin:
            vector[65] = 1.0
        else:
            vector[66] = 1.0
    elif name == 'Rexxar':
        if didWin:
            vector[67] = 1.0
        else:
            vector[68] = 1.0
    elif name == 'Sonya':
        if didWin:
            vector[69] = 1.0
        else:
            vector[70] = 1.0
    elif name == 'Stitches':
        if didWin:
            vector[71] = 1.0
        else:
            vector[72] = 1.0
    elif name == 'Tyrael':
        #if korean == autowin
        if didWin:
            vector[73] = 1.0
        else:
            vector[74] = 1.0
    elif name == 'Zarya':
        if didWin:
            vector[75] = 1.0
        else:
            vector[76] = 1.0
    elif name == 'Auriel':
        if didWin:
            vector[77] = 1.0
        else:
            vector[78] = 1.0
    elif name == 'Brightwing':
        if didWin:
            vector[79] = 1.0
        else:
            vector[80] = 1.0
    elif name == 'Kharazim':
        if didWin:
            vector[81] = 1.0
        else:
            vector[82] = 1.0
    elif name == 'Li Li':
        if didWin:
            vector[83] = 1.0
        else:
            vector[84] = 1.0
    elif name == 'Lt. Morales':
        if didWin:
            vector[85] = 1.0
        else:
            vector[86] = 1.0
    elif name == 'Malfurion':
        if didWin:
            vector[87] = 1.0
        else:
            vector[88] = 1.0
    elif name == 'Rehgar':
        if didWin:
            vector[89] = 1.0
        else:
            vector[90] = 1.0
    elif name == 'Tassadar':
        if didWin:
            vector[91] = 1.0
        else:
            vector[92] = 1.0
    elif name == 'Tyrande':
        if didWin:
            vector[93] = 1.0
        else:
            vector[94] = 1.0
    elif name == 'Uther':
        if didWin:
            vector[95] = 1.0
        else:
            vector[96] = 1.0
    elif name == 'Abathur':
        if didWin:
            vector[97] = 1.0
        else:
            vector[98] = 1.0
    elif name == 'Azmodan':
        if didWin:
            vector[99] = 1.0
        else:
            vector[100] = 1.0
    elif name == 'Gazlowe':
        if didWin:
            vector[101] = 1.0
        else:
            vector[102] = 1.0
    elif name == 'Medivh':
        if didWin:
            vector[103] = 1.0
        else:
            vector[104] = 1.0
    elif name == 'Murky':
        if didWin:
            vector[105] = 1.0
        else:
            vector[106] = 1.0
    elif name == 'Nazeebo':
        if didWin:
            vector[107] = 1.0
        else:
            vector[108] = 1.0
    elif name == 'Sgt. Hammer':
        if didWin:
            vector[109] = 1.0
        else:
            vector[110] = 1.0
    elif name == 'Sylvanas':
        if didWin:
            vector[111] = 1.0
        else:
            vector[112] = 1.0
    elif name == 'The Lost Vikings':
        if didWin:
            vector[113] = 1.0
        else:
            vector[114] = 1.0
    elif name == 'Xul':
        if didWin:
            vector[115] = 1.0
        else:
            vector[116] = 1.0
    elif name == 'Zagara':
        if didWin:
            vector[117] = 1.0
        else:
            vector[118] = 1.0
    else:
        print "panicBasket panicBasket panicBasket"
        print name
    pass









def FillVectorDetailed(replayDict, ID, heroes, gameClass, subtypes):
    # replayDict contains scraped data for a single replay
    # ID is the replay ID on hotslogs
    # heroes is a bool; if True include individual hero features
    # gameClass is a bool; if True include feature for in game classification
    # subtype takes a value
    #       0: no subtypes
    #       1: hotslogs subtypes
    #       2: our subtypes
    #       3: cluster subtypes

    if subtype not in [0,1,2,3]:
        print "Error: Subtype must take value 0, 1, 2, or 3"
        return

    # randomize which team won based on replay ID
    name = replayDict[1]
    win = str2bool(replayDict[2])
    if int(ID) % 2 is 0:
        # Team "1" won
        didWin = win
    else:
        # Team "2" won
        didWin = not(win)
    if didWin:
        vector[0] = 1
    else:
        vector[0] = -1


        
    if name == 'Alarak':
        if didWin:
            if heroes:
                vector[1] = 1.0
            if gameClass:
                vector[123] += 1.0
            if subtype == 1:
                vector[143] += 1.0
            elif subtype == 2:
                vector[153] += 1.0
            elif subtype == 3:
                vector[141] += 1.0
        else:
            if heroes:
                vector[2] = 1.0
            if gameClass:
                vector[124] += 1.0
            if subtype == 1:
                vector[144] += 1.0
            elif subtype == 2:
                vector[154] += 1.0
            elif subtype == 3:
                vector[142] += 1.0
    elif name == 'Chromie':
        if didWin:
            if heroes:
                vector[3] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[145] += 1.0
        else:
            if heroes:
                vector[4] = 1.0
            if gameClass:
                vector[126] += 1.0
            if subtype == 1:
                vector[146] += 1.0
    elif name == 'Falstad':
        if didWin:
            if heroes:
                vector[5] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[147] += 1.0
        else:
            if heroes:
                vector[6] = 1.0
            if gameClass:
                vector[126] += 1.0
            if subtype == 1:
                vector[148] += 1.0
    elif name == 'Gall':
        if didWin:
            if heroes:
                vector[7] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[147] += 1.0
        else:
            if heroes:
                vector[8] = 1.0
            if gameClass:
                vector[126] += 1.0
            if subtype == 1:
                vector[148] += 1.0
    elif name == 'Greymane':
        if didWin:
            if heroes:
                vector[9] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[147] += 1.0
        else:
            if heroes:
                vector[10] = 1.0
            if gameClass:
                vector[126] += 1.0
            if subtype == 1:
                vector[148] += 1.0
    elif name == "Gul'dan":
        if didWin:
            if heroes:
                vector[11] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[147] += 1.0
        else:
            if heroes:
                vector[12] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[148] += 1.0
    elif name == 'Illidan':
        if didWin:
            if heroes:
                vector[13] = 1.0
            if gameClass:
                vector[123] += 1.0
            if subtype == 1:
                vector[147] += 1.0
        else:
            if heroes:
                vector[14] = 1.0
            if gameClass:
                vector[124] += 1.0
            if subtype == 1:
                vector[148] += 1.0
    elif name == 'Jaina':
        if didWin:
            if heroes:
                vector[15] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[145] += 1.0
        else:
            if heroes:
                vector[16] = 1.0
            if gameClass:
                vector[126] += 1.0
            if subtype == 1:
                vector[146] += 1.0
    elif name == "Kael'thas":
        if didWin:
            if heroes:
                vector[17] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[145] += 1.0
        else:
            if heroes:
                vector[18] = 1.0
            if gameClass:
                vector[126] += 1.0
            if subtype == 1:
                vector[146] += 1.0
    elif name == 'Kerrigan':
        if didWin:
            if heroes:
                vector[19] = 1.0
            if gameClass:
                vector[123] += 1.0
            if subtype == 1:
                vector[143] += 1.0
        else:
            if heroes:
                vector[20] = 1.0
            if gameClass:
                vector[124] += 1.0
            if subtype == 1:
                vector[144] += 1.0
    elif name == 'Li-Ming':
        if didWin:
            if heroes:
                vector[21] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[145] += 1.0
        else:
            if heroes:
                vector[22] = 1.0
            if gameClass:
                vector[126] += 1.0
            vector[146] += 1.0
    elif name == 'Lunara':
        if didWin:
            if heroes:
                vector[23] = 1.0
            if gameClass:
                vector[125] += 1.0
            vector[147] += 1.0
        else:
            if heroes:
                vector[24] = 1.0
            if gameClass:
                vector[126] += 1.0
            vector[148] += 1.0
    elif name == 'Nova':
        if didWin:
            if heroes:
                vector[25] = 1.0
            if gameClass:
                vector[125] += 1.0
            vector[143] += 1.0
        else:
            if heroes:
                vector[26] = 1.0
            if gameClass:
                vector[126] += 1.0
            vector[144] += 1.0
    elif name == 'Raynor':
        if didWin:
            if heroes:
                vector[27] = 1.0
            if gameClass:
                vector[125] += 1.0
            vector[147] += 1.0
        else:
            if heroes:
                vector[28] = 1.0
            if gameClass:
                vector[126] += 1.0
            vector[148] += 1.0
    elif name == 'Samuro':
        if didWin:
            if heroes:
                vector[29] = 1.0
            if gameClass:
                vector[123] += 1.0
            vector[143] += 1.0
        else:
            if heroes:
                vector[30] = 1.0
            if gameClass:
                vector[124] += 1.0
            vector[144] += 1.0
    elif name == 'The Butcher':
        if didWin:
            if heroes:
                vector[31] = 1.0
            if gameClass:
                vector[123] += 1.0
            vector[143] += 1.0
        else:
            if heroes:
                vector[32] = 1.0
            if gameClass:
                vector[124] += 1.0
            vector[144] += 1.0
    elif name == 'Thrall':
        if didWin:
            if heroes:
                vector[33] = 1.0
            if gameClass:
                vector[123] += 1.0
            vector[147] += 1.0
        else:
            if heroes:
                vector[34] = 1.0
            if gameClass:
                vector[124] += 1.0
            vector[148] += 1.0
    elif name == 'Tracer':
        if didWin:
            if heroes:
                vector[35] = 1.0
            if gameClass:
                vector[125] += 1.0
            vector[147] += 1.0
        else:
            if heroes:
                vector[36] = 1.0
            if gameClass:
                vector[126] += 1.0
            vector[148] += 1.0
    elif name == 'Tychus':
        if didWin:
            if heroes:
                vector[37] = 1.0
            if gameClass:
                vector[125] += 1.0
            vector[147] += 1.0
        else:
            if heroes:
                vector[38] = 1.0
            if gameClass:
                vector[126] += 1.0
            vector[148] += 1.0
    elif name == 'Valla':
        if didWin:
            if heroes:
                vector[39] = 1.0
            if gameClass:
                vector[125] += 1.0
            vector[147] += 1.0
        else:
            if heroes:
                vector[40] = 1.0
            if gameClass:
                vector[126] += 1.0
            vector[148] += 1.0
    elif name == 'Varian':
        if didWin:
            if heroes:
                vector[41] = 1.0
            if gameClass:
                vector[119] += 0.5
                vector[123] += 0.5
            vector[137] += 1.0
        else:
            if heroes:
                vector[42] = 1.0
            if gameClass:
                vector[120] += 0.5
                vector[124] += 0.5
            vector[138] += 1.0
    elif name == 'Zeratul':
        if didWin:
            if heroes:
                vector[43] = 1.0
            if gameClass:
                vector[123] += 1.0
            vector[143] += 1.0
        else:
            if heroes:
                vector[44] = 1.0
            if gameClass:
                vector[124] += 1.0
            vector[144] += 1.0
    elif name == "Anub'arak":
        if didWin:
            if heroes:
                vector[45] = 1.0
            if gameClass:
                vector[119] += 1.0
            vector[137] += 1.0
        else:
            if heroes:
                vector[46] = 1.0
            if gameClass:
                vector[120] += 1.0
            vector[138] += 1.0
    elif name == 'Artanis':
        if didWin:
            if heroes:
                vector[47] = 1.0
            if gameClass:
                vector[119] += 1.0
            vector[137] += 1.0
        else:
            if heroes:
                vector[48] = 1.0
            if gameClass:
                vector[120] += 1.0
            vector[138] += 1.0
    elif name == "Arthas":
        if didWin:
            if heroes:
                vector[49] = 1.0
            if gameClass:
                vector[119] += 1.0
            vector[137] += 1.0
        else:
            if heroes:
                vector[50] = 1.0
            if gameClass:
                vector[120] += 1.0
            vector[138] += 1.0
    elif name == 'Chen':
        if didWin:
            if heroes:
                vector[51] = 1.0
            if gameClass:
                vector[119] += 1.0
            vector[135] += 1.0
        else:
            if heroes:
                vector[52] = 1.0
            if gameClass:
                vector[120] += 1.0
            vector[136] += 1.0
    elif name == 'Cho':
        if didWin:
            if heroes:
                vector[53] = 1.0
            if gameClass:
                vector[119] += 1.0
            vector[135] += 1.0
        else:
            if heroes:
                vector[54] = 1.0
            if gameClass:
                vector[120] += 1.0
            vector[136] += 1.0
    elif name == 'Dehaka':
        if didWin:
            if heroes:
                vector[55] = 1.0
            if gameClass:
                vector[119] += 1.0
            vector[135] += 1.0
        else:
            if heroes:
                vector[56] = 1.0
            if gameClass:
                vector[120] += 1.0
            vector[136] += 1.0
    elif name == 'Diablo':
        if didWin:
            if heroes:
                vector[57] = 1.0
            if gameClass:
                vector[119] += 1.0
            vector[135] += 1.0
        else:
            if heroes:
                vector[58] = 1.0
            if gameClass:
                vector[120] += 1.0
            vector[136] += 1.0
    elif name == 'E.T.C.':
        if didWin:
            if heroes:
                vector[59] = 1.0
            if gameClass:
                vector[119] += 1.0
            vector[135] += 1.0
        else:
            if heroes:
                vector[60] = 1.0
            if gameClass:
                vector[120] += 1.0
            vector[136] += 1.0
    elif name == 'Johanna':
        if didWin:
            if heroes:
                vector[61] = 1.0
            if gameClass:
                vector[119] += 1.0
            vector[135] += 1.0
        else:
            if heroes:
                vector[62] = 1.0
            if gameClass:
                vector[120] += 1.0
            vector[136] += 1.0
    elif name == 'Leoric':
        if didWin:
            if heroes:
                vector[63] = 1.0
            if gameClass:
                vector[119] += 1.0
            vector[137] += 1.0
        else:
            if heroes:
                vector[64] = 1.0
            if gameClass:
                vector[120] += 1.0
            vector[138] += 1.0
    elif name == 'Muradin':
        if didWin:
            if heroes:
                vector[65] = 1.0
            if gameClass:
                vector[119] += 1.0
            vector[135] += 1.0
        else:
            if heroes:
                vector[66] = 1.0
            if gameClass:
                vector[120] += 1.0
            vector[136] += 1.0
    elif name == 'Rexxar':
        if didWin:
            if heroes:
                vector[67] = 1.0
            if gameClass:
                vector[121] += 1.0
            vector[135] += 1.0
        else:
            if heroes:
                vector[68] = 1.0
            if gameClass:
                vector[122] += 1.0
            vector[136] += 1.0
    elif name == 'Sonya':
        if didWin:
            if heroes:
                vector[69] = 1.0
            if gameClass:
                vector[119] += 1.0
            vector[137] += 1.0
        else:
            if heroes:
                vector[70] = 1.0
            if gameClass:
                vector[120] += 1.0
            vector[138] += 1.0
    elif name == 'Stitches':
        if didWin:
            if heroes:
                vector[71] = 1.0
            if gameClass:
                vector[119] += 1.0
            vector[135] += 1.0
        else:
            if heroes:
                vector[72] = 1.0
            if gameClass:
                vector[120] += 1.0
            vector[136] += 1.0
    elif name == 'Tyrael':
        #if korean == autowin
        if didWin:
            if heroes:
                vector[73] = 1.0
            if gameClass:
                vector[119] += 1.0
            vector[137] += 1.0
        else:
            if heroes:
                vector[74] = 1.0
            if gameClass:
                vector[120] += 1.0
            vector[138] += 1.0
    elif name == 'Zarya':
        if didWin:
            if heroes:
                vector[75] = 1.0
            if gameClass:
                vector[121] += 1.0
            vector[135] += 1.0
        else:
            if heroes:
                vector[76] = 1.0
            if gameClass:
                vector[122] += 1.0
            vector[136] += 1.0
    elif name == 'Auriel':
        if didWin:
            if heroes:
                vector[77] = 1.0
            if gameClass:
                vector[129] += 1.0
            vector[139] += 1.0
        else:
            if heroes:
                vector[78] = 1.0
            if gameClass:
                vector[130] += 1.0
            vector[140] += 1.0
    elif name == 'Brightwing':
        if didWin:
            if heroes:
                vector[79] = 1.0
            if gameClass:
                vector[129] += 1.0
            vector[139] += 1.0
        else:
            if heroes:
                vector[80] = 1.0
            if gameClass:
                vector[130] += 1.0
            vector[140] += 1.0
    elif name == 'Kharazim':
        if didWin:
            if heroes:
                vector[81] = 1.0
            if gameClass:
                vector[127] += 1.0
            vector[139] += 1.0
        else:
            if heroes:
                vector[82] = 1.0
            if gameClass:
                vector[128] += 1.0
            vector[140] += 1.0
    elif name == 'Li Li':
        if didWin:
            if heroes:
                vector[83] = 1.0
            if gameClass:
                vector[129] += 1.0
            vector[139] += 1.0
        else:
            if heroes:
                vector[84] = 1.0
            if gameClass:
                vector[130] += 1.0
            vector[140] += 1.0
    elif name == 'Lt. Morales':
        if didWin:
            if heroes:
                vector[85] = 1.0
            if gameClass:
                vector[129] += 1.0
            vector[139] += 1.0
        else:
            if heroes:
                vector[86] = 1.0
            if gameClass:
                vector[130] += 1.0
            vector[140] += 1.0
    elif name == 'Malfurion':
        if didWin:
            if heroes:
                vector[87] = 1.0
            if gameClass:
                vector[129] += 1.0
            vector[139] += 1.0
        else:
            if heroes:
                vector[88] = 1.0
            if gameClass:
                vector[130] += 1.0
            vector[140] += 1.0
    elif name == 'Rehgar':
        if didWin:
            if heroes:
                vector[89] = 1.0
            if gameClass:
                vector[127] += 1.0
            vector[139] += 1.0
        else:
            if heroes:
                vector[90] = 1.0
            if gameClass:
                vector[128] += 1.0
            vector[140] += 1.0
    elif name == 'Tassadar':
        if didWin:
            if heroes:
                vector[91] = 1.0
            if gameClass:
                vector[129] += 1.0
            vector[141] += 1.0
        else:
            if heroes:
                vector[92] = 1.0
            if gameClass:
                vector[130] += 1.0
            vector[142] += 1.0
    elif name == 'Tyrande':
        if didWin:
            if heroes:
                vector[93] = 1.0
            if gameClass:
                vector[129] += 1.0
            vector[139] += 1.0
        else:
            if heroes:
                vector[94] = 1.0
            if gameClass:
                vector[130] += 1.0
            vector[140] += 1.0
    elif name == 'Uther':
        if didWin:
            if heroes:
                vector[95] = 1.0
            if gameClass:
                vector[127] += 1.0
            vector[139] += 1.0
        else:
            if heroes:
                vector[96] = 1.0
            if gameClass:
                vector[128] += 1.0
            vector[140] += 1.0
    elif name == 'Abathur':
        if didWin:
            if heroes:
                vector[97] = 1.0
            if gameClass:
                vector[131] += 1.0
            vector[151] += 1.0
        else:
            if heroes:
                vector[98] = 1.0
            if gameClass:
                vector[132] += 1.0
            vector[152] += 1.0
    elif name == 'Azmodan':
        if didWin:
            if heroes:
                vector[99] = 1.0
            if gameClass:
                vector[133] += 1.0
            vector[149] += 1.0
        else:
            if heroes:
                 vector[100] = 1.0
            if gameClass:
                vector[134] += 1.0
            vector[150] += 1.0
    elif name == 'Gazlowe':
        if didWin:
            if heroes:
                vector[101] = 1.0
            if gameClass:
                vector[131] += 1.0
            vector[149] += 1.0
        else:
            if heroes:
                vector[102] = 1.0
            if gameClass:
                vector[132] += 1.0
            vector[150] += 1.0
    elif name == 'Medivh':
        if didWin:
            if heroes:
                vector[103] = 1.0
            if gameClass:
                vector[133] += 1.0
            vector[151] += 1.0
        else:
            if heroes:
                vector[104] = 1.0
            if gameClass:
                vector[135] += 1.0
            vector[152] += 1.0
    elif name == 'Murky':
        if didWin:
            if heroes:
                vector[105] = 1.0
            if gameClass:
                vector[131] += 1.0
            vector[151] += 1.0
        else:
            if heroes:
                vector[106] = 1.0
            if gameClass:
                vector[132] += 1.0
            vector[152] += 1.0
    elif name == 'Nazeebo':
        if didWin:
            if heroes:
                vector[107] = 1.0
            if gameClass:
                vector[133] += 1.0
            vector[149] += 1.0
        else:
            if heroes:
                vector[108] = 1.0
            if gameClass:
                vector[134] += 1.0
            vector[150] += 1.0
    elif name == 'Sgt. Hammer':
        if didWin:
            if heroes:
                vector[109] = 1.0
            if gameClass:
                vector[133] += 1.0
            vector[149] += 1.0
        else:
            if heroes:
                vector[110] = 1.0
            if gameClass:
                vector[134] += 1.0
            vector[150] += 1.0
    elif name == 'Sylvanas':
        if didWin:
            if heroes:
                vector[111] = 1.0
            if gameClass:
                vector[133] += 1.0
            vector[149] += 1.0
        else:
            if heroes:
                vector[112] = 1.0
            if gameClass:
                vector[134] += 1.0
            vector[150] += 1.0
    elif name == 'The Lost Vikings':
        if didWin:
            if heroes:
                vector[113] = 1.0
            if gameClass:
                vector[133] += 1.0
            vector[151] += 1.0
        else:
            if heroes:
                vector[114] = 1.0
            if gameClass:
                vector[134] += 1.0
            vector[152] += 1.0
    elif name == 'Xul':
        if didWin:
            if heroes:
                vector[115] = 1.0
            if gameClass:
                vector[131] += 1.0
            vector[149] += 1.0
        else:
            if heroes:
                 vector[116] = 1.0
            if gameClass:
                vector[132] += 1.0
            vector[150] += 1.0
    elif name == 'Zagara':
        if didWin:
            if heroes:
                vector[117] = 1.0
            if gameClass:
                vector[133] += 1.0
            vector[149] += 1.0
        else:
            if heroes:
                vector[118] = 1.0
            if gameClass:
                vector[134] += 1.0
            vector[150] += 1.0
    else:
        print "panicBasket panicBasket panicBasket"
        print name
    pass






def MarkMap(mapName, vector):
    if mapName == "Battlefield of Eternity":
        vector[153] = 1.0
    elif mapName == "Blackheart's Bay":
        vector[154] = 1.0
    elif mapName == "Braxis Holdout":
        vector[155] = 1.0
    elif mapName == "Cursed Hollow":
        vector[156] = 1.0
    elif mapName == "Dragon Shire":
        vector[157] = 1.0
    elif mapName == "Garden of Terror":
        vector[158] = 1.0
    elif mapName == "Infernal Shrines":
        vector[159] = 1.0
    elif mapName == "Sky Temple":
        vector[160] = 1.0
    elif mapName == "Tomb of the Spider Queen":
        vector[161] = 1.0
    elif mapName == "Towers of Doom":
        vector[162] = 1.0
    elif mapName == "Warhead Junction":
        vector[163] = 1.0
    else:
        print "wat"
        print mapName

    pass




replaydata = pickle.load(open("datasets/masters_replays.data", "rb"))
vectors = dict()
i = 0

for ID, replay in replaydata.iteritems():
    vectors[i] = [0.0] * 164
    MarkMap(replay[0], vectors[i])
    for player in replay[14:25]:
        FillVectorHeroless(player, vectors[i], ID)
    i += 1
f1 = open("datasets/masters_data_heroless.train", "wb")
f2 = open("datasets/masters_data_heroless.dev", "wb")
for vector in vectors.itervalues():
    s = str(vector[0]) + " "
    i = 1
    for feature in vector[1:]:
        if i is 163:
            s += "" + str(i) + ":" + str(feature)
        else:
            s+= "" + str(i) + ":" + str(feature) + " "
        i += 1
    if random.randint(0, 10) % 10 != 0:
        f1.write(s)
        f1.write('\n')
    else:
        f2.write(s)
        f2.write('\n')
f1.close()
f2.close()





"""
Melee Warrior - 119, 120
Ranged Warrior - 121, 122
Melee Assassin - 123, 124
Ranged Assassin - 125, 126
Melee Support - 127, 128
Ranged Support - 129, 130
Melee Specialist - 131, 132
Ranged Specialist - 133, 134

Tank - 135, 136
Bruiser - 137, 138
Healer - 139, 140
Support - 141, 142
Ambusher - 143, 144
Burst Damage - 145, 146
Sustained Damage - 147, 148
Siege - 149, 150
Utility - 151, 152

Battlefield of Eternity - 153
Blackheart's Bay - 154
Braxis Holdout - 155
Cursed Hollow - 156
Dragon Shire - 157
Garden of Terror - 158
Infernal Shrines - 159
Sky Temple - 160
Tomb of the Spider Queen - 161
Towers of Doom - 162
Warhead Junction - 163
"""
























