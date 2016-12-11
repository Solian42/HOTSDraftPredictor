from bs4 import BeautifulSoup
import requests
import pickle
import numpy as np
import unicodedata
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

def toString(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')

def getHeroStats():
    url = 'http://www.hotslogs.com/Sitewide/ScoreResultStatistics'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    table = soup.find()
    herostats = np.zeros(10)
    i = 0
    for tr in soup.find_all('tr')[2:]:
        tds = tr.find_all('td')
        if len(tds) is 15:
            #01: Hero
            #herostats[i][1] = toString(tds[1].text)
            #02: Games
            #herostats[i][2] = float(toString(tds[2].text))
            #03: Win %
            #herostats[i][3] = float(toString(tds[3].text))
            #05: T/D
            #herostats[i][5] = float(toString(tds[5].text))
            #06: Takedowns
            herostats[i][0] = float(toString(tds[6].text).replace(',',''))
            #07: Kills
            herostats[i][1] = float(toString(tds[7].text).replace(',',''))
            #08: Deaths
            herostats[i][2] = float(toString(tds[8].text).replace(',',''))
            #09: Hero Dmg
            herostats[i][3] = float(toString(tds[9].text).replace(',',''))
            #10: Siege Dmg
            herostats[i][4] = float(toString(tds[10].text).replace(',',''))
            #11: Healing
            herostats[i][5] = float(toString(tds[11].text).replace(',','')) if tds[11].text is not u'' else 0.0
            #12: Self Heal
            herostats[i][6] = float(toString(tds[12].text).replace(',','')) if tds[12].text is not u'' else 0.0
            #13: Dmg Taken
            herostats[i][7] = float(toString(tds[13].text).replace(',','')) if tds[13].text is not u'' else 0.0
            #14: XP
            herostats[i][8] = float(toString(tds[14]).replace(',',''))

            # add merc stats manually
            if tds[1] == "Abathur":
                herostats[i][9] = 0.0
            elif tds[1] == "Alarak":
                herostats[i][9] = 7.2
            elif tds[1] == "Anub'arak":
                herostats[i][9] = 10.1
            elif tds[1] == "Artanis":
                herostats[i][9] = 14.9
            elif tds[1] == "Arthas":
                herostats[i][9] = 18.0
            elif tds[1] == "Auriel":
                herostats[i][9] = 4.5
            elif tds[1] == "Azmodan":
                herostats[i][9] = 5.1
            elif tds[1] == "Brightwing":
                herostats[i][9] = 10.4
            elif tds[1] == "Chen":
                herostats[i][9] = 9.1
            elif tds[1] == "Cho":
                herostats[i][9] = 16.4
            elif tds[1] == "Chromie":
                herostats[i][9] = 0.6
            elif tds[1] == "Dehaka":
                herostats[i][9] = 9.1
            elif tds[1] == "Diablo":
                herostats[i][9] = 13.7
            elif tds[1] == "E.T.C.":
                herostats[i][9] = 9.3
            elif tds[1] == "Falstad":
                herostats[i][9] = 6.5
            elif tds[1] == "Gall":
                herostats[i][9] = 0.0
            elif tds[1] == "Gazlowe":
                herostats[i][9] = 46.2
            elif tds[1] == "Greymane":
                herostats[i][9] = 16.6
            elif tds[1] == "Gul'dan":
                herostats[i][9] = 4.9
            elif tds[1] == "Illidan":
                herostats[i][9] = 34.7
            elif tds[1] == "Jaina":
                herostats[i][9] = 9.3
            elif tds[1] == "Johanna":
                herostats[i][9] = 10.7
            elif tds[1] == "Kael'thas":
                herostats[i][9] = 5.4
            elif tds[1] == "Kerrigan":
                herostats[i][9] = 20.4
            elif tds[1] == "Kharazim":
                herostats[i][9] = 18.1
            elif tds[1] == "Leoric":
                herostats[i][9] = 8.1
            elif tds[1] == "Li Li":
                herostats[i][9] = 4.1
            elif tds[1] == "Li-Ming":
                herostats[i][9] = 4.4
            elif tds[1] == "Lt. Morales":
                herostats[i][9] = 1.9
            elif tds[1] == "Lunara":
                herostats[i][9] = 3.2
            elif tds[1] == "Malfurion":
                herostats[i][9] = 4.8
            elif tds[1] == "Medivh":
                herostats[i][9] = 0.6
            elif tds[1] == "Muradin":
                herostats[i][9] = 8.9
            elif tds[1] == "Murky":
                herostats[i][9] = 43.1
            elif tds[1] == "Nazeebo":
                herostats[i][9] = 11.8
            elif tds[1] == "Nova":
                herostats[i][9] = 7.0
            elif tds[1] == "Raynor":
                herostats[i][9] = 4.2
            elif tds[1] == "Rehgar":
                herostats[i][9] = 10.0
            elif tds[1] == "Rexxar":
                herostats[i][9] = 23.0
            elif tds[1] == "Samuro":
                herostats[i][9] = 36.8
            elif tds[1] == "Sgt. Hammer":
                herostats[i][9] = 1.3
            elif tds[1] == "Sonya":
                herostats[i][9] = 30.7
            elif tds[1] == "Stitches":
                herostats[i][9] = 6.9
            elif tds[1] == "Sylvanas":
                herostats[i][9] = 33.8
            elif tds[1] == "Tassadar":
                herostats[i][9] = 2.6
            elif tds[1] == "The Butcher":
                herostats[i][9] = 17.6
            elif tds[1] == "The Lost Vikings":
                herostats[i][9] = 82.2
            elif tds[1] == "Thrall":
                herostats[i][9] = 15.3
            elif tds[1] == "Tracer":
                herostats[i][9] = 5.6
            elif tds[1] == "Tychus":
                herostats[i][9] = 4.3
            elif tds[1] == "Tyrael":
                herostats[i][9] = 10.3
            elif tds[1] == "Tyrande":
                herostats[i][9] = 1.8
            elif tds[1] == "Uther":
                herostats[i][9] = 6.0
            elif tds[1] == "Valla":
                herostats[i][9] = 5.7
            elif tds[1] == "Varian":
                herostats[i][9] = 20.6
            elif tds[1] == "Xul":
                herostats[i][9] = 10.2
            elif tds[1] == "Zagara":
                herostats[i][9] = 17.3
            elif tds[1] == "Zarya":
                herostats[i][9] = 8.8
            elif tds[1] == "Zeratul":
                herostats[i][9] = 7.0
            else:
                print "Oh shit..."
                print tds[1]
        i+= 1
        herostats = np.vstack([herostats, np.zeros(10)])

    
    herostats = np.delete(herostats, herostats.shape - 1, 0)
    
    return herostats

def normalizeStats(herostats):
    # normalizes all stats to between 0 and 1000
    # keys for output are 0 to 8

    numHeroes = max(herostats.keys()) + 1

    normStats = np.zeros((numHeroes, 10))
    
    minStats = np.zeros(10)
    maxStats = np.zeros(10)

    # set min/max to values of first hero's stats
    for i in range(10):
        minStats[i] = herostats[0][i+6]
        maxStats[i] = herostats[0][i+6]
    
    # find min/max value for each stat
    for i in range(1, numHeroes):
        for j in range(10):
            if herostats[i][j+6] > maxStats[j]:
                maxStats[j] = herostats[i][j+6]
            elif herostats[i][j+6] < minStats[j]:
                minStats[j] = herostats[i][j+6]

    # subtract minValue from each stat to set min for each stat to 0
    for i in range(1, numHeroes):
        for j in range(10):
            normStats[i][j] = herostats[i][j+6] - minStats[j]

    # subtract minValue from maxValue to get range for each stat
    for j in range(10):
        maxValue[j] = maxValue[j] - minValue[j]

    # divide each stat by range and multiply by 1000 to normalize
    for i in range(1, numHeroes):
        for j in range(10):
            normStats[i][j] = 1000 * normStats[i][j]/maxValue[j]

    return normStats

def genSplit(normStats, i, k):
    # splits data for k-fold cross validation
    # indices i mod k are test and all others are train (0 <= i <= k-1)

    if i < 0 or i >= k:
        print "Invalid split value!"
        return

    numHeroes = max(herostats.keys()) + 1
    splitSize = numHeroes/k
    if i < numHeroes%k:
        splitSize += 1
    
    testData = np.zeros((numHeroes-splitSize, 10))
    trainData = np.zeroes((splitSize, 10))
    testKey = 0
    trainKey = 0

    for j in range(numHeroes):
        if j % k == i:
            testData[testKey] = normStats[j]
            testKey += 1
        else:
            trainData[trainKey] = normStats[j]
            trainKey += 1

    return [trainData, testData]

def findOptK(n, kmin, kmax, normStats):
    # tests k values with kmin <= k <= kmax for k means
    # returns k with lowest average (over n folds cross validation) error
    # error is sum euclidean distance from cluster centers

    trainSets = dict()
    testSets = dict()
    minError = 10000000.0
    optK = kmin

    # find train/test splits for n fold cross validation
    for i in range(n):
        [trainData, testData] = genSplit(normStats, i, n)
        trainSets[i] = trainData
        testSets[i] = testData
        

    # test different k values
    for k in range(kmin, kmax + 1):
        currError = 0.0

        # check each possible cross validation split        
        for i in range(n):
            # find clusters
            splitError = 0.0
            kmeans = KMeans(n_clusters = k).fit(trainSets[i])
            testClusters = kmeans.predict(testSets[i])

            # determine error
            numSamples = testSets[i].shape[0]
            for j in range(numSamples):
                splitError += euclidean(testSets[i][j], kmeans.cluster_centers_[testClusters[j]])
            currError += splitError/numSamples

        avgError = currError/n
        if avgError < minError:
            minError = avgError
            optK = k

    return k
        
                
        
