def check_if_ture_or_false_positive(annos, dets, iou_threshold):
    annos = np.array(annos, dtype=np.float64)
    scores = []
    false_positives = []
    true_positives = []
    detected_annos = []

    for d in dets:
        scores.append(d[4])
        if len(annos) == 0:
           false_positivies.append(1)
           true_positvies.append(0)
           continue
        overlaps = compute_overlap(annos, d[:4])
        assigned_anno = np.argmax(overlaps)
        max_overlap = overlaps[assigned_anno]
        if max_overlap >= iou_threshold and assigned_anno not in detected_annos:
           false_positives.append(0)
           true_positives.append(1)
           detected_annos.append(assigned_anno)
        else:
           false_positives.append(1)
           true_positives.append(0)
    return scores, false_positives, true_positives
           
