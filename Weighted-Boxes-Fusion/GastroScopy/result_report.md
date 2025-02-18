### Model Metric 

|  Model |   mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|-------------|----------|--------------|--------------|--------------|--------|--------------|--------------|----------------|
|  Yolo    |    0.684 | 0.558 | 0.734 | 0.762 | 0.391 | 0.225 | 0.440 | 0.506     |
|  Detectron2    |    0.671 | 0.532 | 0.695 | 0.786 | 0.373 | 0.195 | 0.422 | 0.502   |
|  EfficientDet    |    0.624 | 0.528 | 0.535 | 0.809 | 0.279 | 0.180 | 0.223 | 0.433     |

### Techinques to Combine Boxes 


1. Non-maximum Supression(NMS)

2. Linear Soft-NMS

3. Guassian Soft-NMS

4. Non-maximum weighted(NMW)

5. Weighted boxes fusion(WBF) 
