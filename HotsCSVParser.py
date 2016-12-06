import csv
import pickle
import random

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

def FillVector(dict, vector, ID):
    name = dict[1]
    win = str2bool(dict[4])
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
    if name == '56':
        if didWin:
            vector[1] = 1.0
        else:
            vector[2] = 1.0
    elif name == '52':
        if didWin:
            vector[3] = 1.0
        else:
            vector[4] = 1.0
    elif name == '9':
        if didWin:
            vector[5] = 1.0
        else:
            vector[6] = 1.0
    elif name == '45':
        if didWin:
            vector[7] = 1.0
        else:
            vector[8] = 1.0
    elif name == '47':
        if didWin:
            vector[9] = 1.0
        else:
            vector[10] = 1.0
    elif name == '54':
        if didWin:
            vector[11] = 1.0
        else:
            vector[12] = 1.0
    elif name == '11':
        if didWin:
            vector[13] = 1.0
        else:
            vector[14] = 1.0
    elif name == '12':
        if didWin:
            vector[15] = 1.0
        else:
            vector[16] = 1.0
    elif name == '14':
        if didWin:
            vector[17] = 1.0
        else:
            vector[18] = 1.0
    elif name == '15':
        if didWin:
            vector[19] = 1.0
        else:
            vector[20] = 1.0
    elif name == '48':
        if didWin:
            vector[21] = 1.0
        else:
            vector[22] = 1.0
    elif name == '46':
        if didWin:
            vector[23] = 1.0
        else:
            vector[24] = 1.0
    elif name == '23':
        if didWin:
            vector[25] = 1.0
        else:
            vector[26] = 1.0
    elif name == '24':
        if didWin:
            vector[27] = 1.0
        else:
            vector[28] = 1.0
    elif name == '58':
        if didWin:
            vector[29] = 1.0
        else:
            vector[30] = 1.0
    elif name == '31':
        if didWin:
            vector[31] = 1.0
        else:
            vector[32] = 1.0
    elif name == '33':
        if didWin:
            vector[33] = 1.0
        else:
            vector[34] = 1.0
    elif name == '51':
        if didWin:
            vector[35] = 1.0
        else:
            vector[36] = 1.0
    elif name == '34':
        if didWin:
            vector[37] = 1.0
        else:
            vector[38] = 1.0
    elif name == '38':
        if didWin:
            vector[39] = 1.0
        else:
            vector[40] = 1.0
    elif name == '59':
        if didWin:
            vector[41] = 1.0
        else:
            vector[42] = 1.0
    elif name == '40':
        if didWin:
            vector[43] = 1.0
        else:
            vector[44] = 1.0
    elif name == '2':
        if didWin:
            vector[45] = 1.0
        else:
            vector[46] = 1.0
    elif name == '43':
        if didWin:
            vector[47] = 1.0
        else:
            vector[48] = 1.0
    elif name == '3':
        if didWin:
            vector[49] = 1.0
        else:
            vector[50] = 1.0
    elif name == '6':
        if didWin:
            vector[51] = 1.0
        else:
            vector[52] = 1.0
    elif name == '44':
        if didWin:
            vector[53] = 1.0
        else:
            vector[54] = 1.0
    elif name == '50':
        if didWin:
            vector[55] = 1.0
        else:
            vector[56] = 1.0
    elif name == '7':
        if didWin:
            vector[57] = 1.0
        else:
            vector[58] = 1.0
    elif name == '8':
        if didWin:
            vector[59] = 1.0
        else:
            vector[60] = 1.0
    elif name == '13':
        if didWin:
            vector[61] = 1.0
        else:
            vector[62] = 1.0
    elif name == '17':
        if didWin:
            vector[63] = 1.0
        else:
            vector[64] = 1.0
    elif name == '20':
        if didWin:
            vector[65] = 1.0
        else:
            vector[66] = 1.0
    elif name == '41':
        if didWin:
            vector[67] = 1.0
        else:
            vector[68] = 1.0
    elif name == '27':
        if didWin:
            vector[69] = 1.0
        else:
            vector[70] = 1.0
    elif name == '28':
        if didWin:
            vector[71] = 1.0
        else:
            vector[72] = 1.0
    elif name == '35':
        #if korean == autowin
        if didWin:
            vector[73] = 1.0
        else:
            vector[74] = 1.0
    elif name == '57':
        if didWin:
            vector[75] = 1.0
        else:
            vector[76] = 1.0
    elif name == '55':
        if didWin:
            vector[77] = 1.0
        else:
            vector[78] = 1.0
    elif name == '5':
        if didWin:
            vector[79] = 1.0
        else:
            vector[80] = 1.0
    elif name == '16':
        if didWin:
            vector[81] = 1.0
        else:
            vector[82] = 1.0
    elif name == '18':
        if didWin:
            vector[83] = 1.0
        else:
            vector[84] = 1.0
    elif name == '42':
        if didWin:
            vector[85] = 1.0
        else:
            vector[86] = 1.0
    elif name == '19':
        if didWin:
            vector[87] = 1.0
        else:
            vector[88] = 1.0
    elif name == '25':
        if didWin:
            vector[89] = 1.0
        else:
            vector[90] = 1.0
    elif name == '30':
        if didWin:
            vector[91] = 1.0
        else:
            vector[92] = 1.0
    elif name == '36':
        if didWin:
            vector[93] = 1.0
        else:
            vector[94] = 1.0
    elif name == '37':
        if didWin:
            vector[95] = 1.0
        else:
            vector[96] = 1.0
    elif name == '1':
        if didWin:
            vector[97] = 1.0
        else:
            vector[98] = 1.0
    elif name == '4':
        if didWin:
            vector[99] = 1.0
        else:
            vector[100] = 1.0
    elif name == '10':
        if didWin:
            vector[101] = 1.0
        else:
            vector[102] = 1.0
    elif name == '53':
        if didWin:
            vector[103] = 1.0
        else:
            vector[104] = 1.0
    elif name == '21':
        if didWin:
            vector[105] = 1.0
        else:
            vector[106] = 1.0
    elif name == '22':
        if didWin:
            vector[107] = 1.0
        else:
            vector[108] = 1.0
    elif name == '26':
        if didWin:
            vector[109] = 1.0
        else:
            vector[110] = 1.0
    elif name == '29':
        if didWin:
            vector[111] = 1.0
        else:
            vector[112] = 1.0
    elif name == '32':
        if didWin:
            vector[113] = 1.0
        else:
            vector[114] = 1.0
    elif name == '49':
        if didWin:
            vector[115] = 1.0
        else:
            vector[116] = 1.0
    elif name == '39':
        if didWin:
            vector[117] = 1.0
        else:
            vector[118] = 1.0
    else:
        print "panicBasket panicBasket panicBasket"
        print name
    pass









def FillVectorDetailed(dict, vector, ID):
    name = dict[2]
    win = str2bool(dict[4])
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
    if name == '56':
        if didWin:
            vector[1] = 1.0
            vector[123] += 1.0
            vector[143] += 1.0
        else:
            vector[2] = 1.0
            vector[124] += 1.0
            vector[144] += 1.0
    elif name == '52':
        if didWin:
            vector[3] = 1.0
            vector[125] += 1.0
            vector[145] += 1.0
        else:
            vector[4] = 1.0
            vector[126] += 1.0
            vector[146] += 1.0
    elif name == '9':
        if didWin:
            vector[5] = 1.0
            vector[125] += 1.0
            vector[147] += 1.0
        else:
            vector[6] = 1.0
            vector[126] += 1.0
            vector[148] += 1.0
    elif name == '45':
        if didWin:
            vector[7] = 1.0
            vector[125] += 1.0
            vector[147] += 1.0
        else:
            vector[8] = 1.0
            vector[126] += 1.0
            vector[148] += 1.0
    elif name == '47':
        if didWin:
            vector[9] = 1.0
            vector[125] += 1.0
            vector[147] += 1.0
        else:
            vector[10] = 1.0
            vector[126] += 1.0
            vector[148] += 1.0
    elif name == '54':
        if didWin:
            vector[11] = 1.0
            vector[125] += 1.0
            vector[147] += 1.0
        else:
            vector[12] = 1.0
            vector[125] += 1.0
            vector[148] += 1.0
    elif name == '11':
        if didWin:
            vector[13] = 1.0
            vector[123] += 1.0
            vector[147] += 1.0
        else:
            vector[14] = 1.0
            vector[124] += 1.0
            vector[148] += 1.0
    elif name == '12':
        if didWin:
            vector[15] = 1.0
            vector[125] += 1.0
            vector[145] += 1.0
        else:
            vector[16] = 1.0
            vector[126] += 1.0
            vector[146] += 1.0
    elif name == '14':
        if didWin:
            vector[17] = 1.0
            vector[125] += 1.0
            vector[145] += 1.0
        else:
            vector[18] = 1.0
            vector[126] += 1.0
            vector[146] += 1.0
    elif name == '15':
        if didWin:
            vector[19] = 1.0
            vector[123] += 1.0
            vector[143] += 1.0
        else:
            vector[20] = 1.0
            vector[124] += 1.0
            vector[144] += 1.0
    elif name == '48':
        if didWin:
            vector[21] = 1.0
            vector[125] += 1.0
            vector[145] += 1.0
        else:
            vector[22] = 1.0
            vector[126] += 1.0
            vector[146] += 1.0
    elif name == '46':
        if didWin:
            vector[23] = 1.0
            vector[125] += 1.0
            vector[147] += 1.0
        else:
            vector[24] = 1.0
            vector[126] += 1.0
            vector[148] += 1.0
    elif name == '23':
        if didWin:
            vector[25] = 1.0
            vector[125] += 1.0
            vector[143] += 1.0
        else:
            vector[26] = 1.0
            vector[126] += 1.0
            vector[144] += 1.0
    elif name == '24':
        if didWin:
            vector[27] = 1.0
            vector[125] += 1.0
            vector[147] += 1.0
        else:
            vector[28] = 1.0
            vector[126] += 1.0
            vector[148] += 1.0
    elif name == '58':
        if didWin:
            vector[29] = 1.0
            vector[123] += 1.0
            vector[143] += 1.0
        else:
            vector[30] = 1.0
            vector[124] += 1.0
            vector[144] += 1.0
    elif name == '31':
        if didWin:
            vector[31] = 1.0
            vector[123] += 1.0
            vector[143] += 1.0
        else:
            vector[32] = 1.0
            vector[124] += 1.0
            vector[144] += 1.0
    elif name == '33':
        if didWin:
            vector[33] = 1.0
            vector[123] += 1.0
            vector[147] += 1.0
        else:
            vector[34] = 1.0
            vector[124] += 1.0
            vector[148] += 1.0
    elif name == '51':
        if didWin:
            vector[35] = 1.0
            vector[125] += 1.0
            vector[147] += 1.0
        else:
            vector[36] = 1.0
            vector[126] += 1.0
            vector[148] += 1.0
    elif name == '34':
        if didWin:
            vector[37] = 1.0
            vector[125] += 1.0
            vector[147] += 1.0
        else:
            vector[38] = 1.0
            vector[126] += 1.0
            vector[148] += 1.0
    elif name == '38':
        if didWin:
            vector[39] = 1.0
            vector[125] += 1.0
            vector[147] += 1.0
        else:
            vector[40] = 1.0
            vector[126] += 1.0
            vector[148] += 1.0
    elif name == '59':
        if didWin:
            vector[41] = 1.0
            # class?
            # vector[123] += 1.0
            vector[137] += 1.0
        else:
            vector[42] = 1.0
            # class?
            # vector[123] += 1.0
            vector[138] += 1.0
    elif name == '40':
        if didWin:
            vector[43] = 1.0
            vector[123] += 1.0
            vector[143] += 1.0
        else:
            vector[44] = 1.0
            vector[124] += 1.0
            vector[144] += 1.0
    elif name == '2':
        if didWin:
            vector[45] = 1.0
            vector[119] += 1.0
            vector[137] += 1.0
        else:
            vector[46] = 1.0
            vector[120] += 1.0
            vector[138] += 1.0
    elif name == '43':
        if didWin:
            vector[47] = 1.0
            vector[119] += 1.0
            vector[137] += 1.0
        else:
            vector[48] = 1.0
            vector[120] += 1.0
            vector[138] += 1.0
    elif name == '3':
        if didWin:
            vector[49] = 1.0
            vector[119] += 1.0
            vector[137] += 1.0
        else:
            vector[50] = 1.0
            vector[120] += 1.0
            vector[138] += 1.0
    elif name == '6':
        if didWin:
            vector[51] = 1.0
            vector[119] += 1.0
            vector[135] += 1.0
        else:
            vector[52] = 1.0
            vector[120] += 1.0
            vector[136] += 1.0
    elif name == '44':
        if didWin:
            vector[53] = 1.0
            vector[119] += 1.0
            vector[135] += 1.0
        else:
            vector[54] = 1.0
            vector[120] += 1.0
            vector[136] += 1.0
    elif name == '50':
        if didWin:
            vector[55] = 1.0
            vector[119] += 1.0
            vector[135] += 1.0
        else:
            vector[56] = 1.0
            vector[120] += 1.0
            vector[136] += 1.0
    elif name == '7':
        if didWin:
            vector[57] = 1.0
            vector[119] += 1.0
            vector[135] += 1.0
        else:
            vector[58] = 1.0
            vector[120] += 1.0
            vector[136] += 1.0
    elif name == '8':
        if didWin:
            vector[59] = 1.0
            vector[119] += 1.0
            vector[135] += 1.0
        else:
            vector[60] = 1.0
            vector[120] += 1.0
            vector[136] += 1.0
    elif name == '13':
        if didWin:
            vector[61] = 1.0
            vector[119] += 1.0
            vector[135] += 1.0
        else:
            vector[62] = 1.0
            vector[120] += 1.0
            vector[136] += 1.0
    elif name == '17':
        if didWin:
            vector[63] = 1.0
            vector[119] += 1.0
            vector[137] += 1.0
        else:
            vector[64] = 1.0
            vector[120] += 1.0
            vector[138] += 1.0
    elif name == '20':
        if didWin:
            vector[65] = 1.0
            vector[119] += 1.0
            vector[135] += 1.0
        else:
            vector[66] = 1.0
            vector[120] += 1.0
            vector[136] += 1.0
    elif name == '41':
        if didWin:
            vector[67] = 1.0
            vector[121] += 1.0
            vector[135] += 1.0
        else:
            vector[68] = 1.0
            vector[122] += 1.0
            vector[136] += 1.0
    elif name == '27':
        if didWin:
            vector[69] = 1.0
            vector[119] += 1.0
            vector[137] += 1.0
        else:
            vector[70] = 1.0
            vector[120] += 1.0
            vector[138] += 1.0
    elif name == '28':
        if didWin:
            vector[71] = 1.0
            vector[119] += 1.0
            vector[135] += 1.0
        else:
            vector[72] = 1.0
            vector[120] += 1.0
            vector[136] += 1.0
    elif name == '35':
        #if korean == autowin
        if didWin:
            vector[73] = 1.0
            vector[119] += 1.0
            vector[137] += 1.0
        else:
            vector[74] = 1.0
            vector[120] += 1.0
            vector[138] += 1.0
    elif name == '57':
        if didWin:
            vector[75] = 1.0
            vector[121] += 1.0
            vector[135] += 1.0
        else:
            vector[76] = 1.0
            vector[122] += 1.0
            vector[136] += 1.0
    elif name == '55':
        if didWin:
            vector[77] = 1.0
            vector[129] += 1.0
            vector[139] += 1.0
        else:
            vector[78] = 1.0
            vector[130] += 1.0
            vector[140] += 1.0
    elif name == '5':
        if didWin:
            vector[79] = 1.0
            vector[129] += 1.0
            vector[139] += 1.0
        else:
            vector[80] = 1.0
            vector[130] += 1.0
            vector[140] += 1.0
    elif name == '16':
        if didWin:
            vector[81] = 1.0
            vector[127] += 1.0
            vector[139] += 1.0
        else:
            vector[82] = 1.0
            vector[128] += 1.0
            vector[140] += 1.0
    elif name == '18':
        if didWin:
            vector[83] = 1.0
            vector[129] += 1.0
            vector[139] += 1.0
        else:
            vector[84] = 1.0
            vector[130] += 1.0
            vector[140] += 1.0
    elif name == '42':
        if didWin:
            vector[85] = 1.0
            vector[129] += 1.0
            vector[139] += 1.0
        else:
            vector[86] = 1.0
            vector[130] += 1.0
            vector[140] += 1.0
    elif name == '19':
        if didWin:
            vector[87] = 1.0
            vector[129] += 1.0
            vector[139] += 1.0
        else:
            vector[88] = 1.0
            vector[130] += 1.0
            vector[140] += 1.0
    elif name == '25':
        if didWin:
            vector[89] = 1.0
            vector[127] += 1.0
            vector[139] += 1.0
        else:
            vector[90] = 1.0
            vector[128] += 1.0
            vector[140] += 1.0
    elif name == '30':
        if didWin:
            vector[91] = 1.0
            vector[129] += 1.0
            vector[141] += 1.0
        else:
            vector[92] = 1.0
            vector[130] += 1.0
            vector[142] += 1.0
    elif name == '36':
        if didWin:
            vector[93] = 1.0
            vector[129] += 1.0
            vector[139] += 1.0
        else:
            vector[94] = 1.0
            vector[130] += 1.0
            vector[140] += 1.0
    elif name == '37':
        if didWin:
            vector[95] = 1.0
            vector[127] += 1.0
            vector[139] += 1.0
        else:
            vector[96] = 1.0
            vector[128] += 1.0
            vector[140] += 1.0
    elif name == '1':
        if didWin:
            vector[97] = 1.0
            # class?
            # vector[129] += 1.0
            vector[151] += 1.0
        else:
            vector[98] = 1.0
            # class?
            # vector[129] += 1.0
            vector[152] += 1.0
    elif name == '4':
        if didWin:
            vector[99] = 1.0
            vector[133] += 1.0
            vector[149] += 1.0
        else:
            vector[100] = 1.0
            vector[134] += 1.0
            vector[150] += 1.0
    elif name == '10':
        if didWin:
            vector[101] = 1.0
            vector[131] += 1.0
            vector[149] += 1.0
        else:
            vector[102] = 1.0
            vector[132] += 1.0
            vector[150] += 1.0
    elif name == '53':
        if didWin:
            vector[103] = 1.0
            vector[133] += 1.0
            vector[151] += 1.0
        else:
            vector[104] = 1.0
            vector[135] += 1.0
            vector[152] += 1.0
    elif name == '21':
        if didWin:
            vector[105] = 1.0
            vector[131] += 1.0
            vector[151] += 1.0
        else:
            vector[106] = 1.0
            vector[132] += 1.0
            vector[152] += 1.0
    elif name == '22':
        if didWin:
            vector[107] = 1.0
            vector[133] += 1.0
            vector[149] += 1.0
        else:
            vector[108] = 1.0
            vector[134] += 1.0
            vector[150] += 1.0
    elif name == '26':
        if didWin:
            vector[109] = 1.0
            vector[133] += 1.0
            vector[149] += 1.0
        else:
            vector[110] = 1.0
            vector[134] += 1.0
            vector[150] += 1.0
    elif name == '29':
        if didWin:
            vector[111] = 1.0
            vector[133] += 1.0
            vector[149] += 1.0
        else:
            vector[112] = 1.0
            vector[134] += 1.0
            vector[150] += 1.0
    elif name == '32':
        if didWin:
            vector[113] = 1.0
            vector[133] += 1.0
            vector[151] += 1.0
        else:
            vector[114] = 1.0
            vector[134] += 1.0
            vector[152] += 1.0
    elif name == '49':
        if didWin:
            vector[115] = 1.0
            vector[131] += 1.0
            vector[149] += 1.0
        else:
            vector[116] = 1.0
            vector[132] += 1.0
            vector[150] += 1.0
    elif name == '39':
        if didWin:
            vector[117] = 1.0
            vector[133] += 1.0
            vector[149] += 1.0
        else:
            vector[118] = 1.0
            vector[134] += 1.0
            vector[150] += 1.0
    else:
        print "panicBasket panicBasket panicBasket"
        print name
    pass



def MarkMap(mapName, vector):
    mapName = str(mapName)
    if mapName == '1001':
        vector[153] = 1.0
    elif mapName == '1002':
        vector[154] = 1.0
    elif mapName == '1012':
        vector[155] = 1.0
    elif mapName == '1003':
        vector[156] = 1.0
    elif mapName == '1004':
        vector[157] = 1.0
    elif mapName == '1005':
        vector[158] = 1.0
    elif mapName == '1007':
        vector[159] = 1.0
    elif mapName == '1008':
        vector[160] = 1.0
    elif mapName == '1009':
        vector[161] = 1.0
    elif mapName == '1010':
        vector[162] = 1.0
    elif mapName == '1013':
        vector[163] = 1.0
    else:
        print "wat"
        print mapName

    pass




def FillVectorHeroless(dict, vector, ID):
    name = dict[2]
    win = str2bool(dict[4])
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
    if name == '56':
        if didWin:
            #vector[1] = 1.0
            vector[123] += 1.0
            vector[143] += 1.0
        else:
            #vector[2] = 1.0
            vector[124] += 1.0
            vector[144] += 1.0
    elif name == '52':
        if didWin:
            #vector[3] = 1.0
            vector[125] += 1.0
            vector[145] += 1.0
        else:
            #vector[4] = 1.0
            vector[126] += 1.0
            vector[146] += 1.0
    elif name == '9':
        if didWin:
            #vector[5] = 1.0
            vector[125] += 1.0
            vector[147] += 1.0
        else:
            #vector[6] = 1.0
            vector[126] += 1.0
            vector[148] += 1.0
    elif name == '45':
        if didWin:
            #vector[7] = 1.0
            vector[125] += 1.0
            vector[147] += 1.0
        else:
            #vector[8] = 1.0
            vector[126] += 1.0
            vector[148] += 1.0
    elif name == '47':
        if didWin:
            #vector[9] = 1.0
            vector[125] += 1.0
            vector[147] += 1.0
        else:
            #vector[10] = 1.0
            vector[126] += 1.0
            vector[148] += 1.0
    elif name == '54':
        if didWin:
            #vector[11] = 1.0
            vector[125] += 1.0
            vector[147] += 1.0
        else:
            #vector[12] = 1.0
            vector[125] += 1.0
            vector[148] += 1.0
    elif name == '11':
        if didWin:
            #vector[13] = 1.0
            vector[123] += 1.0
            vector[147] += 1.0
        else:
            #vector[14] = 1.0
            vector[124] += 1.0
            vector[148] += 1.0
    elif name == '12':
        if didWin:
            #vector[15] = 1.0
            vector[125] += 1.0
            vector[145] += 1.0
        else:
            #vector[16] = 1.0
            vector[126] += 1.0
            vector[146] += 1.0
    elif name == '14':
        if didWin:
            #vector[17] = 1.0
            vector[125] += 1.0
            vector[145] += 1.0
        else:
            #vector[18] = 1.0
            vector[126] += 1.0
            vector[146] += 1.0
    elif name == '15':
        if didWin:
            #vector[19] = 1.0
            vector[123] += 1.0
            vector[143] += 1.0
        else:
            #vector[20] = 1.0
            vector[124] += 1.0
            vector[144] += 1.0
    elif name == '48':
        if didWin:
            #vector[21] = 1.0
            vector[125] += 1.0
            vector[145] += 1.0
        else:
            #vector[22] = 1.0
            vector[126] += 1.0
            vector[146] += 1.0
    elif name == '46':
        if didWin:
            #vector[23] = 1.0
            vector[125] += 1.0
            vector[147] += 1.0
        else:
            #vector[24] = 1.0
            vector[126] += 1.0
            vector[148] += 1.0
    elif name == '23':
        if didWin:
            #vector[25] = 1.0
            vector[125] += 1.0
            vector[143] += 1.0
        else:
            #vector[26] = 1.0
            vector[126] += 1.0
            vector[144] += 1.0
    elif name == '24':
        if didWin:
            #vector[27] = 1.0
            vector[125] += 1.0
            vector[147] += 1.0
        else:
            #vector[28] = 1.0
            vector[126] += 1.0
            vector[148] += 1.0
    elif name == '58':
        if didWin:
            #vector[29] = 1.0
            vector[123] += 1.0
            vector[143] += 1.0
        else:
            #vector[30] = 1.0
            vector[124] += 1.0
            vector[144] += 1.0
    elif name == '31':
        if didWin:
            #vector[31] = 1.0
            vector[123] += 1.0
            vector[143] += 1.0
        else:
            #vector[32] = 1.0
            vector[124] += 1.0
            vector[144] += 1.0
    elif name == '33':
        if didWin:
            #vector[33] = 1.0
            vector[123] += 1.0
            vector[147] += 1.0
        else:
            #vector[34] = 1.0
            vector[124] += 1.0
            vector[148] += 1.0
    elif name == '51':
        if didWin:
            #vector[35] = 1.0
            vector[125] += 1.0
            vector[147] += 1.0
        else:
            #vector[36] = 1.0
            vector[126] += 1.0
            vector[148] += 1.0
    elif name == '34':
        if didWin:
            #vector[37] = 1.0
            vector[125] += 1.0
            vector[147] += 1.0
        else:
            #vector[38] = 1.0
            vector[126] += 1.0
            vector[148] += 1.0
    elif name == '38':
        if didWin:
            #vector[39] = 1.0
            vector[125] += 1.0
            vector[147] += 1.0
        else:
            #vector[40] = 1.0
            vector[126] += 1.0
            vector[148] += 1.0
    elif name == '59':
        if didWin:
            #vector[41] = 1.0
            # class?
            # vector[123] += 1.0
            vector[137] += 1.0
        else:
            #vector[42] = 1.0
            # class?
            # vector[123] += 1.0
            vector[138] += 1.0
    elif name == '40':
        if didWin:
            #vector[43] = 1.0
            vector[123] += 1.0
            vector[143] += 1.0
        else:
            #vector[44] = 1.0
            vector[124] += 1.0
            vector[144] += 1.0
    elif name == '2':
        if didWin:
            #vector[45] = 1.0
            vector[119] += 1.0
            vector[137] += 1.0
        else:
            #vector[46] = 1.0
            vector[120] += 1.0
            vector[138] += 1.0
    elif name == '43':
        if didWin:
            #vector[47] = 1.0
            vector[119] += 1.0
            vector[137] += 1.0
        else:
            #vector[48] = 1.0
            vector[120] += 1.0
            vector[138] += 1.0
    elif name == '3':
        if didWin:
            #vector[49] = 1.0
            vector[119] += 1.0
            vector[137] += 1.0
        else:
            #vector[50] = 1.0
            vector[120] += 1.0
            vector[138] += 1.0
    elif name == '6':
        if didWin:
            #vector[51] = 1.0
            vector[119] += 1.0
            vector[135] += 1.0
        else:
            #vector[52] = 1.0
            vector[120] += 1.0
            vector[136] += 1.0
    elif name == '44':
        if didWin:
            #vector[53] = 1.0
            vector[119] += 1.0
            vector[135] += 1.0
        else:
            #vector[54] = 1.0
            vector[120] += 1.0
            vector[136] += 1.0
    elif name == '50':
        if didWin:
            #vector[55] = 1.0
            vector[119] += 1.0
            vector[135] += 1.0
        else:
            #vector[56] = 1.0
            vector[120] += 1.0
            vector[136] += 1.0
    elif name == '7':
        if didWin:
            #vector[57] = 1.0
            vector[119] += 1.0
            vector[135] += 1.0
        else:
            #vector[58] = 1.0
            vector[120] += 1.0
            vector[136] += 1.0
    elif name == '8':
        if didWin:
            #vector[59] = 1.0
            vector[119] += 1.0
            vector[135] += 1.0
        else:
            #vector[60] = 1.0
            vector[120] += 1.0
            vector[136] += 1.0
    elif name == '13':
        if didWin:
            #vector[61] = 1.0
            vector[119] += 1.0
            vector[135] += 1.0
        else:
            #vector[62] = 1.0
            vector[120] += 1.0
            vector[136] += 1.0
    elif name == '17':
        if didWin:
            #vector[63] = 1.0
            vector[119] += 1.0
            vector[137] += 1.0
        else:
            #vector[64] = 1.0
            vector[120] += 1.0
            vector[138] += 1.0
    elif name == '20':
        if didWin:
            #vector[65] = 1.0
            vector[119] += 1.0
            vector[135] += 1.0
        else:
            #vector[66] = 1.0
            vector[120] += 1.0
            vector[136] += 1.0
    elif name == '41':
        if didWin:
            #vector[67] = 1.0
            vector[121] += 1.0
            vector[135] += 1.0
        else:
            #vector[68] = 1.0
            vector[122] += 1.0
            vector[136] += 1.0
    elif name == '27':
        if didWin:
            #vector[69] = 1.0
            vector[119] += 1.0
            vector[137] += 1.0
        else:
            #vector[70] = 1.0
            vector[120] += 1.0
            vector[138] += 1.0
    elif name == '28':
        if didWin:
            #vector[71] = 1.0
            vector[119] += 1.0
            vector[135] += 1.0
        else:
            #vector[72] = 1.0
            vector[120] += 1.0
            vector[136] += 1.0
    elif name == '35':
        #if korean == autowin
        if didWin:
            #vector[73] = 1.0
            vector[119] += 1.0
            vector[137] += 1.0
        else:
            #vector[74] = 1.0
            vector[120] += 1.0
            vector[138] += 1.0
    elif name == '57':
        if didWin:
            #vector[75] = 1.0
            vector[121] += 1.0
            vector[135] += 1.0
        else:
            #vector[76] = 1.0
            vector[122] += 1.0
            vector[136] += 1.0
    elif name == '55':
        if didWin:
            #vector[77] = 1.0
            vector[129] += 1.0
            vector[139] += 1.0
        else:
            #vector[78] = 1.0
            vector[130] += 1.0
            vector[140] += 1.0
    elif name == '5':
        if didWin:
            #vector[79] = 1.0
            vector[129] += 1.0
            vector[139] += 1.0
        else:
            #vector[80] = 1.0
            vector[130] += 1.0
            vector[140] += 1.0
    elif name == '16':
        if didWin:
            #vector[81] = 1.0
            vector[127] += 1.0
            vector[139] += 1.0
        else:
            #vector[82] = 1.0
            vector[128] += 1.0
            vector[140] += 1.0
    elif name == '18':
        if didWin:
            #vector[83] = 1.0
            vector[129] += 1.0
            vector[139] += 1.0
        else:
            #vector[84] = 1.0
            vector[130] += 1.0
            vector[140] += 1.0
    elif name == '42':
        if didWin:
            #vector[85] = 1.0
            vector[129] += 1.0
            vector[139] += 1.0
        else:
            #vector[86] = 1.0
            vector[130] += 1.0
            vector[140] += 1.0
    elif name == '19':
        if didWin:
            #vector[87] = 1.0
            vector[129] += 1.0
            vector[139] += 1.0
        else:
            #vector[88] = 1.0
            vector[130] += 1.0
            vector[140] += 1.0
    elif name == '25':
        if didWin:
            #vector[89] = 1.0
            vector[127] += 1.0
            vector[139] += 1.0
        else:
            #vector[90] = 1.0
            vector[128] += 1.0
            vector[140] += 1.0
    elif name == '30':
        if didWin:
            #vector[91] = 1.0
            vector[129] += 1.0
            vector[141] += 1.0
        else:
            #vector[92] = 1.0
            vector[130] += 1.0
            vector[142] += 1.0
    elif name == '36':
        if didWin:
            #vector[93] = 1.0
            vector[129] += 1.0
            vector[139] += 1.0
        else:
            #vector[94] = 1.0
            vector[130] += 1.0
            vector[140] += 1.0
    elif name == '37':
        if didWin:
            #vector[95] = 1.0
            vector[127] += 1.0
            vector[139] += 1.0
        else:
            #vector[96] = 1.0
            vector[128] += 1.0
            vector[140] += 1.0
    elif name == '1':
        if didWin:
            #vector[97] = 1.0
            # class?
            # vector[129] += 1.0
            vector[151] += 1.0
        else:
            #vector[98] = 1.0
            # class?
            # vector[129] += 1.0
            vector[152] += 1.0
    elif name == '4':
        if didWin:
            #vector[99] = 1.0
            vector[133] += 1.0
            vector[149] += 1.0
        else:
            #vector[100] = 1.0
            vector[134] += 1.0
            vector[150] += 1.0
    elif name == '10':
        if didWin:
            #vector[101] = 1.0
            vector[131] += 1.0
            vector[149] += 1.0
        else:
            #vector[102] = 1.0
            vector[132] += 1.0
            vector[150] += 1.0
    elif name == '53':
        if didWin:
            #vector[103] = 1.0
            vector[133] += 1.0
            vector[151] += 1.0
        else:
            #vector[104] = 1.0
            vector[135] += 1.0
            vector[152] += 1.0
    elif name == '21':
        if didWin:
            #vector[105] = 1.0
            vector[131] += 1.0
            vector[151] += 1.0
        else:
            #vector[106] = 1.0
            vector[132] += 1.0
            vector[152] += 1.0
    elif name == '22':
        if didWin:
            #vector[107] = 1.0
            vector[133] += 1.0
            vector[149] += 1.0
        else:
            #vector[108] = 1.0
            vector[134] += 1.0
            vector[150] += 1.0
    elif name == '26':
        if didWin:
            #vector[109] = 1.0
            vector[133] += 1.0
            vector[149] += 1.0
        else:
            #vector[110] = 1.0
            vector[134] += 1.0
            vector[150] += 1.0
    elif name == '29':
        if didWin:
            #vector[111] = 1.0
            vector[133] += 1.0
            vector[149] += 1.0
        else:
            #vector[112] = 1.0
            vector[134] += 1.0
            vector[150] += 1.0
    elif name == '32':
        if didWin:
            #vector[113] = 1.0
            vector[133] += 1.0
            vector[151] += 1.0
        else:
            #vector[114] = 1.0
            vector[134] += 1.0
            vector[152] += 1.0
    elif name == '49':
        if didWin:
            #vector[115] = 1.0
            vector[131] += 1.0
            vector[149] += 1.0
        else:
            #vector[116] = 1.0
            vector[132] += 1.0
            vector[150] += 1.0
    elif name == '39':
        if didWin:
            #vector[117] = 1.0
            vector[133] += 1.0
            vector[149] += 1.0
        else:
            #vector[118] = 1.0
            vector[134] += 1.0
            vector[150] += 1.0
    else:
        print "panicBasket panicBasket panicBasket"
        print name
    pass


replays = dict()
with open('Data/Replays.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for rows in reader:
        replays[rows[0]] = list()
        replays[rows[0]].append(rows)

with open('Data/ReplayCharacters.csv', mode='r') as infile:
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

vectors = dict()
i = 0
for replay in hl:
    vectors[i] = [0.0] * 164
    ID = replay[0][0]
    MarkMap(replay[0][3],vectors[i])
    for player in replay[1:11]:
        FillVector(player, vectors[i], ID)
    i+=1
f1 = open("datasets/hl_data_hero_only.train", "wb")
f2 = open("datasets/hl_data_hero_only.dev", "wb")
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

