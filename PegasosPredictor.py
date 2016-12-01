#Tristan Orton-Urbina tortonu1 for cs475

from cs475_types import Predictor, FeatureVector, Instance


class PegasosPredictor(Predictor):
    def __init__(self, regularization, iterations):
        self._w = FeatureVector()
        self._lambda = regularization
        self._numIter = iterations
        self._time = 1.0
        pass

    def train(self, instances):

        for i in range(0, self._numIter):

            for x in instances:
                if x._label._label == 0:
                    scale = -1.0
                else:
                    scale = 1.0
                guess = dotprod(self._w, x._feature_vector) * scale
                addVector = vectormult(self._w, (1.0 - (1.0/self._time)))
                if guess < 1:
                    vectoradd(addVector, vectormult(
                                            x._feature_vector,
                                            (scale * (1.0/
                                                    (self._lambda * self._time)
                                                    )
                                            )
                                        )
                    )

                self._w = addVector
                self._time += 1.0




        pass

    def predict(self, instance):
        guess = dotprod(self._w, instance._feature_vector)
        if guess >= 0:
            return 1
        else:
            return 0
        pass


def dotprod(vector1, vector2):
    result = 0.0
    for key in vector2.data.iterkeys():
        result += vector1.data.get(key, 0) * vector2.data.get(key, 0)
    return result


def vectormult(vector, factor):
    resultVector = FeatureVector()
    for i in vector.data.iterkeys():
        resultVector.data[i] = (factor * vector.data.get(i))
    return resultVector


def vectoradd(vector1, vector2):
    for i in vector2.data.iterkeys():
        vector1.data[i] = vector2.data[i] + vector1.data.get(i, 0)
    pass