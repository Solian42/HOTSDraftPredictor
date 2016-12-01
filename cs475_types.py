#Tristan Orton-Urbina tortonu1 for cs475
from abc import ABCMeta, abstractmethod

# abstract base class for defining labels
class Label:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __str__(self): pass

       
class ClassificationLabel(Label):
    def __init__(self, label):
        self._label = label
        pass
        
    def __str__(self):

        return str(self._label)

class FeatureVector:
    def __init__(self):
        self.data = dict()
        pass
        
    def add(self, index, value):
        self.data[index] = value
        return value
        
    def get(self, index):
        if self.data[index] is None:
            return 0.0
        else:
            return self.data[index]
        

class Instance:
    def __init__(self, feature_vector, label):
        self._feature_vector = feature_vector
        self._label = label


# abstract base class for defining predictors
class Predictor:
    __metaclass__ = ABCMeta

    @abstractmethod
    def train(self, instances): pass

    @abstractmethod
    def predict(self, instance): pass

