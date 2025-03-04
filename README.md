![image](https://github.com/user-attachments/assets/781a248d-6091-438a-b3ec-674da69c4bd4)


## 📚 Project Introduction 📚
**📌 Project Name** 
   
=> 딥러닝 기반 위,대장 내시경 영상 내 질환 자동 검출 
    
**📌 Project Goal**
    
=> 1Stage Model부터 2Stage Model까지 다양한 모델 Architecture 공부 및 의료 이미지 도메인에 대한 이해 향상을 목표로 합니다 

**📌 Lesion Detection**

=> AI를 통해 위장, 대장 내 궤양, 용종, 암 검출 가능 


   
## 📋 Table of content
1. [Dataset](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#-dataset)
   
    I. [AI Hub's Original Dataset](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#ai-hubs-original-dataset)
   
    II. [Gastroscopy Dataset](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#gastroscopy-dataset)
   
    III. [Colonoscopy Dataset](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#colonoscopy-dataset)
   
2. [Exploratory Data Analysis](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#-exploratory-data-analysis)
   
    I. [Gastroscopy EDA](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#gastroscopy-eda)
   
    II. [Colonoscopy EDA](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#colonoscopy-eda)

3. [Train](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#-train)

   I. [Yolo](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#yolo)
   
   II. [Detectron2](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#detectron2)

   III. [EfficientDet](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#efficientdet)

4. [Inference](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#-inference)

   I. [Yolo](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#yolo_test)
   
   II. [Detectron2](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#detectron2_test)

   III. [EfficientDet](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#efficientdet_test)


5. [Ensemble with WBF](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#-ensemble-with-wbf)

6. [Calibrated Confidence Score](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#-calibrated-confidence-score)

7. [RGB Superposition](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#-rgb-superposition)

8. [Next Step](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#-next-step)
   
9. [Citing](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#-citing)

10. [Contact](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#-contact)

### ⏳ Dataset

#### AI Hubs' Original Dataset

<details> 
<summary>주소(Download is possible only Korean)</summary>
<br>
=> https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71666
</details>

<details> 
<summary>소개</summary>
<br>
=> 실제 위, 대장 내시경의 궤양, 용종, 암 이미지를 기반으로 위 20,000장(궤양 5,000장, 용종 5,000장, 암 10,000장), 대장 20,000장(궤양 5,000장, 
용종 5,000장, 암 10,000장) 총 40,000장의 내시경 이미지 합성 이미지를 생성
</details>
  
<details> 
<summary>구축목적</summary>
<br>
=> 개인 정보 이슈가 없이 누구나 사용가능한 헬스케어 데이터를 배포하기 위한 목적으로, 실제의 위/대장 내시경을 기반으로 생성AI를 통해 위/대장 내시    경 이미지를 합성함
   
</details>

<details> 
<summary>데이터 구축 규모</summary>
<br>
=> 내시경 이미지 합성데이터 총 4만장 (위 합성데이터 2만장, 대장 합성데이터 2만장)
   
![image](https://github.com/user-attachments/assets/600fa2ad-17be-49dd-842b-2ca6ca81a255)
</details>


#### Gastroscopy Dataset

<details> 
<summary>주소</summary>
<br>
   
=> **Gastroscopy 256X256**: https://www.kaggle.com/datasets/seoyunje/gastroscopy-256x256-resized-png 

=> **Gastroscopy 1024X1024**: https://www.kaggle.com/datasets/seoyunje/gastroscopy-1024x1024-resized-png

=> **Annotation**: https://www.kaggle.com/datasets/msyu78/gastroscopy-meta
</details>


<details> 
<summary>구축목적</summary>
<br>
=> 리소스 자원의 한계로 인해 4만장의 대용량 데이터셋 학습에 무리가 있음. 이에 리소스 자원 내 모델 학습 및 최적화를 위해 소규모 데이터셋을 구축함. 
</details>

<details>
<summary>데이터 구축 규모</summary>
<br>
위 내시경 이미지 합성데이터 2,000장(암 1,000장, 용종 500장, 궤양 497장)

![image](https://github.com/user-attachments/assets/d471a294-1d91-4b48-a8dc-f944c11bb095)
</details>

<details> 
<summary>Data Split</summary>
<br>
   
![image](https://github.com/user-attachments/assets/3714a459-97ff-4c61-9ff1-9357f8447a70)

</details>


#### Colonoscopy Dataset

<details> 
<summary>주소</summary>
<br>
   
=> **Colonoscopy 256X256**: https://www.kaggle.com/datasets/seoyunje/colonoscopy-256x256-resized-png
   
=> **Colonoscopy 1024X1024**: https://www.kaggle.com/datasets/seoyunje/colonoscopy-1024x1024-resized-png

=> **Annotation**: https://www.kaggle.com/datasets/msyu78/metadataset
</details>

<details> 
<summary>구축목적</summary>
<br>
=> 리소스 자원의 한계로 인해 4만장의 대용량 데이터셋 학습에 무리가 있음. 이에 리소스 자원 내 모델 학습 및 최적화를 위해 소규모 데이터셋을 구축함. 
</details>

<details>
<summary>데이터 구축 규모</summary>
<br>
대장 내시경 이미지 합성데이터 2,000장(암 1,000장, 용종 500장, 궤양 496장)
   
![image](https://github.com/user-attachments/assets/1713067a-f845-406d-9bdb-70ee1949d1e6)


</details>

<details> 
<summary>Data Split</summary>
<br>
   
![image](https://github.com/user-attachments/assets/3714a459-97ff-4c61-9ff1-9357f8447a70)

</details>


### 💡 Exploratory Data Analysis

#### Gastroscopy EDA

<details>
<summary>metadata</summary>
<br>
   
| Meta      | Count |
|----------------------|-------|
| Total Image with bbox annotation| 1997   |
| Average of bboxes per image  | 1   |
| The most bboxes in one image | 29   |
| The least bboxes in one image  | 1   |
</details>

<details>
<summary>Location of Bounding Box</summary>
<br>

![image](https://github.com/user-attachments/assets/d2bfa085-347e-4f20-aba9-a87e31f8a07c)
</details>

<details>
<summary>Examples</summary>
<br>

- Ulcer Example
  
![image](https://github.com/user-attachments/assets/d2b4cc6e-ae9f-4b07-88df-42e791a1c3c7)

- Polyp Example
  
![image](https://github.com/user-attachments/assets/b58bff8a-861d-4f67-8d8b-7cc533b939b1)

- Cancer Example
  
![image](https://github.com/user-attachments/assets/4b319992-379d-4f25-b948-a80d2abfab6e)

</details>


#### Colonoscopy EDA

<details>
<summary>metadata</summary>
<br>
   
| Meta      | Count |
|----------------------|-------|
| Total Image with bbox annotation| 1996   |
| Average of bboxes per image  | 1   |
| The most bboxes in one image | 10   |
| The least bboxes in one image  | 1   |
</details>

<details>
<summary>Location of Bounding Box</summary>
<br>

![image](https://github.com/user-attachments/assets/d96d798d-05cc-4bbc-8dfb-ab46703cea1c)

</details>

<details>
<summary>Examples</summary>
<br>

- Ulcer Example
  
![image](https://github.com/user-attachments/assets/24a66ee0-b475-4b8d-9208-83564497529a)


- Polyp Example
  
![image](https://github.com/user-attachments/assets/8dd3e9e8-3f42-47ce-9442-50647a25c503)


- Cancer Example
  
![image](https://github.com/user-attachments/assets/8bc85778-27cd-45c9-837f-2b7b4651e4cf)


</details>

### 📦 Train 

#### YOLO
<details>
<summary> GastroScopy</summary>

### Update
#### Version1
   - Yolov11 Model Pipeline
   - No augmentation

#### Version2
   - Adding `HSV-Hue augmentation` (**hsv_h**)
   - Adding `HSV-Saturation augmentation` (**hsv_s**)
   - Adding `HSV-Value augmentation` (**hsv_v**)
   - Adding `image rotation`(**degrees**)
   - Adding `image translation`(**translate**)
   - Adding `rotation`(**flipup, fliplr**)

#### Version3 
   - Adding `Image Enhancement Transform`(**CLAHE**)
   - Adding `Random brightness, contrast`(**RandomBrightnessContrast**)

#### Version4
   - Adding `Channel Shuffling Transform` (**ChannelShuffle**)
   - Adding `Defocus Blur Transform` (**Defocus**)
   - Adding `Glass Blur Transform` (**GlassBlur**)

#### Version5
   - optimizer = `auto`
   - Delete `Random brightness, contrast`(**RandomBrightnessContrast**)
   - Delete `rotation up and down` (**flipud**)
   - Adding `mosaic`
   - Adding `mixup`

#### Vesion6
   - Inference, set `conf` = 0.001, `iou` = 0.7, `max_det` = 100
      

</details>


<details>
<summary> ColonoScopy</summary>
<br>

</details>


#### Detectron2
<details>
<summary> GastroScopy </summary>
   
### Updates
___
#### Version 1

- Build Detectron2 Model Pipeline
- Backbone: `faster_rcnn_R_50_FPN_1x`

#### Version 2

- Adding `Flip Transform`(**Horizontal Flip**)
- Adding `Image Enhancement Transform`(**CLAHE**)
- Adding `Channel Transform`(**ToGray, ChannelDropout, ChannelShift, RGBShift**)
- Adding `Dropout Transform`(**XYMasking, CoarseDropout, BBoxSafeRandomCrop**)
- Adding `Nosiy Transform`(**RandomGravel, RandomSnow**)

#### Version 3

- Adding `Custom MixUp Transform`(probability=0.1)
- Adding `Custom Mosaic Transform`(probability=0.25)

![image](https://github.com/user-attachments/assets/5846af60-2928-4da2-aef2-464254d0a697)

#### Version 4
- **Batch Size**: `16 -> 8`
- **base_lr_end**: `0 -> 1e-9`
- **weight_decay**: `1e-5 -> 1e-4`
- **warmup_factor**: `1e-3 -> 1e-4`
- **warmup_iters**: `max_iters//40 -> max_iters//20`

#### Version 5
- **RPN.BBOX_REG_LOSS_TYPE**: `smooth_l1` -> `ciou`
- **ROI.BOX_HEAD.BBOX_REG_LOSS_TYPE**: `smooth_l1` -> `ciou`
- **base_lr**: `1e-2 -> 5e-3`
- **weight_decay**: `1e-4 -> 5e-5`
- **Pooler_Resolution**: `14 -> 28`
- **Img_SIZE**: `256 -> 512`

![image](https://github.com/user-attachments/assets/d7ca0995-2e45-4a92-babe-ae012c2519b6)


#### Version 6

**RPN.BATCH_SIZE_PER_IMAGE**: `256 -> 384`

**cfg.MODEL.ANCHOR_GENERATOR.SIZES**: `[[32, 64, 128, 256, 512]] -> [[16, 32, 64, 128, 192, 256, 512]]`

**cfg.MODEL.RPN.IN_FEATURES**: `["p2", "p3", "p4","p5", "p6"] -> ["p2", "p2", "p3", "p4","p4","p5", "p6"]`

**MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE**: `512 -> 256`

**MODEL.ROI_HEADS.POSITIVE_FRACTION**: `0.25 -> 0.5`

![image](https://github.com/user-attachments/assets/6f845a5d-d418-431b-a52e-bde4be3c683e)

![image](https://github.com/user-attachments/assets/c837ca44-6c24-4976-af51-c64294be6b19)


</details>

<details>
<summary> ColonoScopy</summary>
   
### Updates
___
#### version1
   - Build Detectron2 Model Pipeline
   - Backbone: faster_rcnn_R_50_FPN_3x
     
#### version2
- Adding Data augmentation
   - Adding `RandomFlip` with (prob=0.4, horizontal=True, vertical=False)
   - Adding `RandomContrast` with (intensity_min = 0.5, intensity_max=1.5)
   - Adding `RandomBrightness` with (intensity_min=0.5, intensity_max=1.5)
     
#### version3
   - Adding `Custom Mosaic Transform` with probability = 0.2
   - Adding `RandomLighting` with scale=0.1
   - Adding `RandomRotation` with angle=[-10, 10]

#### version4
   - **Backbone** : faster_rcnn_R_50_FPN_1x
   - **scheduler** : WarmupCosineLR
   - Adding `Mosaic` with probability 0.2

#### version5
   - **batch size** : 8
   - **warmup factor** : 5e-4
   - **scheduler** : WarmupMultiStepLR

#### version6
   - **batch size** : 4



</details>

#### EfficientDet
<details>
<summary> GastroScopy</summary>
<br>
   
### Updates
___
#### Version 1

- Build EfficientDet Model Pipeline
- **Backbone**: `tf_efficientnet_b0`
- **Model**: `tf_efficientdet_d0`
- Adding `HorizontalFlip(p=0.5)`

#### Version 2

- **Batch Size**: `4`
- **lr**: `1e03`
- **weight_decay**: `1e-5`
- **Scheduler_Type**: `CosineAnnealingLR`
- **num_epochs**: `20`

#### Version 3

- **fpn_name**: `BiFpn`
- **FPN Node Weight Method**: `Fast Attention`
- **fpn_cell_repeats**: `3`
- **fpn_channels**: `384`
- **fpn_activation**: `swish`

![image](https://github.com/user-attachments/assets/40496268-860f-4bbb-a660-5e1e77cc1517)

#### Version 4
- **label_smoothing**: `0.0 -> 0.15`
- **num_scales**: `3 -> 4`
  
  => [2^0, 2^0.33, 2^0.66] -> [2^0, 2^0.25, 2^0.5, 2^0.75]
- **anchor_scale**: 3
- **anchor_ratio**: [0.5, 1.0, 2.0]
- **Backbone**: `tf_efficientnet_b0` -> `tf_efficientnet_b0.ns_jft_in1k` 

#### Version 5

- **img_size**: `256X256` -> `512X512`
- **Backbone**: `tf_efficientnet_b0` -> `tf_efficientnet_b1`
- **Model**: `tf_efficientnet_d0` -> `tf_efficientdet_d1`
- **num_epochs**: `20 -> 40`
</details>

<details>
<summary> ColonoScopy</summary>
<br>

</details>

### ⛳ Inference

#### YOLO_TEST

GastroScopy 📌 Metric mAP50, 75


|       Version   | name  |  Train  |  Test   |   mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|-------------------|----------|--------|----------|----------|--------------|--------------|--------------|--------|--------------|--------------|----------------|
| V1    | yolo11n   | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Yolo/GastroScopy/Train/baseline_v1.ipynb)             | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Yolo/GastroScopy/Inference/inference_v1.ipynb)     |    0.466 | 0.148 | 0.540 | 0.594 | 0.229 | 0.090 | 0.240 | 0.356     |
| V2    | yolo11n     | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Yolo/GastroScopy/Train/baseline_v2.ipynb)        | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Yolo/GastroScopy/Inference/inference_v2.ipynb)        |    0.574 | 0.420 | 0.631 | 0.671 | 0.324 | 0.209 | 0.348 | 0.397     |
| V3    | yolo11n     | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Yolo/GastroScopy/Train/baseline_v3.ipynb)       | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Yolo/GastroScopy/Inference/inference_v3.ipynb)       |    0.532 | 0.390 | 0.548 | 0.658 | 0.301 | 0.180 | 0.309 | 0.412     |
| V4    | yolo11n     | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Yolo/GastroScopy/Train/baseline_v4.ipynb)        | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Yolo/GastroScopy/Inference/inference_v4.ipynb)       |    0.529 | 0.354 | 0.598 | 0.636 | 0.312 | 0.218 | 0.313 | 0.404     |
| V5    | yolo11n    | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Yolo/GastroScopy/Train/baseline_v5.ipynb)        | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Yolo/GastroScopy/Inference/inference_v5.ipynb)       |    0.610 | 0.459 | 0.660 | 0.712 | 0.353 | 0.178 | 0.413 | 0.468     |
| V6    | yolo11n     | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Yolo/GastroScopy/Train/baseline_v6.ipynb)        | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Yolo/GastroScopy/Inference/inference_v6.ipynb)       |    0.658 | 0.519 | 0.704 | 0.750 | 0.354 | 0.207 | 0.357 | 0.498     |

ColonoScopy 📌 Metric mAP50, 75

|       Version   | name  |  Train  |  Test   |   mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|-------------------|----------|--------|----------|----------|--------------|--------------|--------------|--------|--------------|--------------|----------------|
| V1    | rtdeter-large   | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Yolo/GastroScopy/Train/baseline_v1.ipynb)             | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Yolo/GastroScopy/Inference/inference_v1.ipynb)     |    0.466 | 0.148 | 0.540 | 0.594 | 0.229 | 0.090 | 0.240 | 0.356     |


#### Detectron2_TEST
GastroScopy 📌 Metric mAP50, 75
   
|              Version            | Train  | Infer     |  Config |  mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|---------------------------------|----------|-------|--------|----------|--------------|--------------|--------------|--------|--------------|--------------|----------------|
| V1                  | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Train/baseline_v1.ipynb) |[NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Inference/predict_script_v1.ipynb)     | [Config](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Train/Config/config_v1.yaml)  | 0.587 | 0.410 | 0.637 | 0.716 | 0.281 | 0.134 | 0.285 | 0.423     |
| V1 with TTA         | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Train/baseline_v1.ipynb) |[NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Inference/predict_script_tta_v1.ipynb)       |  [Config](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Train/Config/config_v1.yaml)  |  0.616 | 0.440 | 0.672 | 0.736 | 0.286 | 0.146 | 0.314 | 0.397     |
| V2                  | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Train/baseline_v2.ipynb) |[NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Inference/predict_script_v2.ipynb)       |  [Config](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Train/Config/config_v2.yaml)  |  0.639 | 0.457 | 0.697 | 0.763 | 0.294 | 0.141 | 0.316 | 0.425     |
| V3                  | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Train/baseline_v3.ipynb) |[NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Inference/predict_script_v3.ipynb)       | [Config](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Train/Config/config_v3.yaml)  |   0.665 | 0.504 | 0.712 | 0.779 | 0.319 | 0.158 | 0.340 | 0.460     |  
| V4                  | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Train/baseline_v4.ipynb) | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Inference/predict_script_v4.ipynb)       | [Config](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Train/Config/config_v4.yaml)  |   0.668 | 0.521 | 0.717 | 0.767 | 0.322 | 0.183 | 0.329 | 0.455     |
| V5                  | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Train/baseline_v5.ipynb) | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Inference/predict_script_v5.ipynb)       | [Config](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Train/Config/config_v5.yaml)  |   0.701 | 0.552 | 0.745 | 0.805 | 0.343 | 0.199 | 0.399 | 0.430     |
| V6                  | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Train/baseline_v6.ipynb) | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Inference/predict_script_v6.ipynb)       | [Config](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Train/Config/config_v6.yaml)  |   0.675 | 0.533 | 0.700 | 0.792 | 0.363 | 0.188 | 0.419 | 0.480     |
| V7                  |  X |[NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Inference/predict_script_v7.ipynb)       | [Config](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Train/Config/config_v6.yaml)  |   0.671 | 0.532 | 0.695 | 0.786 | 0.373 | 0.195 | 0.422 | 0.502     |


ColonoScopy 📌 Metric mAP50, 75
   
|              Version            | Train  | Inference  |   mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|---------------------------------|----------|-------|------|--------------|--------------|--------------|--------|--------------|--------------|----------------|
| V1                  | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/Colonoscopy/Train/baseline1.ipynb) | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/Colonoscopy/Inference/inference1.ipynb)     |    0.445 | 0.107 | 0.576 | 0.652 | 0.230 | 0.008 | 0.319 | 0.362     |
| V2                  | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/Colonoscopy/Train/baseline2.ipynb) | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/Colonoscopy/Inference/inference2.ipynb)      |    0.534 | 0.281 | 0.619 | 0.701 | 0.309 | 0.033 | 0.437 | 0.458     |
| V3                  | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/Colonoscopy/Train/baseline3.ipynb) | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/Colonoscopy/Inference/inference3.ipynb)      |    0.565 | 0.316 | 0.634 | 0.744 | 0.267 | 0.035 | 0.337 | 0.431     |
| V4                  | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/Colonoscopy/Train/baseline3.ipynb) | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/Colonoscopy/Inference/inference4.ipynb)      |    0.552 | 0.316 | 0.611 | 0.729 | 0.239 | 0.050 | 0.320 | 0.347     |
| V5                  | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/Colonoscopy/Train/baseline3.ipynb) | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/Colonoscopy/Inference/inference5.ipynb)      |    0.619 | 0.411 | 0.655 | 0.792 | 0.188 | 0.029 | 0.211 | 0.324     |
| V6                  | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/Colonoscopy/Train/baseline3.ipynb) | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/Colonoscopy/Inference/inference6.ipynb)      |    0.612 | 0.404 | 0.640 | 0.792 | 0.228 | 0.027 | 0.293 | 0.366     |


|     Version     |    Name       | Train  | Infer  |   mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|----------------|-----------------|--------|--------|------|--------------|--------------|--------|--------------|--------------|----------------|------|
| V1      | MViTv2_T(Faster-RCNN)   | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/Colonoscopy/Vit/Train/baseline_v1.ipynb)  |  [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/Colonoscopy/Vit/Inference/baseline_v1.ipynb)  |  0.678 | 0.447 | 0.718 | 0.870 | 0.333 | 0.0412 | 0.430 | 0.527     |


#### EfficientDet_TEST
GastroScopy 📌 Metric mAP50, 75

|     Version    | Name | Train  | Infer     |  mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|------------------|---------------|----------|-------|-----|--------------|--------------|--------------|--------|--------------|--------------|----------------|
| V1    | tf-efficientdet_d0              | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/EfficientDet/GastroScopy/Train/baseline_v1.ipynb) |[NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/EfficientDet/GastroScopy/Inference/predict_script_v1.ipynb)     |  0.399 | 0.335 | 0.167 | 0.695 | 0.139 | 0.092 | 0.020 | 0.305     |
| V2     | tf-efficientdet_d0               | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/EfficientDet/GastroScopy/Train/baseline_v2.ipynb) |[NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/EfficientDet/GastroScopy/Inference/predict_script_v2.ipynb)     |  0.591 | 0.550 | 0.448 | 0.775 | 0.213 | 0.129 | 0.148 | 0.363     |
| V3      | tf-efficientdet_d0              | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/EfficientDet/GastroScopy/Train/baseline_v3.ipynb) |[NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/EfficientDet/GastroScopy/Inference/predict_script_v3.ipynb)     |  0.624 | 0.528 | 0.535 | 0.809 | 0.279 | 0.180 | 0.223 | 0.433     |
| V4      | tf-efficientdet_d0              | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/EfficientDet/GastroScopy/Train/baseline_v4.ipynb) |[NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/EfficientDet/GastroScopy/Inference/predict_script_v4.ipynb)     |  0.620 | 0.536 | 0.528 | 0.794 | 0.293 | 0.212 | 0.207 | 0.458     |
| V5      | tf-efficientdet_d1             | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/EfficientDet/GastroScopy/Train/baseline_v5.ipynb) |[NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/EfficientDet/GastroScopy/Inference/predict_script_v5.ipynb)     |  0.689 | 0.551 | 0.713 | 0.803 | 0.376 | 0.199 | 0.432 | 0.498     |


ColonoScopy 📌 Metric mAP50, 75

|     Version    | Name | Train  | Infer     |  mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|------------------|---------------|----------|-------|-----|--------------|--------------|--------------|--------|--------------|--------------|----------------|
| V1    | Resdet50  | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/EfficientDet/ColonoScopy/Train/baseline_v1.ipynb) |  X  |  0.399 | 0.335 | 0.167 | 0.695 | 0.139 | 0.092 | 0.020 | 0.305     |

### 🎯 Ensemble with WBF(PostProcessing: Change Bboxes)

If you want to see applied wbf, nms, nmw, soft-nms, [click here](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Weighted-Boxes-Fusion/readme.md)

#### GastroScopy

- `YoloV11n` on 256X256, infer 256X256 - **mAP50: 0.658**, **mAP75: 0.354**
  
- `Detectron2` on 512X512, infer 512X512 - **mAP50: 0.671**, **mAP75: 0.373**

- `EfficientDet0` on 512X512 infer 512X512 - **mAP50: 0.689**, **mAP75: 0.376**

📌 After Applying Weighted-Box-Fusiones `mAP50` increases by `+0.05`, mAP75 increases by `+ 0.075`

=> `WBF` - **mAP50: 0.735**, **mAP75: 0.443**

If you want to see result report, [click here](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Weighted-Boxes-Fusion/GastroScopy/result_report.md)

![image](https://github.com/user-attachments/assets/e71b478f-b0d1-4233-bf54-72a88286d4f5)


|  Techniques to Combine Box |  Notebook  | mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|-------------|----------|--------|------|--------------|--------------|--------|--------------|--------------|----------------|
|  NMS    |   [Notebook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Weighted-Boxes-Fusion/GastroScopy/NMS.ipynb)  |  0.717 | 0.578 | 0.759 | 0.815 | 0.398 | 0.200 | 0.484 | 0.511     |
|  Soft-NMS    |  [Notebook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Weighted-Boxes-Fusion/GastroScopy/Soft_NMS.ipynb)  |  0.662 | 0.534 | 0.677 | 0.774 | 0.417 | 0.224 | 0.483 | 0.545   |
|  NMW    |    [Notebook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Weighted-Boxes-Fusion/GastroScopy/NMW.ipynb)  | 0.721 | 0.589 | 0.765 | 0.819 | 0.430 | 0.230 | 0.501 | 0.561    |
|  WBF    |  [Notebook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Weighted-Boxes-Fusion/GastroScopy/WBF.ipynb)  |   0.735 | 0.616 | 0.763 | 0.826 | 0.443 | 0.257 | 0.485 | 0.586     |

#### ColonoScopy

### 🔗 Calibrated Confidence Score(PostProcessing: Change Confidence order)

#### Bbox Confidence Score Order is Important
By simply adjusting the confidence scores of your bbox and not changing their xmin, xmax, ymin, ymax you can increase your mAP metrics. In the following example. the entire plot is 1class, each dot is 1 bbox and the numbers are confidence scores. If the confidence score for bbox D and G are changed then the mAP for this class increases by +0.12!! Therefore it is important to calibrate bbox probabilities.
![image](https://github.com/user-attachments/assets/a4eaaf2a-e2eb-4928-b7e8-7a2df09f4a6f)
The first probability is derived from the object detection model, representing the likelihood of a detected object belonging to a specific class. The second probability comes from the classifer model, refining this prediction by providing and independent confidence estimate.

To explore the relatvie importance of these two components, we conducted experiments by adjusting their contributions in the final confidence score. As a result, we modified the formula as follows:

             Confidence Score=P(class∣detection)^α×σ(classifier output)^β
wehre α and 𝛽 control the balance between the object detection model and the classifier model, allowing for optimal confidence calibration.


#### GastroScopy

📌 After Calibrated Confidence Score, mAP50 increases by +0.018, mAP75 increases by + 0.006

|  Alpha | Beta |   mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|--------|-------|----------|--------------|--------------|--------------|--------|--------------|--------------|----------------|
|   1.0  |  0.0  |    0.735 | 0.616 | 0.763 | 0.826 | 0.443 | 0.257 | 0.485 | 0.586     |
|   0.7  |  0.3  |     0.753 | 0.622 | 0.796 | 0.841 | 0.449 | 0.255 | 0.501 | 0.592   |
|   0.6  |  0.4  |     0.753 | 0.621 | 0.797 | 0.841 | 0.447 | 0.253 | 0.498 | 0.591     |
|   0.5  |  0.5  |     0.752 | 0.618 | 0.797 | 0.841 | 0.445 | 0.251 | 0.496 | 0.589   |
|   0.4  |  0.6  |     0.749 | 0.613 | 0.794 | 0.838 | 0.443 | 0.249 | 0.492 | 0.588     |
|   0.3  |  0.7  |     0.744 | 0.608 | 0.789 | 0.834 | 0.438 | 0.243 | 0.487 | 0.585     |      

#### ColonoScopy

### 🛴 RGB SuperPosition

If you want to sea more detail [click here](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/RGB-Superposition.md)

#### The process of creating an RGB Superposition Image

![image](https://github.com/user-attachments/assets/9645ec15-b0a2-4924-8432-461fd567b343)

#### Example with Bbox

![image](https://github.com/user-attachments/assets/12cd11bb-23d5-4867-b937-4ed13e62dd4d)



### ⚾ Next Step

- `Custom BBox Loss`
- `Custom FPN Architecture`
- `Adding Attention Techniques`
- `Exploration of other object detection library`
- `Exploration of other backbone model` 

### 📝 Citing
    {
      Author = {서윤제, 유민선},
      Title = {Endoscope Object Detection Model},
      Year = {2025},
      Publisher = {GitHub},
      Journal = {GitHub repository},
      Howpublished = {\url{https://github.com/SEOYUNJE/Endoscope-Object-Detection}}
    }


### 🧧 Contact

=> **서윤제's email**: seoyunje2001@gmail.com

=> **유민선's email**: msyu787@gmail.com
