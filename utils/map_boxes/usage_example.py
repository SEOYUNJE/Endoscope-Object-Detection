!pip install -q map-boxes

"""Example with using csv File"""

from map_boxes import mean_average_precision_for_boxes 

annotations_file = 'example/annotations.csv'
detections_file = 'example/detections.csv'
mean_ap, average_precisions = mean_average_precision_for_boxes(annotations_file, detections_file)

"""Example with using np.array"""
"""you can pass directly numpy arrays of shapes (N, 6) and (M, 7). Be careful about order of variables in arrays:

from map_boxes import mean_average_precision_for_boxes
import pandas as pd

ann = pd.read_csv("example/annotation.csv")
det = pd.read_csv("example/detections.csv)
ann = ann[['ImageId', 'LabelName', 'XMin', 'XMax', 'YMin', 'YMax']].values
det = det[['ImageId', 'LabelName', 'Conf', 'XMin', 'XMax', 'YMin', 'YMax']].values
mean_ap, average_precisions = mean_average_precision_for_boxes(ann,det)
