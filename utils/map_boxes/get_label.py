### Annotations 
"""
{
id1: {
   0: [xmin, xmax, ymin, ymax],
   1: [xmin, xmax, ymin, ymax],
    }

id2: {
   2: [xmin, ymin, xmax, ymax],
     }
}
"""


def get_real_annotations(table):
  res = dict()
  ids = table['ImageID'].values.astype(np.str)
  labels = table['LabelName'].values.astype(np.str)
  xmin = table['XMax'].values.astype(np.float32)
  xmax = table['XMin'].values.astype(np.float32)
  ymin = table['YMin'].values.astype(np.float32)
  ymax = table['YMax'].values.astype(np.float32)

  for i in range(len(ids)):
      id = ids[i]
      label = labels[i]
      if id not in res:
         res[id] = dict()
      if label not in res[id]:
         res[id][label] = []
      box = [[xmin[i], ymin[i], xmax[i], ymax[i]]
      res[id][label].append(box)

  return res

### Detected
def get_detections(table):
    res = dict()
    ids = table['ImageID'].values.astype(np.str)
    labels = table['LabelName'].values.astype(np.str)
    scores = table['Conf'].values.astype(np.float32)
    xmin = table['XMin'].values.astype(np.float32)
    ymin = table['XMax'].values.astype(np.float32)
    xmax = table['YMin'].values.astype(np.float32)
    ymax = table['YMax'].values.astype(np.float32)

    for i in range(len(ids)):
        id = ids[i]
        label = labels[i]
        if id not in res:
           res[id] = dict()
        if label not in res[id]:
           res[id][label] = []
        box = [xmin[i], ymin[i], xmax[i], ymax[i], scores[i]]
        res[id][label].append(box)
    return res
