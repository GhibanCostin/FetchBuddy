from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import json
# %matplotlib inline
import numpy as np


def createDictFromCSV(file):
    my_dict = {}

    data = pd.read_csv(file)

    for i in range(len(data.values)):
        my_dict[data.values[i][0]] = data.values[i][1]

    return my_dict


def processData(data):
    hobbies_to_index = createDictFromCSV('hobbies.csv')
    department_to_index = createDictFromCSV('department.csv')

    for i in range(len(data)):
        # data[i][0] = data[i][0]
        # data[i][2] = data[i][2]
        data[i][0] = 2 * int(department_to_index.get(data[i][0]))
        data[i][2] = int(hobbies_to_index.get(data[i][2]))

    return data


def createClusters(max_no_cluster, step):
    my_dict = {}

    employee_data = pd.read_csv('EmployeeData.csv')

    data = employee_data.iloc[:, 2:5].values

    data = np.array(processData(data))

    plt.figure(figsize=(10, 7))
    plt.title("Employee Dendograms")

    dend = shc.dendrogram(shc.linkage(data, method='ward'))

    for no_clusters in range(max_no_cluster, 0, -step):
        cluster = AgglomerativeClustering(n_clusters=no_clusters, affinity='euclidean', linkage='ward')
        cluster.fit_predict(data)

        plt.figure()
        ax = plt.axes(projection='3d')
        ax.scatter3D(list(data[:, 0]), list(data[:, 1]), list(data[:, 2]), c=cluster.labels_, cmap='rainbow')

        label_list = []
        for i in cluster.labels_:
            label_list.append(int(i))

        my_dict[str(no_clusters)] = label_list

    with open("cluster_to_labels.json", "w") as outfile:
        json.dump(my_dict, outfile)

    plt.show()

    return my_dict


def createClusters2(max_no_cluster, step):
    my_dict = {}

    customer_data = pd.read_csv(
        'C:\\Users\\User\\Downloads\\hierarchical-clustering-with-python-and-scikit-learn-shopping-data.csv')

    data = customer_data.iloc[:, 2:5].values

    print(data)

    plt.figure(figsize=(10, 7))
    plt.title("Employee Dendograms")

    dend = shc.dendrogram(shc.linkage(data, method='ward'))

    for no_clusters in range(max_no_cluster, 0, -step):
        cluster = AgglomerativeClustering(n_clusters=no_clusters, affinity='euclidean', linkage='ward')
        cluster.fit_predict(data)

        print(cluster.labels_)

        plt.figure(figsize=(10, 7))
        ax = plt.axes(projection='3d')
        ax.scatter3D(data[:, 0], data[:, 1], data[:, 2], c=cluster.labels_, cmap='rainbow')

        label_list = []
        for i in cluster.labels_:
            label_list.append(int(i))

        my_dict[str(no_clusters)] = label_list

    with open("cluster_to_labels.json", "w") as outfile:
        json.dump(my_dict, outfile)

    plt.show()

    return my_dict

def solution():
    cluster_to_labels = createClusters(10, 2)


solution()

