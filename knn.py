
import csv
import random
import math
import operator

def loadDataset(filename, datasetResult):
    with open(filename, 'rb') as tsv:
        row, column = map(int, tsv.readline().split(" "));

        lines = csv.reader(tsv, delimiter=" ")
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(column):
                dataset[x][y] = float(dataset[x][y])
            datasetResult.append(dataset[x])


def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += ((instance1[x] * instance1[x]) + (instance2[x]*instance2[x]))
    //return math.sqrt(distance)
    return distance

def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors
    
    
def getNeighborsv2(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    closest = 9999;
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        if dist <= closest:
            distances.insert(0, (trainingSet[x], dist))
            closest = dist
        else
            distances.append((trainingSet[x], dist))
            
    """distances.sort(key=operator.itemgetter(1))"""
   
    closeset_neighbors = []
    for x in range(k):
        closeset_neighbors.append(distances[x][0])
    return closeset_neighbors    
    

def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.iteritems(), key = operator.itemgetter(1), reverse = True)
    return sortedVotes[0][0]


def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0



def main():

    trainingSet = []
    testSet     = []

    loadDataset('150k/CCtrain', trainingSet)
    loadDataset('150k/CCtest1', testSet)

    print 'Train set: ' + repr(len(trainingSet))
    print 'Test set: ' + repr(len(testSet))

    predictions = []
    k = 3
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print ('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')



main()
