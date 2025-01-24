!pip install q map-boxes

from map_boxes import mean_average_precision_for_boxes

df['score'] = [np.random.rand() for _ in range(len(df))]

ann = df[['image_id','class_name','x_min','x_max','y_min','y_max']].values

det = df[['image_id','class_name','score','x_min','x_max','y_min','y_max']].values

mean_ap, average_precisions = mean_average_precision_for_boxes(ann, det, iou_threshold=0.5)
