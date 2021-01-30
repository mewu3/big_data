#!/usr/bin/python
import sys
from random import *
import numpy as np
import json
import collections
import math

### Input options ###
# k_centroids=sys.argb[1]
k = 2
# input_file = sys.argv[2]
inputFile = "/home/hadoop/Documents/mine/cho.txt"

### Global variable ###
centroids = []

### functions ###
def initiateCentroids(k, inputFile):
    centroids = []
    file = open(inputFile)
    length = len(file.readline())
    lines = [x.strip("\n").split()[1:] for x in open(inputFile).readlines()]
    centroids = [choice(lines) for x in range(k)]
    centroids = np.array(centroids, float)

    with open('centroids.txt', 'w') as f:
        for centroid in centroids :
            f.write(' '.join(str(point) for point in centroid))
            f.write("\n")

    return centroids

def calculateDistance(center, data) :
    center = np.array(center)
    data = np.array(data)
    return np.linalg.norm(center - data)

def kemansMapper(k, inputFile):
    centroids = initiateCentroids(k, inputFile)
    datas = open(inputFile)

    for li in datas:
        data = [float(data) for data in (li.split()[1:])]
        minDistance = calculateDistance(centroids[0], data[0])
        for i in range(len(centroids)):
            distance = calculateDistance(centroids[i], data)
            if distance < minDistance :
                minDistance = distance
                cluster = i

        # data = [float(x) for x in data]
        # print("{} {}".format(cluster, " ".join(data)))
        print([cluster, data])

kemansMapper(k, inputFile)

# initiateCentroids(k, inputFile)
