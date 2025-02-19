### Model Metric 

|  Model |   mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|-------------|----------|--------------|--------------|--------------|--------|--------------|--------------|----------------|
|  Yolo    |    0.658 | 0.519 | 0.704 | 0.750 | 0.354 | 0.207 | 0.357 | 0.498     |
|  Detectron2    |    0.671 | 0.532 | 0.695 | 0.786 | 0.373 | 0.195 | 0.422 | 0.502   |
|  EfficientDet    |    0.689 | 0.551 | 0.713 | 0.803 | 0.376 | 0.199 | 0.432 | 0.498     |

### Techinques to Combine Boxes 


1. Non-maximum Supression(NMS)

|  Iou_threshold | Yolo_Weight | Detectron2_Weight | efficientdet_weight |  mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|--------|----------|------------|------------|----------|--------------|--------------|--------------|--------|--------------|--------------|----------------|
|  0.5    |   1.0  |   1.0  |  1.0   | 0.684 | 0.558 | 0.734 | 0.762 | 0.391 | 0.225 | 0.440 | 0.506     |


2. Soft-NMS
   
|  Iou_threshold |  sigma |  thresh   |Yolo_Weight | Detectron2_Weight | efficientdet_weight |  mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|--------|-------|-------|--------|------------|------------|----------|--------------|--------------|--------------|--------|--------------|--------------|----------------|
|  0.5    |   0.5   |  0.001  |  1.0  |   1.0  |  1.0   | 0.684 | 0.558 | 0.734 | 0.762 | 0.391 | 0.225 | 0.440 | 0.506     |

3. Non-maximum weighted(NMW)

|  Iou_threshold |  skip_box_thr  |Yolo_Weight | Detectron2_Weight | efficientdet_weight |  mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|--------|-------|--------|------------|------------|----------|--------------|--------------|--------------|--------|--------------|--------------|----------------|
|  0.5    |   0.005  |  1.0  |   1.0  |  1.0   | 0.684 | 0.558 | 0.734 | 0.762 | 0.391 | 0.225 | 0.440 | 0.506     |

4. Weighted boxes fusion(WBF) 

|  Iou_threshold |  skip_box_thr |  conf_type  |   allows_overflow   |Yolo_Weight | Detectron2_Weight | efficientdet_weight |  mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|--------|-------|-------|--------|-----------|-------|------------|----------|--------------|--------------|--------------|--------|--------------|--------------|----------------|
|  0.5    |   0.005   |  `avg`  |  False   | 1.0  |   1.0  |  1.0   | 0.684 | 0.558 | 0.734 | 0.762 | 0.391 | 0.225 | 0.440 | 0.506     |
