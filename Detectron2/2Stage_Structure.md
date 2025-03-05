# 1. 2Satge Model with CNN Backbone

**`One Stage Model`**: 

One-stage 모델은 Backbone에서 추출된 feature map을 Feature Pyramid Network(FPN)을 통해 한 번만 처리한 후, 바로 객체의 bounding box와 class를 예측하는 방식, 간결한 구조 덕분에 빠른 연산이 가능하며, 실시간 감지 및 경량화된 모델을 필요로 하는 응용 분야에서 강점을 보인다. 대표적인 예로 **YOLO**, **EfficientDet**, **RetinaNet**이 있다.

**`Two Stage Model`**: 

Two-stage 모델은 Backbone에서 추출된 feature map을 Region Propsal Network(RPN)을 통해 추천 영역(Proposal Box)을 먼저 생성한 후, ROI Network에서 ROI Pooling을 수행하여 더욱 정교한 객체 분류와 박스 회귀를 수행하는 방식이다. 두단계에 걸쳐 정제된 예측을 수행하기 때문에 높은 정확도와 강력한 성능을 자랑하며, 대표적인 모델로 `Faster R-CNN`이 있다.

## Architecture of Base-RCNN-FPN

![image](https://github.com/user-attachments/assets/4f88c573-bae2-45ce-a7ca-0c94fb0800b3)

## FPN(Feature Pyramid Network)

![image](https://github.com/user-attachments/assets/e73e1e94-f325-4adc-bf54-7fdaea3d1036)

## RPN: Region Propsal Network

=> RPN Input is the output feature map from FPN network

=> P2부터 P6의 Feature Map을 이용하며 상황에 따라 Feature Map의 Level를 선택할 수 있다.

=> P2, P3의 경우 작은 물체를 발견할 수 있고 P4~P6의 경우 더 큰 물체를 발견할 수 있다. 이처럼 multiscale는 single scale과 달리 다양한 크기의 물체를 발견할 수 있다.

=> Ground Truth의 경우, gt_boxes, gt_classes가 주어지고 이때 RPN에선 gt_boxes만 사용한다.

![image](https://github.com/user-attachments/assets/6b919c69-2b76-47e3-a3ae-a043b605cd9e)

### RPN Part1. RPN Head

=> `The neural network part of RPN is simple.` 

=> `It is called RPN Head and consists of three convolution layers defined in the StandardRPNHead class`

1) conv(3x3, 256 -> 256ch)
2) objectness logits conv(1x1, 256 -> 3ch)
3) anchor deltas conv(1x1, 256 -> 3x4ch)

### RPN Part2. Anchor Generation

**`Generate Cell Anchors`**

Anchor Ratio의 경우 0.5, 1.0, 2.0로 총 3개가 있으며 이때, 총 5개 레벨에 대해 Cell Anchors가 생성되므로 3x5=15개가 존재한다.

**`Place Anchors on the Grid Points`**

각 Grid Points 마다 Cell Anchors를 위치해 놓으며 이때 Grid Point의 갯수의 경우, 3XWidthxHeight이다. 

### RPN Part3. Ground Truth Preparation

**`Calculate Intersection-over-Unit(Iou) Matrix`**

두개의 Gt_boxes가 있다고 가정할때 P2~P6의 전체 Anchors를 각 gt_boxes 별로
Generated Anchors와의 Iou를 계산한다. 

**`Examine the IoU matrix by Matcher`**

위에서 전체 Generate Anchors에 대해 구한 Iou를 바탕으로 0.7보다 크면 Foreground(1), 0.3보다 작으면 Background(0), 그렇지 않으면 Ignored(-1)

=> 이는 Objectness_logits랑 관련되어 있다. 

**`Calculate anchor deltas`**

Foreground anchor box는 GT boxes랑 비슷하지만 GT boxes의 정확한 모양과 위치를 학습하기 위해서 GT boxes와의 거리 차이는 deltas를 가지고 학습시킨다. 이를 gt_anchor_deltas라고 한다.

=> 이는 Anchor_deltas랑 관련되어 있다.

### RPN Part4. Loss Calculation

**`Objectness Loss`**

Foreground(1)과 Background(0)에 해당하는 Grid Points 부분에 대해서만 loss를 측정한다. 

**`Localiztion Loss`**

Foregounrd(1)에 해당하는 Grid Points 부분에 대해서만 loss를 측정한다. 

=> 이후 최종적으로 총 1_000개의 Proposal boxes를 얻는다.

## ROI: Region Of Interest
___

**=>** `Proposal boxes are only used to crop the feature map and deal with the ROIs`

**=>** `이때, Proposal Box를 크기에 따라 P2~P5(P6 x)에 해당하여 ROI Pooling을 진행한다.`

**=>** `ROI Feature map의 classification의 경우 background도 포함해서 학습시킨다.`

**=>** `ROI Feature map의 Box Localizationd의 경우 예측 class의 bbox만 선택해 학습시킨다.`

![image](https://github.com/user-attachments/assets/ea0b1b55-c72f-400b-8338-fa0c15cfffe0)


# 2. Multiscale Vision Transformers

![image](https://github.com/user-attachments/assets/515f5f90-b4ea-4947-b072-032b25a87327)

**Multiscale Vision Transformers** learn a hierarchy from dense(in space) and simple(in channels) to coarse and complex features. Several resolution-channel scale stages progressively increase the channel capacity of the intermediate latent sequence while reducing its length and thereby spatial resolution

![image](https://github.com/user-attachments/assets/0327721d-4c1f-4a47-99b0-f69c0d4de707)

**Accuracy/complexity trade-off** on Kinetics-400 for
varying # of inference clips per video shown in MViT curves.
Concurrent vision-transformer based methods [78,6,1] require over
5× more computation and large-scale external pre-training on
ImageNet-21K (IN-21K), to achieve equivalent MViT accuracy.

![image](https://github.com/user-attachments/assets/676a9d77-5ca6-43c5-b16a-1766d41e2471)

**Pooling Attention** is a flexible attention mechanism that
(i) allows obtaining the reduced space-time resolution (TˆHˆWˆ ) of
the input (T HW) by pooling the query, Q = P(Qˆ; ΘQ), and/or
(ii) computes attention on a reduced length (T˜H˜W˜ ) by pooling the
key, K = P(Kˆ ; ΘK), and value, V = P(Vˆ ; ΘV ), sequences.

