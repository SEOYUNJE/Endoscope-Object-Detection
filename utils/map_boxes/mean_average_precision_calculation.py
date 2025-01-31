def mean_average_precision_for_boxes(ann, pred, iou_threshold=0.5, exclude_not_in_annoations=False, verbose=True):
    """
    ann: numpy array of shape (N,6)
    pred: numpy array of shape (N,7)
    iou_threshold: IoU between boxes which count as 'match'
    exclude_not_in_annotations: exclude image Ids which are not exist in annotations
    return: tuple, where first value in mAP and second values is dict with AP for each class.
    
    """
    valid = pd.DataFrame(ann, columns=['ImageID','LabelName','XMin','XMax', 'YMin','YMax'])
    preds = pd.DataFrame(pred, columns=['ImageID','LabelName','Conf','XMin','XMax','YMin','YMax'])
    ann_unique = valid['ImageID'].unique()
    preds_unique = preds['ImageID'].unique()

    if verbose:
        print('Number of files in annotations: {}'.format(len(ann_unique)))
        print('Number of files in predictions: {}'.format(len(preds_unique)))

    # Exclude files not in annotations!
    if exclude_not_in_annotations:
        preds = preds[preds['ImageID'].isin(ann_unique)]
        preds_unique = preds['ImageID'].unique()
        if verbose:
            print('Number of files in detection after reduction: {}'.format(len(preds_unique)))

    unique_classes = valid['LabelName'].unique().astype(np.str)
    if verbose:
        print('Unique classes: {}'.format(len(unique_classes)))

    all_detections = get_detections(preds)
    all_annotations = get_real_annotations(valid)
    if verbose: 
        print('Detections length: {}'.format(len(all_detections)))
        print('Annotations length: {}'.format(len(all_annotations)))

    average_precisions = {}
    for zz, label in enumerate(sorted(unique_classes)):
        # Negative class
        if str(label) == 'nan':
            continue

        false_positives = []
        true_positives = []
        scores = []
        num_annotations = 0.0

        for i in range(len(ann_unique)):
            detections = []
            annotations = []
            id = ann_unique[i]
            if id in all_detections:
               if label in all_detections[id]:
                  detections = all_detections[id][label]
            if id in all_annotations:
               if label in all_annotations[id]:
                  annotations = all_annotations[id][label]

            if len(detections) == 0 and len(annotations) == 0:
               continue
              
            num_annotations += len(annotations)

            scr, fp, tp = check_if_true_or_false_positive(annotations, detections, iou_threshold)
            scores += scr
            false_positives += fp
            true_positives += tp
      
        if num_annotations == 0:
           average_precisions[label] = 0, 0
           continue

        false_positives = np.array(false_positives)
        true_positives = np.array(true_positives)
        scores = np.array(scores)

        # sort by score
        indiecs = np.argsort(-scores)
        false_positives = false_positives[indices]
        true_positives = true_positives[indices]

        ## compute false positives and true positvies
        false_positives = np.cumsum(false_positives)
        true_positives = np.cumsum(true_positives)
      
        ## compute recall and precision
        recall = true_positives / num_annotations
        precision = true_positives / np.maximum(true_positives + false_positvies, np.finfo(np.float64).eps)

        ## compute average precision
        average_precision = compute_ap(recall, precision)
        average_precisions[label] = average_precision, num_annotations, precision, recall

        if verbose:
            s1 = "{:30s} | {:.6f} | {:7d}".format(label, average_precision, int(num_annotations))
            print(s1)
      
    present_classes = 0
    precision = 0
    for label, (average_precision, num_annotations, _, _) in average_precisions.items():
        if num_annotations > 0:
           present_classes += 1
           precision += average_precision
    mean_ap = precision / present_classes
    if verbose:
        print('mAP: {:.6f}'.format(mean_ap))
    return mean_ap, average_precision

