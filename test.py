# def createClusters(max_no_cluster, step):
#     my_dict = {}
#
#     customer_data = pd.read_csv(
#         'C:\\Users\\User\\Downloads\\hierarchical-clustering-with-python-and-scikit-learn-shopping-data.csv')
#
#     data = customer_data.iloc[:, 2:5].values
#
#     print(data)
#
#     plt.figure(figsize=(10, 7))
#     plt.title("Customer Dendograms")
#
#     dend = shc.dendrogram(shc.linkage(data, method='ward'))
#
#     for no_clusters in range(max_no_cluster, 0, -step):
#         cluster = AgglomerativeClustering(n_clusters=no_clusters, affinity='euclidean', linkage='ward')
#         cluster.fit_predict(data)
#
#         print(cluster.labels_)
#
#         plt.figure(figsize=(10, 7))
#         ax = plt.axes(projection='3d')
#         ax.scatter3D(data[:, 0], data[:, 1], data[:, 2], c=cluster.labels_, cmap='rainbow')
#
#         label_list = []
#         for i in cluster.labels_:
#             label_list.append(int(i))
#
#         my_dict[str(no_clusters)] = label_list
#
#     with open("cluster_to_labels.json", "w") as outfile:
#         json.dump(my_dict, outfile)
#
#     plt.show()
#
#     return my_dict


import plotly.graph_objects as go

categories = ['processing cost','mechanical properties','chemical stability',
              'thermal stability', 'device integration']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=[1, 5, 2, 2, 3],
      theta=categories,
      fill='toself',
      name='Product A'
))
fig.add_trace(go.Scatterpolar(
      r=[4, 3, 2.5, 1, 2],
      theta=categories,
      fill='toself',
      name='Product B'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 5]
    )),
  showlegend=False
)

fig.show()