import numpy as np
import os

#create a file with random points between 0 and 10
num_points = 20
dimensions = 2

points = np.random.uniform(0, 10, [num_points, dimensions])

f = open("data.txt", "w") 

for i in range(len(points)):
  f.write("%s %s\n" %(str(points[i][0]), str(points[i][1])))
#remove the last \n at the last line
f.seek(-1, os.SEEK_END)
f.truncate()
f.close()

print("data.txt created!")




#######################################################################
centerList = [[5.1, 3.5], [4.9, 3.0]]

def calculate_distance(point1, point2):
  somme = [(point1[i] - point2[i]) **2 for i in range(0,len(point1))]
  return(sum(somme))


##get instances to calculate on a list of lists
list_points = []


with open("data.txt") as f:
  for i in range(num_points):
    list_points.append(f.readline().strip().split())

def assign_instance_to_class(instance): #instannce = one line of the dataset
  output = []
  key_value = []

  for point in instance:
    coords = [float(i) for i in point.strip().split()]
    key_value.append(coords)
    minDistance = calculate_distance(coords, centerList[0])
  minCenter = centerList[0]

  for i in range(1, len(centerList)):
    dist = calculate_distance(coords, centerList[i])
    if dist < minDistance:
      minCenter = centerList[i]
      minDistance = dist
    output.append(i)
    output = output + key_value
    key_value = [] # re-init to not have previous values during the next iteration 
  return(output)


def map_function(list_points):Emploi
  results = []
  for line in list_points:
    results.append(assign_instance_to_class(line))
  return(results)
    

key_value_list = (map_function(list_points))
