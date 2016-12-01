from cs475_types import Predictor, Instance, FeatureVector
import math
class KNNPredictor(Predictor):


    def __init__(self, knn):
        self._knn = knn
        self._data = None
        pass

    def train(self, instances):
        self._data = instances
        pass

    def predict(self, instance):
        maxD = 0.0
        foundNeighbors = dict()
        for i in self._data:
            if len(foundNeighbors) < self._knn:
                foundNeighbors[len(foundNeighbors)] = i
                continue
            if maxD == 0.0 and len(foundNeighbors) == self._knn:
                curr = 0.0
                for p in range(0, len(foundNeighbors)):
                    curr = getDistance(instance, foundNeighbors[p])
                    if curr > maxD:
                        maxD = curr

            if maxD > getDistance(instance, i):
                nMax = 0

                for j in range(1, len(foundNeighbors)):
                    if getDistance(instance, foundNeighbors[nMax]) < getDistance(instance, foundNeighbors[j]):
                        nMax = j
                foundNeighbors[nMax] = i
                curr = 0.0
                maxD = 0.0
                for p in range(0, len(foundNeighbors)):
                    curr = getDistance(instance, foundNeighbors[p])
                    if curr > maxD:
                        maxD = curr
        labelVotes = dict()
        for i in foundNeighbors.itervalues():
            if i._label._label not in labelVotes:
                labelVotes[i._label._label] = 1
            else:
                labelVotes[i._label._label] += 1
        mostVotes = 0
        numVotes = 0
        for i in labelVotes.iterkeys():
            if labelVotes[i] > numVotes:
                numVotes = labelVotes[i]
                mostVotes = i

        return mostVotes


class DistanceKNNPredictor(Predictor):
    def __init__(self, knn):
        self._knn = knn
        self._data = None
        pass

    def train(self, instances):
        self._data = instances
        pass

    def predict(self, instance):
        maxD = 0.0
        foundNeighbors = dict()
        for i in self._data:
            if len(foundNeighbors) < self._knn:
                foundNeighbors[len(foundNeighbors)] = i
                continue
            if maxD == 0.0 and len(foundNeighbors) == self._knn:
                curr = 0.0
                for p in range (0, len(foundNeighbors)):
                    curr = getDistance(instance, foundNeighbors[p])
                    if curr > maxD:
                        maxD = curr
            if maxD > getDistance(instance, i):
                nMax = 0
                for j in range(1, len(foundNeighbors)):
                    if getDistance(instance, foundNeighbors[nMax]) < getDistance(instance, foundNeighbors[j]):
                        nMax = j
                foundNeighbors[nMax] = i
                curr = 0.0
                maxD = 0.0
                for p in range(0, len(foundNeighbors)):
                    curr = getDistance(instance, foundNeighbors[p])
                    if curr > maxD:
                        maxD = curr
        labelVotes = dict()
        for i in foundNeighbors.itervalues():
            if i._label._label not in labelVotes:
                labelVotes[i._label._label] = 1.0
            else:
                labelVotes[i._label._label] += 1.0/(1.0 + math.pow(getDistance(instance, i),2))
        mostVotes = 0
        numVotes = 0
        for i in labelVotes.iterkeys():
            if labelVotes[i] >= numVotes:
                numVotes = labelVotes[i]
                mostVotes = i

        return mostVotes



def getDistance(vectorOne, vectorTwo):
    esum = 0.0
    for i in vectorOne._feature_vector.data.iterkeys():
        esum += math.pow(vectorOne._feature_vector.data.get(i, 0) - vectorTwo._feature_vector.data.get(i, 0), 2)
    esum = math.sqrt(esum)

    return esum