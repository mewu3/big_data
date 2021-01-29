#!/usr/bin/python
import sys
import json
import collections
import math
import numpy as np

input = sys.stdin
newCentroids = []
oldCentroids = []

def combiner():
    clusterDict = collections.defaultdict(int)

    for line in input :
        line = json.loads(line)
        clusterId = line[0]
        dataPoints = line[1]

        try :
            clusterDict[clusterId] = clusterDict[clusterId] + [dataPoints]
        except :
            clusterDict[clusterId] = [] + [dataPoints]

    for key, val in clusterDict.items():
        singleCentroidsVals = []
        for centroidVal in [round(sum(idx)/len(val), 7) for idx in zip(*val)]:
            singleCentroidsVals.append(centroidVal)

        newCentroids.append(singleCentroidsVals)

    return newCentroids

newCentroids = combiner()

def reducer() :
    with open('centroids.txt', 'r') as f:
        for line in f:
            oldCentroids.append([float(data) for data in line.split()])

    if oldCentroids == newCentroids:
        with open('clusterResult.txt', 'w') as f1:
            f1.write(json.dumps(input))
    else :
        with open("centroids.txt", "w") as f2 :
            for idx in range(len(newCentroids)):
                f2.write(" ".join(str(val) for val in newCentroids[idx]))
                f2.write("\n")


reducer()
