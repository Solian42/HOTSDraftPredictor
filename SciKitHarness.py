from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import neighbors
from sklearn.svm import SVC
import os
import argparse
import sys
import pickle

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

def check_args(args):
    if args.mode.lower() == "train":
        if args.algorithm is None:
            raise Exception("--algorithm should be specified in mode \"train\"")
    else:
        if args.predictions_file is None:
            raise Exception("--prediction_file should be specified in mode \"test\"")
        if not os.path.exists(args.model_file):
            raise Exception("model file specified by --model-file does not exist.")


def get_args():
    parser = argparse.ArgumentParser(description="This is the main test harness for scikit")

    parser.add_argument("--data", type=str, required=True, help="The data to use for training or testing.")
    parser.add_argument("--mode", type=str, required=True, choices=["train", "test"],
                        help="Operating mode: train or test.")
    parser.add_argument("--model-file", type=str, required=True,
                        help="The name of the model file to create/load.")
    parser.add_argument("--predictions-file", type=str, help="The predictions file to create.")
    parser.add_argument("--algorithm", type=str, help="The name of the algorithm for training.")
    parser.add_argument("--knn", type=int, help="The value of K for KNN classification.",
                        default=5)
    parser.add_argument("--svm-kernel", type=str, help="The kernel to use for SVM classification",
                        default='poly')
    args = parser.parse_args()
    check_args(args)

    return args

def train(instances, labels):
    args = get_args()
    algorithm = args.algorithm

    if algorithm == "neural_network":
        NNclassifier = MLPClassifier(solver='adam', alpha=1e-5,
                                     hidden_layer_sizes=(100), random_state=1,
                                     max_iter=10000)
        NNclassifier.fit(instances, labels)
        return NNclassifier
    elif algorithm == "logistic_regression":
        LRclassifier = LogisticRegression(solver='liblinear', max_iter=1000)
        LRclassifier.fit(instances, labels)
        return LRclassifier
    elif algorithm == "knn":
        KNNclassifier = neighbors.KNeighborsClassifier(args.knn)
        KNNclassifier.fit(instances, labels)
        return KNNclassifier
    elif algorithm == "svm":
        SVclassifier = SVC(kernel=args.svm_kernel)
        SVclassifier.fit(instances, labels)
        return SVclassifier
    else:
        return None


def write_predictions(predictor, instances, predictions_file):
    try:
        with open(predictions_file, 'w') as writer:

                results = predictor.predict(instances)
                for label in results:
                    writer.write(str(label))
                    writer.write('\n')
    except IOError:
        raise Exception("Exception while opening/writing file for writing predicted labels: " + predictions_file)

def main():
    args = get_args()

    if args.mode.lower() == "train":
        # Load the training data.
        instances, labels = load_data(args.data)
        # Train the model.
        predictor = train(instances, labels)
        try:
            with open(args.model_file, 'wb') as writer:
                pickle.dump(predictor, writer)
        except IOError:
            raise Exception("Exception while writing to the model file.")
        except pickle.PickleError:
            raise Exception("Exception while dumping pickle.")

    elif args.mode.lower() == "test":
        # Load the test data.
        instances, labels = load_data(args.data)

        predictor = None
        # Load the model.
        try:
            with open(args.model_file, 'rb') as reader:
                predictor = pickle.load(reader)
        except IOError:
            raise Exception("Exception while reading the model file.")
        except pickle.PickleError:
            raise Exception("Exception while loading pickle.")

        write_predictions(predictor, instances, args.predictions_file)
    else:
        raise Exception("Unrecognized mode.")

if __name__ == "__main__":
    main()
