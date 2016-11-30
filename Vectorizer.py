import pickle

replaydata = pickle.load(open("Data/VectorData.data", "rb"))
vectors = dict()
i = 0
for replay in replaydata.itervalues():
    vectors[i] = list()
    