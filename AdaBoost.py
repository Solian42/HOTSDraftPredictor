from cs475_types import Predictor, Instance, FeatureVector
import math

class AdaBoostPredictor(Predictor):
    def __init__(self, iterations):
        self._alphas = dict()
        self._D = dict()
        self._H = dict()
        self._savedH = dict()
        self._T = iterations
        pass
    def train(self, instances):
        instancesDict = dict(enumerate(instances))
        maxJ = 0
        for i in instancesDict:
            tempMax = 0
            for myMax in instancesDict[i]._feature_vector.data.iterkeys():
                if myMax > tempMax: tempMax = myMax
            if tempMax > maxJ: maxJ = tempMax
            self._D[i] = 1.0 / len(instances)
        for j in range(1, maxJ+1):
            sortedInstances = sorted(instances, key=lambda instance: instance._feature_vector.data.get(j, 0))
            sortedInstancesDict = dict(enumerate(sortedInstances))
            self._H[j] = dict()
            for k in range (1, len(instancesDict)):
                if (sortedInstancesDict[k - 1]._feature_vector.data.get(j, 0)) != (sortedInstancesDict[k]._feature_vector.data.get(j, 0)):
                    cutoff = .5 * ((sortedInstancesDict[k - 1]._feature_vector.data.get(j, 0) +
                                     sortedInstancesDict[k]._feature_vector.data.get(j, 0)))
                    sumG0 = 0
                    sumG1 = 0
                    sumL0 = 0
                    sumL1 = 0
                    upper = 0
                    lower = 0
                    for val in sortedInstancesDict.itervalues():
                        if val._feature_vector.data.get(j, 0) >= cutoff:
                            if val._label._label == 1: sumG1 += 1
                            else: sumG0 += 1
                        else:
                            if val._label._label == 1: sumL1 += 1
                            else: sumL0 += 1
                    if sumG1 > sumG0: upper = 1
                    else: upper = 0
                    if sumL1 > sumL0: lower = 1
                    else: lower = 0
                    if (sumG0 + sumG1 != 0) and (sumL0 + sumL1 != 0):
                        self._H[j][k] = [cutoff, upper, lower, j]
        for t in range(0, self._T):
            error = 1.0
            hj = 0
            hc = 0
            for j in self._H.iterkeys():
                for c in self._H[j].iterkeys():
                    currErr = 0.0
                    for i in instancesDict.iterkeys():
                        if instancesDict[i]._feature_vector.data.get(j, 0) > self._H[j][c][0]:
                            if instancesDict[i]._label._label != self._H[j][c][1]: currErr += self._D[i]
                        else:
                            if instancesDict[i]._label._label != self._H[j][c][2]: currErr += self._D[i]
                    if error >= currErr:
                        hj = j
                        hc = c
                        error = currErr
            if error < 0.000001:
                if t == 0:
                    self._savedH[0] = [self._H[hj][hc][0], self._H[hj][hc][1], self._H[hj][hc][2], self._H[hj][hc][3]]
                    self._alphas[0] = 1
                return
            self._savedH[t] = [self._H[hj][hc][0], self._H[hj][hc][1], self._H[hj][hc][2], self._H[hj][hc][3]]
            insideLog = (1.0 - error)/error
            self._alphas[t] = .5 * math.log(insideLog)
            z = 0.0
            for i in instancesDict.iterkeys():
                predict = 0
                if instancesDict[i]._feature_vector.data.get(hj, 0) > self._savedH[t][0]:
                    if self._savedH[t][1] == 0:
                        predict = -1
                    else: predict = 1
                else:
                    if self._savedH[t][2] == 0:
                        predict = -1
                    else: predict = 1
                if instancesDict[i]._label._label == 0:
                    transformedLabel = -1
                else: transformedLabel = 1
                z += self._D[i] * math.exp(-self._alphas[t] * transformedLabel * predict)
            for i in instancesDict.iterkeys():
                predict = 0
                if instancesDict[i]._feature_vector.data.get(hj, 0) > self._savedH[t][0]:
                    if self._savedH[t][1] == 0:
                        predict = -1
                    else: predict = 1
                else:
                    if self._savedH[t][2] == 0:
                        predict = -1
                    else: predict = 1
                transformedLabel = 0
                if instancesDict[i]._label._label == 0:
                    transformedLabel = -1
                else: transformedLabel = 1
                self._D[i] = (1.0 / z) * self._D[i] * math.exp(-self._alphas[t] * transformedLabel * predict)
        pass

    def predict(self, instance):
        sum0 = 0.0
        sum1 = 0.0
        for t in self._savedH.iterkeys():
            if instance._feature_vector.data.get(self._savedH[t][3], 0) > self._savedH[t][0]:
                if self._savedH[t][1] == 0: sum0 += self._alphas[t]
                else: sum1 += self._alphas[t]
            else:
                if self._savedH[t][2] == 0: sum0 += self._alphas[t]
                else: sum1 += self._alphas[t]
        if sum1 > sum0: return 1
        return 0
