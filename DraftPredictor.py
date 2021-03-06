import pickle
import copy
from sklearn import neighbors
def main():
    print "Let's try to win this game!"
    map = raw_input("Enter the map you're on: ")
    if map == "":
        print "That's not a map, that's an enter key."
        return
    team1 = raw_input("Enter the heroes on team 1, seperated by commas (just return if you're done): ")
    if team1 == "":
        print "I have no heroes to do things with! pls to help."
        return
    team2 = raw_input("Enter the heroes on team 2, seperated by commas (just return if you're done): ")
    if team2 == "":
        print "I have no heroes to do things with! pls to help."
        return
    knnModel = pickle.load(open("datasets/hl_data_heroless_highmmr.knn.model", "rb"))
    team1Heroes = [x.strip() for x in team1.split(',')]
    team2Heroes = [x.strip() for x in team2.split(',')]

    currVec = [0] * 166
    MarkMap(map, currVec)
    for hero in team1Heroes:
        FillVectorRoleOnly(hero, currVec, 1)
    for hero in team2Heroes:
        FillVectorRoleOnly(hero, currVec, 2)
    vectorArray = createAllVectors(currVec, len(team1Heroes), len(team2Heroes))
    for i in range(len(vectorArray)):
        vectorArray[i] = vectorArray[i][1:]

    probability = knnModel.predict_proba(vectorArray.values())
    maxWin = 0.0
    winner = 0
    i = 0
    for vector in probability:
        if maxWin <= vector[0]:
            maxWin = vector[0]
            winner = i
        i += 1
    if winner is 0:
        print "You could use a Tank"
    elif winner is 1:
        print "You could use a Bruiser"
    elif winner is 2:
        print "You could use a Healer"
    elif winner is 3:
        print "You could use a Support"
    elif winner is 4:
        print "You could use a Ambusher"
    elif winner is 5:
        print "You could use a Burst Damage Hero"
    elif winner is 6:
        print "You could use a Sustained Damage Hero"
    elif winner is 7:
        print "You could use a Siege Hero"
    elif winner is 8:
        print "You could use a Utility Hero"
    print probability

def createAllVectors(startVector, team1Size, team2Size):
    vectors = dict()
    if team1Size is 4 and team2Size is 5:
        for i in range(9):
            vectors[i] = copy.deepcopy(startVector)
            if i is 0:
                vectors[i][135] += 1.0
            elif i is 1:
                vectors[i][127] += 1.0
            elif i is 2:
                vectors[i][139] += 1.0
            elif i is 3:
                vectors[i][141] += 1.0
            elif i is 4:
                vectors[i][143] += 1.0
            elif i is 5:
                vectors[i][145] += 1.0
            elif i is 6:
                vectors[i][147] += 1.0
            elif i is 7:
                vectors[i][149] += 1.0
            elif i is 8:
                vectors[i][151] += 1.0
    return vectors


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
    """


def FillVectorRoleOnly(name, vector, team):
    if team % 2 is 0:
        # Team "1" won
        didWin = True
    else:
        # Team "2" won
        didWin = False
    if name == 'Alarak':
        if didWin:
            #vector[1] = 1.0
            #vector[123] += 1.0
            vector[143] += 1.0
        else:
            #vector[2] = 1.0
            #vector[124] += 1.0
            vector[144] += 1.0
    elif name == 'Chromie':
        if didWin:
            #vector[3] = 1.0
            #vector[125] += 1.0
            vector[145] += 1.0
        else:
            #vector[4] = 1.0
            #vector[126] += 1.0
            vector[146] += 1.0
    elif name == 'Falstad':
        if didWin:
            #vector[5] = 1.0
            #vector[125] += 1.0
            vector[147] += 1.0
        else:
            #vector[6] = 1.0
            #vector[126] += 1.0
            vector[148] += 1.0
    elif name == 'Gall':
        if didWin:
            #vector[7] = 1.0
            #vector[125] += 1.0
            vector[147] += 1.0
        else:
            #vector[8] = 1.0
            #vector[126] += 1.0
            vector[148] += 1.0
    elif name == 'Greymane':
        if didWin:
            #vector[9] = 1.0
            #vector[125] += 1.0
            vector[147] += 1.0
        else:
            #vector[10] = 1.0
            #vector[126] += 1.0
            vector[148] += 1.0
    elif name == 'Gul\'dan':
        if didWin:
            #vector[11] = 1.0
            #vector[125] += 1.0
            vector[147] += 1.0
        else:
            #vector[12] = 1.0
            #vector[125] += 1.0
            vector[148] += 1.0
    elif name == 'Illidan':
        if didWin:
            #vector[13] = 1.0
            #vector[123] += 1.0
            vector[147] += 1.0
        else:
            #vector[14] = 1.0
            #vector[124] += 1.0
            vector[148] += 1.0
    elif name == 'Jaina':
        if didWin:
            #vector[15] = 1.0
            #vector[125] += 1.0
            vector[145] += 1.0
        else:
            #vector[16] = 1.0
            #vector[126] += 1.0
            vector[146] += 1.0
    elif name == 'Kael\'Thas':
        if didWin:
            #vector[17] = 1.0
            #vector[125] += 1.0
            vector[145] += 1.0
        else:
            #vector[18] = 1.0
            #vector[126] += 1.0
            vector[146] += 1.0
    elif name == 'Kerrigan':
        if didWin:
            #vector[19] = 1.0
            #vector[123] += 1.0
            vector[143] += 1.0
        else:
            #vector[20] = 1.0
            #vector[124] += 1.0
            vector[144] += 1.0
    elif name == 'Li-Ming':
        if didWin:
            #vector[21] = 1.0
            #vector[125] += 1.0
            vector[145] += 1.0
        else:
            #vector[22] = 1.0
            #vector[126] += 1.0
            vector[146] += 1.0
    elif name == 'Lunara':
        if didWin:
            #vector[23] = 1.0
            #vector[125] += 1.0
            vector[147] += 1.0
        else:
            #vector[24] = 1.0
            #vector[126] += 1.0
            vector[148] += 1.0
    elif name == 'Nova':
        if didWin:
            #vector[25] = 1.0
            #vector[125] += 1.0
            vector[143] += 1.0
        else:
            #vector[26] = 1.0
            #vector[126] += 1.0
            vector[144] += 1.0
    elif name == 'Raynor':
        if didWin:
            #vector[27] = 1.0
            #vector[125] += 1.0
            vector[147] += 1.0
        else:
            #vector[28] = 1.0
            #vector[126] += 1.0
            vector[148] += 1.0
    elif name == 'Samuro':
        if didWin:
            #vector[29] = 1.0
            #vector[123] += 1.0
            vector[143] += 1.0
        else:
            #vector[30] = 1.0
            #vector[124] += 1.0
            vector[144] += 1.0
    elif name == 'The Butcher':
        if didWin:
            #vector[31] = 1.0
            #vector[123] += 1.0
            vector[143] += 1.0
        else:
            #vector[32] = 1.0
            #vector[124] += 1.0
            vector[144] += 1.0
    elif name == 'Thrall':
        if didWin:
            #vector[33] = 1.0
            #vector[123] += 1.0
            vector[147] += 1.0
        else:
            #vector[34] = 1.0
            #vector[124] += 1.0
            vector[148] += 1.0
    elif name == 'Tracer':
        if didWin:
            #vector[35] = 1.0
            #vector[125] += 1.0
            vector[147] += 1.0
        else:
            #vector[36] = 1.0
            #vector[126] += 1.0
            vector[148] += 1.0
    elif name == 'Tychus':
        if didWin:
            #vector[37] = 1.0
            #vector[125] += 1.0
            vector[147] += 1.0
        else:
            #vector[38] = 1.0
            #vector[126] += 1.0
            vector[148] += 1.0
    elif name == 'Valla':
        if didWin:
            #vector[39] = 1.0
            #vector[125] += 1.0
            vector[147] += 1.0
        else:
            #vector[40] = 1.0
            #vector[126] += 1.0
            vector[148] += 1.0
    elif name == 'Varian':
        if didWin:
            #vector[41] = 1.0
            # class?
            # #vector[123] += 1.0
            vector[137] += 1.0
        else:
            #vector[42] = 1.0
            # class?
            # vector[123] += 1.0
            vector[138] += 1.0
    elif name == 'Zeratul':
        if didWin:
            #vector[43] = 1.0
            #vector[123] += 1.0
            vector[143] += 1.0
        else:
            #vector[44] = 1.0
            #vector[124] += 1.0
            vector[144] += 1.0
    elif name == 'Anub\'arak':
        if didWin:
            #vector[45] = 1.0
            #vector[119] += 1.0
            vector[137] += 1.0
        else:
            #vector[46] = 1.0
            #vector[120] += 1.0
            vector[138] += 1.0
    elif name == 'Artanis':
        if didWin:
            #vector[47] = 1.0
            #vector[119] += 1.0
            vector[137] += 1.0
        else:
            #vector[48] = 1.0
            #vector[120] += 1.0
            vector[138] += 1.0
    elif name == "Arthas":
        if didWin:
            #vector[49] = 1.0
            #vector[119] += 1.0
            vector[137] += 1.0
        else:
            #vector[50] = 1.0
            #vector[120] += 1.0
            vector[138] += 1.0
    elif name == 'Chen':
        if didWin:
            #vector[51] = 1.0
            #vector[119] += 1.0
            vector[135] += 1.0
        else:
            #vector[52] = 1.0
            #vector[120] += 1.0
            vector[136] += 1.0
    elif name == 'Cho':
        if didWin:
            #vector[53] = 1.0
            #vector[119] += 1.0
            vector[135] += 1.0
        else:
            #vector[54] = 1.0
            #vector[120] += 1.0
            vector[136] += 1.0
    elif name == 'Dehaka':
        if didWin:
            #vector[55] = 1.0
            #vector[119] += 1.0
            vector[135] += 1.0
        else:
            #vector[56] = 1.0
            #vector[120] += 1.0
            vector[136] += 1.0
    elif name == 'Diablo':
        if didWin:
            #vector[57] = 1.0
            #vector[119] += 1.0
            vector[135] += 1.0
        else:
            #vector[58] = 1.0
            #vector[120] += 1.0
            vector[136] += 1.0
    elif name == 'E.T.C.':
        if didWin:
            #vector[59] = 1.0
            #vector[119] += 1.0
            vector[135] += 1.0
        else:
            #vector[60] = 1.0
            #vector[120] += 1.0
            vector[136] += 1.0
    elif name == 'Johanna':
        if didWin:
            #vector[61] = 1.0
            #vector[119] += 1.0
            vector[135] += 1.0
        else:
            #vector[62] = 1.0
            #vector[120] += 1.0
            vector[136] += 1.0
    elif name == 'Leoric':
        if didWin:
            #vector[63] = 1.0
            #vector[119] += 1.0
            vector[137] += 1.0
        else:
            #vector[64] = 1.0
            #vector[120] += 1.0
            vector[138] += 1.0
    elif name == 'Muradin':
        if didWin:
            #vector[65] = 1.0
            #vector[119] += 1.0
            vector[135] += 1.0
        else:
            #vector[66] = 1.0
            #vector[120] += 1.0
            vector[136] += 1.0
    elif name == 'Rexxar':
        if didWin:
            #vector[67] = 1.0
            #vector[121] += 1.0
            vector[135] += 1.0
        else:
            #vector[68] = 1.0
            #vector[122] += 1.0
            vector[136] += 1.0
    elif name == 'Sonya':
        if didWin:
            #vector[69] = 1.0
            #vector[119] += 1.0
            vector[137] += 1.0
        else:
            #vector[70] = 1.0
            #vector[120] += 1.0
            vector[138] += 1.0
    elif name == 'Stitches':
        if didWin:
            #vector[71] = 1.0
            #vector[119] += 1.0
            vector[135] += 1.0
        else:
            #vector[72] = 1.0
            #vector[120] += 1.0
            vector[136] += 1.0
    elif name == 'Tyrael':
        #if korean == autowin
        if didWin:
            #vector[73] = 1.0
            #vector[119] += 1.0
            vector[137] += 1.0
        else:
            #vector[74] = 1.0
            #vector[120] += 1.0
            vector[138] += 1.0
    elif name == 'Zarya':
        if didWin:
            #vector[75] = 1.0
            #vector[121] += 1.0
            vector[135] += 1.0
        else:
            #vector[76] = 1.0
            #vector[122] += 1.0
            vector[136] += 1.0
    elif name == 'Auriel':
        if didWin:
            #vector[77] = 1.0
            #vector[129] += 1.0
            vector[139] += 1.0
        else:
            #vector[78] = 1.0
            #vector[130] += 1.0
            vector[140] += 1.0
    elif name == 'Brightwing':
        if didWin:
            #vector[79] = 1.0
            #vector[129] += 1.0
            vector[139] += 1.0
        else:
            #vector[80] = 1.0
            #vector[130] += 1.0
            vector[140] += 1.0
    elif name == 'Kharazim':
        if didWin:
            #vector[81] = 1.0
            #vector[127] += 1.0
            vector[139] += 1.0
        else:
            #vector[82] = 1.0
            #vector[128] += 1.0
            vector[140] += 1.0
    elif name == 'Li Li':
        if didWin:
            #vector[83] = 1.0
            #vector[129] += 1.0
            vector[139] += 1.0
        else:
            #vector[84] = 1.0
            #vector[130] += 1.0
            vector[140] += 1.0
    elif name == 'Lt. Morales':
        if didWin:
            #vector[85] = 1.0
            #vector[129] += 1.0
            vector[139] += 1.0
        else:
            #vector[86] = 1.0
            #vector[130] += 1.0
            vector[140] += 1.0
    elif name == 'Malfurion':
        if didWin:
            #vector[87] = 1.0
            #vector[129] += 1.0
            vector[139] += 1.0
        else:
            #vector[88] = 1.0
            #vector[130] += 1.0
            vector[140] += 1.0
    elif name == 'Rehgar':
        if didWin:
            #vector[89] = 1.0
            #vector[127] += 1.0
            vector[139] += 1.0
        else:
            #vector[90] = 1.0
            #vector[128] += 1.0
            vector[140] += 1.0
    elif name == 'Tassadar':
        if didWin:
            #vector[91] = 1.0
            #vector[129] += 1.0
            vector[141] += 1.0
        else:
            #vector[92] = 1.0
            #vector[130] += 1.0
            vector[142] += 1.0
    elif name == 'Tyrande':
        if didWin:
            #vector[93] = 1.0
            #vector[129] += 1.0
            vector[139] += 1.0
        else:
            #vector[94] = 1.0
            #vector[130] += 1.0
            vector[140] += 1.0
    elif name == 'Uther':
        if didWin:
            #vector[95] = 1.0
            #vector[127] += 1.0
            vector[139] += 1.0
        else:
            #vector[96] = 1.0
            #vector[128] += 1.0
            vector[140] += 1.0
    elif name == 'Abathur':
        if didWin:
            #vector[97] = 1.0
            # class?
            # #vector[129] += 1.0
            vector[151] += 1.0
        else:
            #vector[98] = 1.0
            # class?
            # #vector[129] += 1.0
            vector[152] += 1.0
    elif name == 'Azmodan':
        if didWin:
            #vector[99] = 1.0
            #vector[133] += 1.0
            vector[149] += 1.0
        else:
            ##vector[100] = 1.0
            #vector[134] += 1.0
            vector[150] += 1.0
    elif name == 'Gazlowe':
        if didWin:
            #vector[101] = 1.0
            #vector[131] += 1.0
            vector[149] += 1.0
        else:
            ##vector[102] = 1.0
            #vector[132] += 1.0
            vector[150] += 1.0
    elif name == 'Medivh':
        if didWin:
            #vector[103] = 1.0
            #vector[133] += 1.0
            vector[151] += 1.0
        else:
            ##vector[104] = 1.0
            #vector[135] += 1.0
            vector[152] += 1.0
    elif name == 'Murky':
        if didWin:
            #vector[105] = 1.0
            #vector[131] += 1.0
            vector[151] += 1.0
        else:
            #vector[106] = 1.0
            #vector[132] += 1.0
            vector[152] += 1.0
    elif name == 'Nazeebo':
        if didWin:
            #vector[107] = 1.0
            #vector[133] += 1.0
            vector[149] += 1.0
        else:
            #vector[108] = 1.0
            #vector[134] += 1.0
            vector[150] += 1.0
    elif name == 'Sgt. Hammer':
        if didWin:
            #vector[109] = 1.0
            #vector[133] += 1.0
            vector[149] += 1.0
        else:
            #vector[110] = 1.0
            #vector[134] += 1.0
            vector[150] += 1.0
    elif name == 'Sylvanas':
        if didWin:
            #vector[111] = 1.0
            #vector[133] += 1.0
            vector[149] += 1.0
        else:
            ##vector[112] = 1.0
            #vector[134] += 1.0
            vector[150] += 1.0
    elif name == 'The Lost Vikings':
        if didWin:
            #vector[113] = 1.0
            #vector[133] += 1.0
            vector[151] += 1.0
        else:
            #vector[114] = 1.0
            #vector[134] += 1.0
            vector[152] += 1.0
    elif name == 'Xul':
        if didWin:
            #vector[115] = 1.0
            #vector[131] += 1.0
            vector[149] += 1.0
        else:
            #vector[116] = 1.0
            #vector[132] += 1.0
            vector[150] += 1.0
    elif name == 'Zagara':
        if didWin:
            #vector[117] = 1.0
            #vector[133] += 1.0
            vector[149] += 1.0
        else:
            #vector[118] = 1.0
            #vector[134] += 1.0
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







if __name__ == "__main__":
    main()