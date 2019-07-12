import csv
import random
import math
import operator
from sklearn.metrics import confusion_matrix
import pandas as pd


# Split the data into training and test data
def loadData(filename, split, trainingSet=[] , testSet=[]):
    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])
                
def distance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((float(instance1[x]) - float(instance2[x])), 2)
    return math.sqrt(distance)
    
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = distance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key = operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors
    
def getResponse(neighbors):
    # Creating a list with all the possible neighbors
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]
    
def findAcc(testSet, predictions,length):
    correct = 0
    #for x in range(len(testSet)):
    for x in range(length):
        if testSet[x][-1] == predictions[x]:
        	correct += 1
    
    #return (correct/float(len(testSet))) * 100.0
    return (correct/float(length)) * 100.0
                
def main():
    trainingSet=[]
    testSet=[]
    split = 0.67
    loadData('myfile.csv', split, trainingSet, testSet)
    print 'Train set: ' + repr(len(trainingSet))
    print 'Test set: ' + repr(len(testSet))    
    predictions=[]
    k = 3
    y_actu = []
    y_pred = []
    labels = []
    length=15
    #for x in range(len(testSet)):
    for x in range(length):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
        y_actu.append(repr(testSet[x][-1]))
        y_pred.append(repr(result))
        
    accuracy = findAcc(testSet, predictions,length)
    print 'Accuracy: ', accuracy
    y_actu = pd.Series(y_actu, name='Actual')
    y_pred = pd.Series(y_pred, name='Predicted')
    df_confusion = pd.crosstab(y_actu, y_pred)
    print df_confusion
    # cm = confusion_matrix(y_actu, y_pred)
    
    # tp=[0 for i in range(13)]
    # for i in range(13):
    #     tp[i]+=cm[i][i]

    # fp=[0 for i in range(13)]
    # for i in range(13):
    #     for j in range(13):
    #         if i!=j:
    #             fp[j]+=cm[i][j]

    # tn=[0 for i in range(13)]
    # for i in range(13):
    #     for j in range(13):
    #         if i!=j:
    #             fp[i]+=cm[i][j]

    # fn=[0 for i in range(13)]
    # for k in range(13):
    #     for i in range(13):
    #         for j in range(13):
    #             if i!=k and j!=k:
    #                 fp[k]+=cm[i][j]

    # tpr=0.0
    # fpr=0.0

    # for i in range(13):
    #     if fn[i]+tp[i]>0:
    #         tpr+=1.0*tp[i]/((fn[i]+tp[i])*13)
    #     if fp[i]+tn[i]>0:
    #         fpr+=1.0*fp[i]/((fp[i]+tn[i])*13)

    # print "True positive rate : "+str(tpr)
    # print "False positive rate : "+str(fpr)
    # print ""


    


main()
