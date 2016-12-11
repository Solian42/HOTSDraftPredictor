import pickle
from sklearn import neighbors
def main():
    print "Let's try to win this game!"
    team1 = input("Enter the heroes on team 1, seperated by spaces (just return if you're done): ")
    if team1 == "":
        print "I have no heroes to do things with! pls to help."
        return
    team2 = input("Enter the heroes on team 1, seperated by spaces (just return if you're done): ")
    if team2 == "":
        print "I have no heroes to do things with! pls to help."
        return
    knnModel = pickle.load(open("datasets/hl_data_heroless_highmmr.knn.model", "rb"))











if __name__ == "__main__":
    main()