from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression

def load_data(filename):
    instances = []
    labels = []
    with open(filename) as reader:
        for line in reader:
            if len(line.strip()) == 0:
                continue

            # Divide the line into features and label.
            split_line = line.split(" ")
            label_string = split_line[0]

            int_label = -1
            try:
                int_label = int(label_string)
            except ValueError:
                raise ValueError("Unable to convert " + label_string + " to integer in ")

            labels.append(int_label)
            feature_vector = []

            for item in split_line[1:]:
                try:
                    index = int(item.split(":")[0])
                except ValueError:
                    raise ValueError("Unable to convert index " + item.split(":")[0] + " to integer.")
                try:
                    value = float(item.split(":")[1])
                except ValueError:
                    raise ValueError("Unable to convert value " + item.split(":")[1] + " to float.")

                feature_vector.insert(index, value)

            instances.append(feature_vector)

    return instances, labels

instances, labels = load_data("datasets/masters_data.train")

NNclassifier = MLPClassifier(solver='adam', alpha=1e-5,
                           hidden_layer_sizes=(75), random_state=1,
                           max_iter=10000)
LRclassifier = LogisticRegression(solver='liblinear', max_iter=1000)

LRclassifier.fit(instances, labels)
NNclassifier.fit(instances, labels)

pInstances, pLabels = load_data("datasets/masters_data.dev")

NNresults = NNclassifier.predict(pInstances)
LRresults = LRclassifier.predict(pInstances)
LRcorrect = 0.0
NNcorrect = 0.0
for i in range(0, len(pLabels)):
    if NNresults[i] == pLabels[i]:
        NNcorrect += 1.0
    if LRresults[i] == pLabels[i]:
        LRcorrect += 1.0
NNresult = "Accuracy: " + str(NNcorrect/i) + " (" + str(int(NNcorrect)) + "/" + str(i) + ")"
LRresult = "Accuracy: " + str(LRcorrect/i) + " (" + str(int(LRcorrect)) + "/" + str(i) + ")"
print NNresult
print LRresult
