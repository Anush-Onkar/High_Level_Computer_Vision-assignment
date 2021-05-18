# Assignment Submission by
# 
# Name 1: Hitesh Kotte Student id 1:7010571 Email 1:hiko00001@stud.uni-saarland.de
# 
# Name 2:Rahul Mudambi Venkatesh Student id 2:7015710 Email 2:ramu00001@stud.uni-saarland.de
# 
# Name 3: Anush Onkarappa Student id 3:7010620 Email 3:anon00001@stud.uni-saarland.de

# compute chi2 distance between x and y
def dist_chi2(x,y):
  a = x + y
  b = ((x - y)**2)
  x = a != 0 #as we dont want to divide with 0, so we check for index where vector value i not 0
  return sum(b[x]/a[x])

# compute l2 distance between x and y
def dist_l2(x,y):
  #Computing sum of squared distances
  return sum((x-y)**2)
 
# compute intersection distance between x and y
# return 1 - intersection, so that smaller values also correspond to more similar histograms
def dist_intersect(x,y):
  return 1-sum([min(x[i],y[i]) for i in range(x.size)])

def get_dist_by_name(x, y, dist_name):
  if dist_name == 'chi2':
    return dist_chi2(x,y)
  elif dist_name == 'intersect':
    return dist_intersect(x,y)
  elif dist_name == 'l2':
    return dist_l2(x,y)
  else:
    assert 'unknown distance: %s'%dist_name