from sklearn.neural_network import MLPClassifier

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

classifier = MLPClassifier(solver='adam', alpha=1e-5,
                           hidden_layer_sizes=(75), random_state=1,
                           max_iter=10000)

classifier.fit(instances, labels)

pInstances, pLabels = load_data("datasets/masters_data.dev")

results = classifier.predict(pInstances)

correct = 0.0
for i in range(0, len(pLabels)):
    if results[i] == pLabels[i]:
        correct += 1.0
result = "Accuracy: " + str(correct/i) + " (" + str(int(correct)) + "/" + str(i) + ")"
print result
