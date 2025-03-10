### Model Metric 

|  Model |   mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|-------------|----------|--------------|--------------|--------------|--------|--------------|--------------|----------------|
|  Yolo    |    0.658 | 0.519 | 0.704 | 0.750 | 0.354 | 0.207 | 0.357 | 0.498     |
|  Detectron2    |    0.671 | 0.532 | 0.695 | 0.786 | 0.373 | 0.195 | 0.422 | 0.502   |
|  EfficientDet    |    0.689 | 0.551 | 0.713 | 0.803 | 0.376 | 0.199 | 0.432 | 0.498     |

### Techinques to Combine Boxes 


📌 Non-maximum Supression(NMS)

- Iou Threhold
- Model Weight

|  Iou_threshold | Yolo_Weight | Detectron2_Weight | efficientdet_weight |  mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|--------|----------|------------|------------|----------|--------------|--------------|--------------|--------|--------------|--------------|----------------|
|  0.4    |   1.0  |   1.0  |  1.0   | 0.709 | 0.568 | 0.751 | 0.810 | 0.379 | 0.199 | 0.445 | 0.493     |
|  0.5    |   1.0  |   1.0  |  1.0   | 0.715 | 0.567 | 0.757 | 0.820 | 0.388 | 0.201 | 0.454 | 0.507     |
|  0.55    |   1.0  |   1.0  |  1.0   | 0.714 | 0.567 | 0.755 | 0.821 | 0.391 | 0.202 | 0.455 | 0.514     |
|  0.6    |   1.0  |   1.0  |  1.0   | 0.710 | 0.563 | 0.748 | 0.820 | 0.403 | 0.213 | 0.465 | 0.529     |
|  0.6    |   0.9  |   0.9  |  1.2   | 0.717 | 0.578 | 0.759 | 0.815 | 0.398 | 0.200 | 0.484 | 0.511     |


📌 Soft-NMS

- Iou Threshold
- Sigma
- Thresh(Important for SoftNMS)
- Model weight
   
|  Iou_threshold |  sigma |  thresh   |Yolo_Weight | Detectron2_Weight | efficientdet_weight |  mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|--------|-------|-------|--------|------------|------------|----------|--------------|--------------|--------------|--------|--------------|--------------|----------------|
|  0.5    |   0.5   |  0.001  |  1.0  |   1.0  |  1.0   | 0.588 | 0.489 | 0.544 | 0.730 | 0.373 | 0.211 | 0.391 | 0.517     |
|  0.5    |   0.5   |  0.001  |  0.9  |   0.9  |  1.2   | 0.662 | 0.535 | 0.676 | 0.774 | 0.415 | 0.221 | 0.480 | 0.542     |
|  0.5    |   0.4   |  0.001  |  0.9  |   0.9  |  1.2   | 0.662 | 0.533 | 0.677 | 0.775 | 0.414 | 0.221 | 0.478 | 0.544     |
|  0.5    |   0.5   |  0.0  |  0.9  |   0.9  |  1.2   | 0.662 | 0.534 | 0.677 | 0.774 | 0.417 | 0.224 | 0.483 | 0.545     |
|  0.5    |   0.5   |  0.005  |  0.9  |   0.9  |  1.2   | 0.661 | 0.533 | 0.674 | 0.774 | 0.413 | 0.219 | 0.479 | 0.541     |


📌 Non-maximum weighted(NMW)

- Iou Threshold
- Skip Box Threshold

|  Iou_threshold |  skip_box_thr  |Yolo_Weight | Detectron2_Weight | efficientdet_weight |  mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|--------|-------|--------|------------|------------|----------|--------------|--------------|--------------|--------|--------------|--------------|----------------|
|  0.4    |   0.005  |  1.0  |   1.0  |  1.0   | 0.700 | 0.538 | 0.760 | 0.803 | 0.388 | 0.219 | 0.456 | 0.491     |
|  0.5    |   0.005  |  1.0  |   1.0  |  1.0   | 0.703 | 0.543 | 0.757 | 0.810 | 0.404 | 0.223 | 0.473 | 0.515     |
|  0.6    |   0.005  |  1.0  |   1.0  |  1.0   | 0.709 | 0.569 | 0.749 | 0.808 | 0.433 | 0.222 | 0.502 | 0.575     |   
|  0.6    |   0.010  |  1.0  |   1.0  |  1.0   | 0.708 | 0.569 | 0.747 | 0.808 | 0.433 | 0.222 | 0.502 | 0.575     |
|  0.6    |   0.001  |  0.9  |   0.9  |  1.2   | 0.728 | 0.600 | 0.760 | 0.824 | 0.424 | 0.227 | 0.492 | 0.552     |
|  0.6    |   0.001  |  0.9  |   1.0  |  1.1   | 0.721 | 0.589 | 0.765 | 0.819 | 0.430 | 0.230 | 0.501 | 0.561     |

📌 Weighted boxes fusion(WBF) 

- Iou Threshold
- Skip Box Threshold
- Conf Type:
   - `avg`: average value
   - `max`: maximum value
   - `box_and_model_avg`: box and model wise hybrid weighted average
   - `absent_model_aware_avg`: weighted average that takes into account the absent model

|  Iou_threshold |  skip_box_thr |  conf_type  |Yolo_Weight | Detectron2_Weight | efficientdet_weight |  mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|--------|-------|-------|--------|--------|------------|----------|--------------|--------------|--------------|--------|--------------|--------------|----------------|
|   0.4    |   0.005   |  `avg`  |  1.0  |   1.0  |  1.0   | 0.680 | 0.488 | 0.754 | 0.798 | 0.355 | 0.174 | 0.418 | 0.475     |
|   0.5    |   0.005   |  `avg`  |  1.0  |   1.0  |  1.0   | 0.691 | 0.512 | 0.761 | 0.801 | 0.392 | 0.218 | 0.447 | 0.512     |
|   0.6    |   0.005   |  `avg`  |  1.0  |   1.0  |  1.0   | 0.726 | 0.604 | 0.762 | 0.813 | 0.445 | 0.268 | 0.491 | 0.577     |
|   0.65    |   0.005   |  `avg`  |  1.0  |   1.0  |  1.0   | 0.734 | 0.616 | 0.763 | 0.823 | 0.443 | 0.260 | 0.485 | 0.584     |
|   0.65    |   0.010   |  `avg`  |  1.0  |   1.0  |  1.0   | 0.735 | 0.616 | 0.763 | 0.826 | 0.443 | 0.257 | 0.485 | 0.586     |
|   0.65    |   0.010   |  `max`  |  1.0  |   1.0  |  1.0   | 0.709 | 0.566 | 0.747 | 0.813 | 0.422 | 0.222 | 0.485 | 0.558     |
|   0.65    |   0.001   |  `box_and_model_avg`  |  1.0  |   1.0  |  1.0   | 0.734 | 0.616 | 0.761 | 0.826 | 0.441 | 0.256 | 0.485 | 0.584     |
|   0.65    |   0.001   |  `absent_model_aware_avg`  |  1.0  |   1.0  |  1.0   | 0.735 | 0.616 | 0.762 | 0.826 | 0.442 | 0.256 | 0.485 | 0.584     |
|   0.65    |   0.010   |  `avg`  |  0.9  |   0.9  |  1.2   | 0.730 | 0.605 | 0.761 | 0.826 | 0.446 | 0.257 | 0.492 | 0.589     |
|   0.65    |   0.010   |  `avg`  |  0.9  |   1.0  |  1.1   | 0.730 | 0.606 | 0.760 | 0.823 | 0.447 | 0.256 | 0.492 | 0.593     |
