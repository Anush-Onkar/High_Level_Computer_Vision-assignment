# Assignment Submission by
# 
# Name 1: Hitesh Kotte Student id 1:7010571 Email 1:hiko00001@stud.uni-saarland.de
# 
# Name 2:Rahul Mudambi Venkatesh Student id 2:7015710 Email 2:ramu00001@stud.uni-saarland.de
# 
# Name 3: Anush Onkarappa Student id 3:7010620 Email 3:anon00001@stud.uni-saarland.de

import numpy as np
import matplotlib.pyplot as plt
import histogram_module
import dist_module
import match_module

# compute and plot the recall/precision curve
# D - square matrix, D(i, j) = distance between model image i, and query image j
# note: assume that query and model images are in the same order, i.e. correct answer for i-th query image is the i-th model image
def plot_rpc(D, plot_color):
    recall = []
    precision = []
    total_imgs = D.shape[1]
    num_images = D.shape[0]
    
    assert(D.shape[0] == D.shape[1])
    
    labels = np.diag([1]*num_images)
    d = D.reshape(D.size)
    l = labels.reshape(labels.size)
    
    sortidx = d.argsort()
    d = d[sortidx]
    l = l[sortidx]
    tp = 0
    
    for idx in range(len(d)):
        tp = tp + l[idx]
        #compute precision and recall values and append them to "recall" and "precision" vectors
        precision.append(tp/(idx+1))
        recall.append(tp/num_images)
    plt.plot([1-precision[i] for i in range(len(precision))], recall, plot_color+'-')

def compare_dist_rpc(model_images, query_images, dist_types, hist_type, num_bins, plot_colors):
  assert len(plot_colors) == len(dist_types)
  for idx in range(len(dist_types)):
    [best_match, D] = match_module.find_best_match(model_images, query_images, dist_types[idx], hist_type, int(num_bins))
    plot_rpc(D, plot_colors[idx])

  plt.axis([0, 1, 0, 1])
  plt.xlabel('1 - precision')
  plt.ylabel('recall')
  #legend(dist_types, 'Location', 'Best')
  plt.legend( dist_types, loc='best')