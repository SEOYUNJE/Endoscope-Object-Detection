# My Journey to Test mAP50: 0.684 / mAP75: 0.391

I studied about YOLOv11, which is a one-stage model for object detection. In this case, the goal was to detect lesions in the given gastroscopy images(cancer, polyp, ulcer). I went through a lot of trial and error to obtaion the best mAP for using Yolov11 model.


#### YOLOv11 is a

`1 stage model` 
  -  predicts bounding boxes and class labels in a single pass through the network.

Introduces `C3k2 block`
  - compact version of the CSP bottleneck structure, reducing trainable parameters and improving architectural efficiency. Also, uses two smaller convolutions instead of a single large convolution

Introduces `C2PSA block`
  - helps the model concentrate on specific areas of interest, improving detection accuracy for objects of various sizes and positions.




### Part-1: Build Pipeline Notebook(Test mAP50: 0.466 / mAP75: 0.229)

First, I trained yolov11 without any adjustments, and only with the yolo default setting. 

### Thanks for Reading My Documents !!!
