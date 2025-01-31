### Basics

#### Precision and Recall
**Precision**: What proportion of the positive identifications (predicted boxes) was actually correct?

`Precision = TP/(TP + FP)`

**Recall**: What proportion of actual positives was identified correctly?

`Recall = TP / (TP + FN)`


![image](https://github.com/user-attachments/assets/875bbdec-ea4d-426d-9720-118cc3f66a3a)

**TP**: `True Positives`. You Predict, and it is correct.

**FP**: `False Positives`. You Predict, but it is wrong

**FN**: `False Negative`. You did not predict. and it is worng. You should have predicted

There are no true negatives(TN) in object detection

#### Intersection over union(IOU)
Iou measures the overlap between 2 boxes. 

IoU = (area of overlap) / (area of union)

**IoU @ 0.5**

IoU at 0.5 means that we consider a predicted box as a true positive (TP) 
if the Iou of this box and on of the GT box is greater than 0.5 

![image](https://github.com/user-attachments/assets/7cb53034-f3e4-45d3-a65e-a9b31bdfa169)

#### How to determine TP, FP, FN

1) Sort the predicted boxes in descendent(by score)
2) Pick the most confident prediction
3) Calculate the IoU between the selected prediction box and **all** of the Gt boxes
4) Select the highest IoU
5) If the Iou is greater than our threshold(0.5), We have a true positive(TP) match. In this case, We
remove the matched boxes from the predicted and the GT list of boxes. 
6) Repeat 2-4
7) After we iterate through in our predicted boxes, what is left in the predited list
8) are the false positives(FP) and What is left the GT list are the false negtaives(FN)

**=> All of thease are per class**

### Average Precision(AP)

| Rank   | Correct(TP) | Precision | Recall|
|--------|-------------|-----------|-------|
|    1   |   True      |    1.0    |  0.2  |
|    2   |   True      |    1.0    |  0.4  |
|    3   |   False      |    0.67    |  0.4  |
|    4   |   False      |    0.5    |  0.4  |
|    5   |   False      |    0.4    |  0.4  |
|    6   |   True      |    0.5    |  0.6  |
|    7   |   True      |    0.57    |  0.8  |
|    8   |   False      |    0.5    |  0.8  |
|    9   |   False     |    0.44    |  0.8  |
|    10  |   True      |    0.5    |  1.0  |

**Note: The Recall Value is always increasing(or stays the same)!!** 

![image](https://github.com/user-attachments/assets/eb58c404-9f67-4c41-910a-523822194812)
