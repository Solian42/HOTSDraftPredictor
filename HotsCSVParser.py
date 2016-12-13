import csv
import pickle
import random
import math

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")


def FillVectorDetailed(replayDict, vector, ID, heroes, gameClass, subtypes):
    # replayDict contains scraped data for a single player in a replay
    # vector is the feature vector so far
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
    name = replayDict[2]
    win = str2bool(replayDict[4])
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


    # set features based on hero played and given input
    
    if name == '56':
        # Alarak
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
    elif name == '52':
        # Chromie
        if didWin:
            if heroes:
                vector[3] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[145] += 1.0
            elif subtype == 2:
                vector[145] += 1.0
            elif subtype == 3:
                vector[141] += 1.0
        else:
            if heroes:
                vector[4] = 1.0
            if gameClass:
                vector[126] += 1.0
            if subtype == 1:
                vector[146] += 1.0
            elif subtype == 2:
                vector[146] += 1.0
            elif subtype == 3:
                vector[142] += 1.0
    elif name == '9':
        # Falstad
        if didWin:
            if heroes:
                vector[5] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[147] += 1.0
            elif subtype == 2:
                vector[149] += 1.0
            elif subtype == 3:
                vector[141] += 1.0
        else:
            if heroes:
                vector[6] = 1.0
            if gameClass:
                vector[126] += 1.0
            if subtype == 1:
                vector[148] += 1.0
            elif subtype == 2:
                vector[150] += 1.0
            elif subtype == 3:
                vector[142] += 1.0
    elif name == '45':
        # Gall
        if didWin:
            if heroes:
                vector[7] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[147] += 1.0
            elif subtype == 2:
                vector[149] += 1.0
            elif subtype == 3:
                vector[149] += 1.0
        else:
            if heroes:
                vector[8] = 1.0
            if gameClass:
                vector[126] += 1.0
            if subtype == 1:
                vector[148] += 1.0
            elif subtype == 2:
                vector[150] += 1.0
            elif subtype == 3:
                vector[150] += 1.0
    elif name == '47':
        # Greymane
        if didWin:
            if heroes:
                vector[9] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[147] += 1.0
            elif subtype == 2:
                vector[153] += 1.0
            elif subtype == 3:
                vector[141] += 1.0
        else:
            if heroes:
                vector[10] = 1.0
            if gameClass:
                vector[126] += 1.0
            if subtype == 1:
                vector[148] += 1.0
            elif subtype == 2:
                vector[154] += 1.0
            elif subtype == 3:
                vector[142] += 1.0
    elif name == "54":
        # Gul'dan
        if didWin:
            if heroes:
                vector[11] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[147] += 1.0
            elif subtype == 2:
                vector[149] += 1.0
            elif subtype == 3:
                vector[141] += 1.0
        else:
            if heroes:
                vector[12] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[148] += 1.0
            elif subtype == 2:
                vector[150] += 1.0
            elif subtype == 3:
                vector[142] += 1.0
    elif name == '11':
        # Illidan
        if didWin:
            if heroes:
                vector[13] = 1.0
            if gameClass:
                vector[123] += 1.0
            if subtype == 1:
                vector[147] += 1.0
            elif subtype == 2:
                vector[151] += 1.0
            elif subtype == 3:
                vector[151] += 1.0
        else:
            if heroes:
                vector[14] = 1.0
            if gameClass:
                vector[124] += 1.0
            if subtype == 1:
                vector[148] += 1.0
            elif subtype == 2:
                vector[152] += 1.0
            elif subtype == 3:
                vector[152] += 1.0
    elif name == '12':
        # Jaina
        if didWin:
            if heroes:
                vector[15] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[145] += 1.0
            elif subtype == 2:
                vector[145] += 1.0
            elif subtype == 3:
                vector[141] += 1.0
        else:
            if heroes:
                vector[16] = 1.0
            if gameClass:
                vector[126] += 1.0
            if subtype == 1:
                vector[146] += 1.0
            elif subtype == 2:
                vector[146] += 1.0
            elif subtype == 3:
                vector[142] += 1.0
    elif name == "14":
        # Kael'thas
        if didWin:
            if heroes:
                vector[17] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[145] += 1.0
            elif subtype == 2:
                vector[145] += 1.0
            elif subtype == 3:
                vector[141] += 1.0
        else:
            if heroes:
                vector[18] = 1.0
            if gameClass:
                vector[126] += 1.0
            if subtype == 1:
                vector[146] += 1.0
            elif subtype == 2:
                vector[146] += 1.0
            elif subtype == 3:
                vector[142] += 1.0
    elif name == '15':
        # Kerrigan
        if didWin:
            if heroes:
                vector[19] = 1.0
            if gameClass:
                vector[123] += 1.0
            if subtype == 1:
                vector[143] += 1.0
            elif subtype == 2:
                vector[153] += 1.0
            elif subtype == 3:
                vector[151] += 1.0
        else:
            if heroes:
                vector[20] = 1.0
            if gameClass:
                vector[124] += 1.0
            if subtype == 1:
                vector[144] += 1.0
            elif subtype == 2:
                vector[154] += 1.0
            elif subtype == 3:
                vector[152] += 1.0
    elif name == '48':
        # Li-Ming
        if didWin:
            if heroes:
                vector[21] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[145] += 1.0
            elif subtype == 2:
                vector[145] += 1.0
            elif subtype == 3:
                vector[141] += 1.0
        else:
            if heroes:
                vector[22] = 1.0
            if gameClass:
                vector[126] += 1.0
            if subtype == 1:
                vector[146] += 1.0
            elif subtype == 2:
                vector[146] += 1.0
            elif subtype == 3:
                vector[142] += 1.0
    elif name == '46':
        # Lunara
        if didWin:
            if heroes:
                vector[23] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[147] += 1.0
            elif subtype == 2:
                vector[147] += 1.0
            elif subtype == 3:
                vector[141] += 1.0
        else:
            if heroes:
                vector[24] = 1.0
            if gameClass:
                vector[126] += 1.0
            if subtype == 1:
                vector[148] += 1.0
            elif subtype == 2:
                vector[148] += 1.0
            elif subtype == 3:
                vector[142] += 1.0
    elif name == '23':
        # Nova
        if didWin:
            if heroes:
                vector[25] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[143] += 1.0
            elif subtype == 2:
                vector[145] += 1.0
            elif subtype == 3:
                vector[143] += 1.0
        else:
            if heroes:
                vector[26] = 1.0
            if gameClass:
                vector[126] += 1.0
            if subtype == 1:
                vector[144] += 1.0
            elif subtype == 2:
                vector[146] += 1.0
            elif subtype == 3:
                vector[144] += 1.0
    elif name == '24':
        # Raynor
        if didWin:
            if heroes:
                vector[27] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[147] += 1.0
            elif subtype == 2:
                vector[147] += 1.0
            elif subtype == 3:
                vector[141] += 1.0
        else:
            if heroes:
                vector[28] = 1.0
            if gameClass:
                vector[126] += 1.0
            if subtype == 1:
                vector[148] += 1.0
            elif subtype == 2:
                vector[148] += 1.0
            elif subtype == 3:
                vector[142] += 1.0
    elif name == '58':
        # Samuro
        if didWin:
            if heroes:
                vector[29] = 1.0
            if gameClass:
                vector[123] += 1.0
            if subtype == 1:
                vector[143] += 1.0
            elif subtype == 2:
                vector[151] += 1.0
            elif subtype == 3:
                vector[141] += 1.0
        else:
            if heroes:
                vector[30] = 1.0
            if gameClass:
                vector[124] += 1.0
            if subtype == 1:
                vector[144] += 1.0
            elif subtype == 2:
                vector[152] += 1.0
            elif subtype == 3:
                vector[142] += 1.0
    elif name == '31':
        # The Butcher
        if didWin:
            if heroes:
                vector[31] = 1.0
            if gameClass:
                vector[123] += 1.0
            if subtype == 1:
                vector[143] += 1.0
            elif subtype == 2:
                vector[151] += 1.0
            elif subtype == 3:
                vector[143] += 1.0
        else:
            if heroes:
                vector[32] = 1.0
            if gameClass:
                vector[124] += 1.0
            if subtype == 1:
                vector[144] += 1.0
            elif subtype == 2:
                vector[152] += 1.0
            elif subtype == 3:
                vector[144] += 1.0
    elif name == '33':
        # Thrall
        if didWin:
            if heroes:
                vector[33] = 1.0
            if gameClass:
                vector[123] += 1.0
            if subtype == 1:
                vector[147] += 1.0
            elif subtype == 2:
                vector[139] += 1.0
            elif subtype == 3:
                vector[151] += 1.0
        else:
            if heroes:
                vector[34] = 1.0
            if gameClass:
                vector[124] += 1.0
            if subtype == 1:
                vector[148] += 1.0
            elif subtype == 2:
                vector[140] += 1.0
            elif subtype == 3:
                vector[152] += 1.0
    elif name == '51':
        # Tracer
        if didWin:
            if heroes:
                vector[35] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[147] += 1.0
            elif subtype == 2:
                vector[151] += 1.0
            elif subtype == 3:
                vector[143] += 1.0
        else:
            if heroes:
                vector[36] = 1.0
            if gameClass:
                vector[126] += 1.0
            if subtype == 1:
                vector[148] += 1.0
            elif subtype == 2:
                vector[152] += 1.0
            elif subtype == 3:
                vector[144] += 1.0
    elif name == '34':
        # Tychus
        if didWin:
            if heroes:
                vector[37] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[147] += 1.0
            elif subtype == 2:
                vector[147] += 1.0
            elif subtype == 3:
                vector[141] += 1.0
        else:
            if heroes:
                vector[38] = 1.0
            if gameClass:
                vector[126] += 1.0
            if subtype == 1:
                vector[148] += 1.0
            elif subtype == 2:
                vector[148] += 1.0
            elif subtype == 3:
                vector[142] += 1.0
    elif name == '38':
        # Valla
        if didWin:
            if heroes:
                vector[39] = 1.0
            if gameClass:
                vector[125] += 1.0
            if subtype == 1:
                vector[147] += 1.0
            elif subtype == 2:
                vector[147] += 1.0
            elif subtype == 3:
                vector[141] += 1.0
        else:
            if heroes:
                vector[40] = 1.0
            if gameClass:
                vector[126] += 1.0
            if subtype == 1:
                vector[148] += 1.0
            elif subtype == 2:
                vector[148] += 1.0
            elif subtype == 3:
                vector[142] += 1.0
    elif name == '59':
        # Varian
        if didWin:
            if heroes:
                vector[41] = 1.0
            if gameClass:
                vector[119] += 0.5
                vector[123] += 0.5
            if subtype == 1:
                vector[137] += 1.0
            elif subtype == 2:
                vector[139] += 1.0
            elif subtype == 3:
                vector[147] += 1.0
        else:
            if heroes:
                vector[42] = 1.0
            if gameClass:
                vector[120] += 0.5
                vector[124] += 0.5
            if subtype == 1:
                vector[138] += 1.0
            elif subtype == 2:
                vector[140] += 1.0
            elif subtype == 3:
                vector[148] += 1.0
    elif name == '40':
        # Zeratul
        if didWin:
            if heroes:
                vector[43] = 1.0
            if gameClass:
                vector[123] += 1.0
            if subtype == 1:
                vector[143] += 1.0
            elif subtype == 2:
                vector[153] += 1.0
            elif subtype == 3:
                vector[143] += 1.0
        else:
            if heroes:
                vector[44] = 1.0
            if gameClass:
                vector[124] += 1.0
            if subtype == 1:
                vector[144] += 1.0
            elif subtype == 2:
                vector[154] += 1.0
            elif subtype == 3:
                vector[144] += 1.0
    elif name == "2":
        # Anub'arak
        if didWin:
            if heroes:
                vector[45] = 1.0
            if gameClass:
                vector[119] += 1.0
            if subtype == 1:
                vector[137] += 1.0
            elif subtype == 2:
                vector[137] += 1.0
            elif subtype == 3:
                vector[137] += 1.0
        else:
            if heroes:
                vector[46] = 1.0
            if gameClass:
                vector[120] += 1.0
            if subtype == 1:
                vector[138] += 1.0
            elif subtype == 2:
                vector[138] += 1.0
            elif subtype == 3:
                vector[138] += 1.0
    elif name == '43':
        # Artanis
        if didWin:
            if heroes:
                vector[47] = 1.0
            if gameClass:
                vector[119] += 1.0
            if subtype == 1:
                vector[137] += 1.0
            elif subtype == 2:
                vector[139] += 1.0
            elif subtype == 3:
                vector[147] += 1.0
        else:
            if heroes:
                vector[48] = 1.0
            if gameClass:
                vector[120] += 1.0
            if subtype == 1:
                vector[138] += 1.0
            elif subtype == 2:
                vector[140] += 1.0
            elif subtype == 3:
                vector[148] += 1.0
    elif name == "3":
        # Arthas
        if didWin:
            if heroes:
                vector[49] = 1.0
            if gameClass:
                vector[119] += 1.0
            if subtype == 1:
                vector[137] += 1.0
            elif subtype == 2:
                vector[137] += 1.0
            elif subtype == 3:
                vector[137] += 1.0
        else:
            if heroes:
                vector[50] = 1.0
            if gameClass:
                vector[120] += 1.0
            if subtype == 1:
                vector[138] += 1.0
            elif subtype == 2:
                vector[138] += 1.0
            elif subtype == 3:
                vector[138] += 1.0
    elif name == '6':
        # Chen
        if didWin:
            if heroes:
                vector[51] = 1.0
            if gameClass:
                vector[119] += 1.0
            if subtype == 1:
                vector[135] += 1.0
            elif subtype == 2:
                vector[137] += 1.0
            elif subtype == 3:
                vector[137] += 1.0
        else:
            if heroes:
                vector[52] = 1.0
            if gameClass:
                vector[120] += 1.0
            if subtype == 1:
                vector[136] += 1.0
            elif subtype == 2:
                vector[138] += 1.0
            elif subtype == 3:
                vector[138] += 1.0
    elif name == '44':
        # Cho
        if didWin:
            if heroes:
                vector[53] = 1.0
            if gameClass:
                vector[119] += 1.0
            if subtype == 1:
                vector[135] += 1.0
            elif subtype == 2:
                vector[135] += 1.0
            elif subtype == 3:
                vector[137] += 1.0
        else:
            if heroes:
                vector[54] = 1.0
            if gameClass:
                vector[120] += 1.0
            if subtype == 1:
                vector[136] += 1.0
            elif subtype == 2:
                vector[136] += 1.0
            elif subtype == 3:
                vector[138] += 1.0
    elif name == '50':
        # Dehaka
        if didWin:
            if heroes:
                vector[55] = 1.0
            if gameClass:
                vector[119] += 1.0
            if subtype == 1:
                vector[135] += 1.0
            elif subtype == 2:
                vector[137] += 1.0
            elif subtype == 3:
                vector[137] += 1.0
        else:
            if heroes:
                vector[56] = 1.0
            if gameClass:
                vector[120] += 1.0
            if subtype == 1:
                vector[136] += 1.0
            elif subtype == 2:
                vector[138] += 1.0
            elif subtype == 3:
                vector[138] += 1.0
    elif name == '7':
        # Diablo
        if didWin:
            if heroes:
                vector[57] = 1.0
            if gameClass:
                vector[119] += 1.0
            if subtype == 1:
                vector[135] += 1.0
            elif subtype == 2:
                vector[137] += 1.0
            elif subtype == 3:
                vector[147] += 1.0
        else:
            if heroes:
                vector[58] = 1.0
            if gameClass:
                vector[120] += 1.0
           if subtype == 1:
                vector[136] += 1.0
            elif subtype == 2:
                vector[138] += 1.0
            elif subtype == 3:
                vector[148] += 1.0
    elif name == '8':
        # E.T.C.
        if didWin:
            if heroes:
                vector[59] = 1.0
            if gameClass:
                vector[119] += 1.0
            if subtype == 1:
                vector[135] += 1.0
            elif subtype == 2:
                vector[135] += 1.0
            elif subtype == 3:
                vector[137] += 1.0
        else:
            if heroes:
                vector[60] = 1.0
            if gameClass:
                vector[120] += 1.0
            if subtype == 1:
                vector[136] += 1.0
            elif subtype == 2:
                vector[136] += 1.0
            elif subtype == 3:
                vector[138] += 1.0
    elif name == '13':
        # Johanna
        if didWin:
            if heroes:
                vector[61] = 1.0
            if gameClass:
                vector[119] += 1.0
            if subtype == 1:
                vector[135] += 1.0
            elif subtype == 2:
                vector[135] += 1.0
            elif subtype == 3:
                vector[137] += 1.0
        else:
            if heroes:
                vector[62] = 1.0
            if gameClass:
                vector[120] += 1.0
            if subtype == 1:
                vector[136] += 1.0
            elif subtype == 2:
                vector[136] += 1.0
            elif subtype == 3:
                vector[138] += 1.0
    elif name == '17':
        # Leoric
        if didWin:
            if heroes:
                vector[63] = 1.0
            if gameClass:
                vector[119] += 1.0
            if subtype == 1:
                vector[137] += 1.0
            elif subtype == 2:
                vector[137] += 1.0
            elif subtype == 3:
                vector[137] += 1.0
        else:
            if heroes:
                vector[64] = 1.0
            if gameClass:
                vector[120] += 1.0
            if subtype == 1:
                vector[138] += 1.0
            elif subtype == 2:
                vector[138] += 1.0
            elif subtype == 3:
                vector[138] += 1.0
    elif name == '20':
        # Muradin
        if didWin:
            if heroes:
                vector[65] = 1.0
            if gameClass:
                vector[119] += 1.0
            if subtype == 1:
                vector[135] += 1.0
            elif subtype == 2:
                vector[135] += 1.0
            elif subtype == 3:
                vector[137] += 1.0
        else:
            if heroes:
                vector[66] = 1.0
            if gameClass:
                vector[120] += 1.0
            if subtype == 1:
                vector[136] += 1.0
            elif subtype == 2:
                vector[136] += 1.0
            elif subtype == 3:
                vector[138] += 1.0
    elif name == '41':
        # Rexxar
        if didWin:
            if heroes:
                vector[67] = 1.0
            if gameClass:
                vector[121] += 1.0
            if subtype == 1:
                vector[135] += 1.0
            elif subtype == 2:
                vector[137] += 1.0
            elif subtype == 3:
                vector[147] += 1.0
        else:
            if heroes:
                vector[68] = 1.0
            if gameClass:
                vector[122] += 1.0
            if subtype == 1:
                vector[136] += 1.0
            elif subtype == 2:
                vector[138] += 1.0
            elif subtype == 3:
                vector[148] += 1.0
    elif name == '27':
        # Sonya
        if didWin:
            if heroes:
                vector[69] = 1.0
            if gameClass:
                vector[119] += 1.0
            if subtype == 1:
                vector[137] += 1.0
            elif subtype == 2:
                vector[139] += 1.0
            elif subtype == 3:
                vector[137] += 1.0
        else:
            if heroes:
                vector[70] = 1.0
            if gameClass:
                vector[120] += 1.0
            if subtype == 1:
                vector[138] += 1.0
            elif subtype == 2:
                vector[140] += 1.0
            elif subtype == 3:
                vector[138] += 1.0
    elif name == '28':
        # Stitches
        if didWin:
            if heroes:
                vector[71] = 1.0
            if gameClass:
                vector[119] += 1.0
            if subtype == 1:
                vector[135] += 1.0
            elif subtype == 2:
                vector[135] += 1.0
            elif subtype == 3:
                vector[137] += 1.0
        else:
            if heroes:
                vector[72] = 1.0
            if gameClass:
                vector[120] += 1.0
            if subtype == 1:
                vector[136] += 1.0
            elif subtype == 2:
                vector[136] += 1.0
            elif subtype == 3:
                vector[138] += 1.0
    elif name == '35':
        # Tyrael
        if didWin:
            if heroes:
                vector[73] = 1.0
            if gameClass:
                vector[119] += 1.0
            if subtype == 1:
                vector[137] += 1.0
            elif subtype == 2:
                vector[137] += 1.0
            elif subtype == 3:
                vector[147] += 1.0
        else:
            if heroes:
                vector[74] = 1.0
            if gameClass:
                vector[120] += 1.0
            if subtype == 1:
                vector[138] += 1.0
            elif subtype == 2:
                vector[138] += 1.0
            elif subtype == 3:
                vector[148] += 1.0
    elif name == '57':
        # Zarya
        if didWin:
            if heroes:
                vector[75] = 1.0
            if gameClass:
                vector[121] += 1.0
            if subtype == 1:
                vector[135] += 1.0
            elif subtype == 2:
                vector[137] += 1.0
            elif subtype == 3:
                vector[147] += 1.0
        else:
            if heroes:
                vector[76] = 1.0
            if gameClass:
                vector[122] += 1.0
            if subtype == 1:
                vector[136] += 1.0
            elif subtype == 2:
                vector[138] += 1.0
            elif subtype == 3:
                vector[148] += 1.0
    elif name == '55':
        # Auriel
        if didWin:
            if heroes:
                vector[77] = 1.0
            if gameClass:
                vector[129] += 1.0
            if subtype == 1:
                vector[139] += 1.0
            elif subtype == 2:
                vector[143] += 1.0
            elif subtype == 3:
                vector[145] += 1.0
        else:
            if heroes:
                vector[78] = 1.0
            if gameClass:
                vector[130] += 1.0
            if subtype == 1:
                vector[140] += 1.0
            elif subtype == 2:
                vector[144] += 1.0
            elif subtype == 3:
                vector[146] += 1.0
    elif name == '5':
        # Brightwing
        if didWin:
            if heroes:
                vector[79] = 1.0
            if gameClass:
                vector[129] += 1.0
            if subtype == 1:
                vector[139] += 1.0
            elif subtype == 2:
                vector[141] += 1.0
            elif subtype == 3:
                vector[145] += 1.0
        else:
            if heroes:
                vector[80] = 1.0
            if gameClass:
                vector[130] += 1.0
            if subtype == 1:
                vector[140] += 1.0
            elif subtype == 2:
                vector[142] += 1.0
            elif subtype == 3:
                vector[146] += 1.0
    elif name == '16':
        # Kharazim
        if didWin:
            if heroes:
                vector[81] = 1.0
            if gameClass:
                vector[127] += 1.0
            if subtype == 1:
                vector[139] += 1.0
            elif subtype == 2:
                vector[141] += 1.0
            elif subtype == 3:
                vector[145] += 1.0
        else:
            if heroes:
                vector[82] = 1.0
            if gameClass:
                vector[128] += 1.0
            if subtype == 1:
                vector[140] += 1.0
            elif subtype == 2:
                vector[142] += 1.0
            elif subtype == 3:
                vector[146] += 1.0
    elif name == '18':
        # Li Li
        if didWin:
            if heroes:
                vector[83] = 1.0
            if gameClass:
                vector[129] += 1.0
            if subtype == 1:
                vector[139] += 1.0
            elif subtype == 2:
                vector[141] += 1.0
            elif subtype == 3:
                vector[145] += 1.0
        else:
            if heroes:
                vector[84] = 1.0
            if gameClass:
                vector[130] += 1.0
            if subtype == 1:
                vector[140] += 1.0
            elif subtype == 2:
                vector[142] += 1.0
            elif subtype == 3:
                vector[146] += 1.0
    elif name == '42':
        # Lt. Morales
        if didWin:
            if heroes:
                vector[85] = 1.0
            if gameClass:
                vector[129] += 1.0
            if subtype == 1:
                vector[139] += 1.0
            elif subtype == 2:
                vector[141] += 1.0
            elif subtype == 3:
                vector[145] += 1.0
        else:
            if heroes:
                vector[86] = 1.0
            if gameClass:
                vector[130] += 1.0
            if subtype == 1:
                vector[140] += 1.0
            elif subtype == 2:
                vector[142] += 1.0
            elif subtype == 3:
                vector[146] += 1.0
    elif name == '19':
        # Malfurion
        if didWin:
            if heroes:
                vector[87] = 1.0
            if gameClass:
                vector[129] += 1.0
            if subtype == 1:
                vector[139] += 1.0
            elif subtype == 2:
                vector[141] += 1.0
            elif subtype == 3:
                vector[145] += 1.0
        else:
            if heroes:
                vector[88] = 1.0
            if gameClass:
                vector[130] += 1.0
            if subtype == 1:
                vector[140] += 1.0
            elif subtype == 2:
                vector[142] += 1.0
            elif subtype == 3:
                vector[146] += 1.0
    elif name == '25':
        # Rehgar
        if didWin:
            if heroes:
                vector[89] = 1.0
            if gameClass:
                vector[127] += 1.0
            if subtype == 1:
                vector[139] += 1.0
            elif subtype == 2:
                vector[143] += 1.0
            elif subtype == 3:
                vector[145] += 1.0
        else:
            if heroes:
                vector[90] = 1.0
            if gameClass:
                vector[128] += 1.0
            if subtype == 1:
                vector[140] += 1.0
            elif subtype == 2:
                vector[144] += 1.0
            elif subtype == 3:
                vector[146] += 1.0
    elif name == '30':
        # Tassadar
        if didWin:
            if heroes:
                vector[91] = 1.0
            if gameClass:
                vector[129] += 1.0
            if subtype == 1:
                vector[141] += 1.0
            elif subtype == 2:
                vector[157] += 1.0
            elif subtype == 3:
                vector[145] += 1.0
        else:
            if heroes:
                vector[92] = 1.0
            if gameClass:
                vector[130] += 1.0
            if subtype == 1:
                vector[142] += 1.0
            elif subtype == 2:
                vector[158] += 1.0
            elif subtype == 3:
                vector[146] += 1.0
    elif name == '36':
        # Tyrande
        if didWin:
            if heroes:
                vector[93] = 1.0
            if gameClass:
                vector[129] += 1.0
            if subtype == 1:
                vector[139] += 1.0
            elif subtype == 2:
                vector[157] += 1.0
            elif subtype == 3:
                vector[145] += 1.0
        else:
            if heroes:
                vector[94] = 1.0
            if gameClass:
                vector[130] += 1.0
            if subtype == 1:
                vector[140] += 1.0
            elif subtype == 2:
                vector[158] += 1.0
            elif subtype == 3:
                vector[146] += 1.0
    elif name == '37':
        # Uther
        if didWin:
            if heroes:
                vector[95] = 1.0
            if gameClass:
                vector[127] += 1.0
            if subtype == 1:
                vector[139] += 1.0
            elif subtype == 2:
                vector[143] += 1.0
            elif subtype == 3:
                vector[145] += 1.0
        else:
            if heroes:
                vector[96] = 1.0
            if gameClass:
                vector[128] += 1.0
            if subtype == 1:
                vector[140] += 1.0
            elif subtype == 2:
                vector[144] += 1.0
            elif subtype == 3:
                vector[146] += 1.0
    elif name == '1':
        # Abathur
        if didWin:
            if heroes:
                vector[97] = 1.0
            if gameClass:
                vector[131] += 1.0
            if subtype == 1:
                vector[151] += 1.0
            elif subtype == 2:
                vector[159] += 1.0
            elif subtype == 3:
                vector[139] += 1.0
        else:
            if heroes:
                vector[98] = 1.0
            if gameClass:
                vector[132] += 1.0
            if subtype == 1:
                vector[152] += 1.0
            elif subtype == 2:
                vector[160] += 1.0
            elif subtype == 3:
                vector[140] += 1.0
    elif name == '4':
        # Azmodan
        if didWin:
            if heroes:
                vector[99] = 1.0
            if gameClass:
                vector[133] += 1.0
            if subtype == 1:
                vector[149] += 1.0
            elif subtype == 2:
                vector[155] += 1.0
            elif subtype == 3:
                vector[139] += 1.0
        else:
            if heroes:
                 vector[100] = 1.0
            if gameClass:
                vector[134] += 1.0
            if subtype == 1:
                vector[150] += 1.0
            elif subtype == 2:
                vector[156] += 1.0
            elif subtype == 3:
                vector[140] += 1.0
    elif name == '10':
        # Gazlowe
        if didWin:
            if heroes:
                vector[101] = 1.0
            if gameClass:
                vector[131] += 1.0
            if subtype == 1:
                vector[149] += 1.0
            elif subtype == 2:
                vector[155] += 1.0
            elif subtype == 3:
                vector[139] += 1.0
        else:
            if heroes:
                vector[102] = 1.0
            if gameClass:
                vector[132] += 1.0
            if subtype == 1:
                vector[150] += 1.0
            elif subtype == 2:
                vector[156] += 1.0
            elif subtype == 3:
                vector[140] += 1.0
    elif name == '53':
        # Medivh
        if didWin:
            if heroes:
                vector[103] = 1.0
            if gameClass:
                vector[133] += 1.0
            if subtype == 1:
                vector[151] += 1.0
            elif subtype == 2:
                vector[157] += 1.0
            elif subtype == 3:
                vector[141] += 1.0
        else:
            if heroes:
                vector[104] = 1.0
            if gameClass:
                vector[135] += 1.0
            if subtype == 1:
                vector[152] += 1.0
            elif subtype == 2:
                vector[158] += 1.0
            elif subtype == 3:
                vector[142] += 1.0
    elif name == '21':
        # Murky
        if didWin:
            if heroes:
                vector[105] = 1.0
            if gameClass:
                vector[131] += 1.0
            if subtype == 1:
                vector[151] += 1.0
            elif subtype == 2:
                vector[155] += 1.0
            elif subtype == 3:
                vector[139] += 1.0
        else:
            if heroes:
                vector[106] = 1.0
            if gameClass:
                vector[132] += 1.0
            if subtype == 1:
                vector[152] += 1.0
            elif subtype == 2:
                vector[156] += 1.0
            elif subtype == 3:
                vector[140] += 1.0
    elif name == '22':
        # Nazeebo
        if didWin:
            if heroes:
                vector[107] = 1.0
            if gameClass:
                vector[133] += 1.0
            if subtype == 1:
                vector[149] += 1.0
            elif subtype == 2:
                vector[149] += 1.0
            elif subtype == 3:
                vector[139] += 1.0
        else:
            if heroes:
                vector[108] = 1.0
            if gameClass:
                vector[134] += 1.0
            if subtype == 1:
                vector[150] += 1.0
            elif subtype == 2:
                vector[150] += 1.0
            elif subtype == 3:
                vector[140] += 1.0
    elif name == '26':
        # Sgt. Hammer
        if didWin:
            if heroes:
                vector[109] = 1.0
            if gameClass:
                vector[133] += 1.0
            if subtype == 1:
                vector[149] += 1.0
            elif subtype == 2:
                vector[155] += 1.0
            elif subtype == 3:
                vector[141] += 1.0
        else:
            if heroes:
                vector[110] = 1.0
            if gameClass:
                vector[134] += 1.0
            if subtype == 1:
                vector[150] += 1.0
            elif subtype == 2:
                vector[156] += 1.0
            elif subtype == 3:
                vector[142] += 1.0
    elif name == '29':
        # Sylvanas
        if didWin:
            if heroes:
                vector[111] = 1.0
            if gameClass:
                vector[133] += 1.0
            if subtype == 1:
                vector[149] += 1.0
            elif subtype == 2:
                vector[155] += 1.0
            elif subtype == 3:
                vector[139] += 1.0
        else:
            if heroes:
                vector[112] = 1.0
            if gameClass:
                vector[134] += 1.0
            if subtype == 1:
                vector[150] += 1.0
            elif subtype == 2:
                vector[156] += 1.0
            elif subtype == 3:
                vector[140] += 1.0
    elif name == '32':
        # The Lost Vikings
        if didWin:
            if heroes:
                vector[113] = 1.0
            if gameClass:
                vector[133] += 1.0
            if subtype == 1:
                vector[151] += 1.0
            elif subtype == 2:
                vector[159] += 1.0
            elif subtype == 3:
                vector[135] += 1.0
        else:
            if heroes:
                vector[114] = 1.0
            if gameClass:
                vector[134] += 1.0
            if subtype == 1:
                vector[152] += 1.0
            elif subtype == 2:
                vector[160] += 1.0
            elif subtype == 3:
                vector[136] += 1.0
    elif name == '49':
        # Xul
        if didWin:
            if heroes:
                vector[115] = 1.0
            if gameClass:
                vector[131] += 1.0
            if subtype == 1:
                vector[149] += 1.0
            elif subtype == 2:
                vector[155] += 1.0
            elif subtype == 3:
                vector[139] += 1.0
        else:
            if heroes:
                 vector[116] = 1.0
            if gameClass:
                vector[132] += 1.0
            if subtype == 1:
                vector[150] += 1.0
            elif subtype == 2:
                vector[156] += 1.0
            elif subtype == 3:
                vector[140] += 1.0
    elif name == '39':
        # Zagara
        if didWin:
            if heroes:
                vector[117] = 1.0
            if gameClass:
                vector[133] += 1.0
            if subtype == 1:
                vector[149] += 1.0
            elif subtype == 2:
                vector[155] += 1.0
            elif subtype == 3:
                vector[139] += 1.0
        else:
            if heroes:
                vector[118] = 1.0
            if gameClass:
                vector[134] += 1.0
            if subtype == 1:
                vector[150] += 1.0
            elif subtype == 2:
                vector[156] += 1.0
            elif subtype == 3:
                vector[140] += 1.0
    else:
        print "panicBasket panicBasket panicBasket"
        print name
    pass



def MarkMap(mapName, vector):
    mapName = str(mapName)
    if mapName == '1001':
        vector[161] = 1.0
    elif mapName == '1002':
        vector[162] = 1.0
    elif mapName == '1012':
        vector[163] = 1.0
    elif mapName == '1003':
        vector[164] = 1.0
    elif mapName == '1004':
        vector[165] = 1.0
    elif mapName == '1005':
        vector[166] = 1.0
    elif mapName == '1007':
        vector[167] = 1.0
    elif mapName == '1008':
        vector[168] = 1.0
    elif mapName == '1009':
        vector[169] = 1.0
    elif mapName == '1010':
        vector[170] = 1.0
    elif mapName == '1013':
        vector[171] = 1.0
    else:
        print "wat"
        print mapName

    pass




hl = pickle.load(open("datasets/hl_list.data", "rb"))
vectors = dict()
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
    if (Team1AvgMMR > 3200 or Team2AvgMMR > 3200) or (Team1AvgMMR < 2200 or Team2AvgMMR < 2200):
        doNothing = 0
    elif Team2AvgMMR is not 0.0 and Team1AvgMMR is not 0.0:
        noPotato += 1
        vectors[i] = [0.0] * 166
        ID = replay[0][0]
        MarkMap(replay[0][2], vectors[i])
        for player in replay[1:11]:
            FillVectorHeroless(player, vectors[i], ID)
        Team2AvgMMR = math.log(Team2AvgMMR)
        Team1AvgMMR = math.log(Team1AvgMMR)

        if int(ID) % 2 is 0:
            ##Team "1" won

            vectors[i][164] = Team1AvgMMR
            vectors[i][165] = Team2AvgMMR
        else:
            #Team "2" won
            vectors[i][164] = Team2AvgMMR
            vectors[i][165] = Team1AvgMMR
    i+=1
f1 = open("datasets/hl_data_heroless_midmmr.train", "wb")
f2 = open("datasets/hl_data_heroless_midmmr.dev", "wb")
for vector in vectors.itervalues():
    s = str(vector[0]) + " "
    i = 1
    for feature in vector[1:]:
        if i is 165:
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
print noPotato


