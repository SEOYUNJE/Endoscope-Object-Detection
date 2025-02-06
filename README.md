![image](https://github.com/user-attachments/assets/781a248d-6091-438a-b3ec-674da69c4bd4)


## 📚 Project Introduction 📚
**📌 Project Name** 
   
=> 딥러닝 기반 위,대장 내시경 영상 내 질환 자동 검출 
    
**📌 Project Goal**
    
=> 1Stage Model부터 2Stage Model까지 다양한 모델 Architecture 공부 및 의료 이미지 도메인에 대한 이해 향상을 목표로 합니다 

**📌 Lesion Detection**

=> AI를 통해 위장, 대장 내 궤양, 용종, 암 검출 가능 

![image](https://github.com/user-attachments/assets/8ba85673-6c77-465c-a990-688d4f6ff05b)


**📌 Project Background**

내시경 판독의 경우 장기간에 걸쳐 지속적으로 병변을 판독해야 합니다. 이는 집중력의 감소로 인해 휴먼에러를 야기하며, 판독을 시행하는 사람의 경험과 주관에 따라 다른 결론이 날 여지가 있습니다.

본 프로젝트에서 개발하는 인공지능 모델은 사람을 대신하여 내시경 동영상을 빠르고 정확하게 판독하고 질병의 진단을 손쉽게 하여 질병의 진행을 예방하고자 합니다.

![image](https://github.com/user-attachments/assets/adb89331-959d-419c-985d-564bf5452960)

   
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

5. [Inference](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#-inference)

   I. [Yolo](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#yolo_test)
   
   II. [Detectron2](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#detectron2_test)

   III. [EfficientDet](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#efficientdet_test)


7. [Ensemble with WBF](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#-ensemble-with-wbf)

8. [Calibrated Confidence Score](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#-calibrated-confidence-score)

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

</details>

<details>
<summary> ColonoScopy</summary>
<br>

</details>

#### Detectron2
<details>
<summary> GastroScopy</summary>
   
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

![image](https://github.com/user-attachments/assets/84fa4b7a-04a0-4ecd-83c9-6c5160a3d7bc)

![image](https://github.com/user-attachments/assets/b2139a4c-ea9a-4699-94fc-dc9a23241d74)

#### Version 7

**Backbone**: `faster_rcnn_R_50_FPN_1x -> faster_rcnn_X_101_32x8d_FPN_3x`

</details>

<details>
<summary> ColonoScopy</summary>
<br>

</details>

#### EfficientDet
<details>
<summary> GastroScopy</summary>
<br>

</details>

<details>
<summary> ColonoScopy</summary>
<br>

</details>

### ⛳ Inference

#### YOLO_TEST
<details>
<summary>  GastroScopy 📌 Metric mAP50, 75</summary>
<br>

|              Version            | Link     |   mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|---------------------------------|----------|----------|--------------|--------------|--------------|--------|--------------|--------------|----------------|
| V1                  | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Yolo/GastroScopy/Inference/inference_v1.ipynb)     |    0.466 | 0.148 | 0.540 | 0.594 | 0.229 | 0.090 | 0.240 | 0.356     |
| V2      | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Inference/predict_script_tta_v1.ipynb)       |    0.574 | 0.420 | 0.631 | 0.671 | 0.324 | 0.209 | 0.348 | 0.397     |
| V3                 | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Yolo/GastroScopy/Inference/inference_v3.ipynb)       |    0.532 | 0.390 | 0.548 | 0.658 | 0.301 | 0.180 | 0.309 | 0.412     |
| V4                 | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Yolo/GastroScopy/Inference/inference_v4.ipynb)       |    0.529 | 0.354 | 0.598 | 0.636 | 0.312 | 0.218 | 0.313 | 0.404     |  

</details>

<details>
<summary>  ColonoScopy 📌 Metric mAP50, 75</summary>
<br>

</details>

#### Detectron2_TEST
<details>
<summary> GastroScopy 📌 Metric mAP50, 75</summary>
<br>
   
|              Version            | Link     |  Config |  mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|---------------------------------|----------|---------|----------|--------------|--------------|--------------|--------|--------------|--------------|----------------|
| V1                  | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Inference/predict_script_v1.ipynb)     | [Config](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Train/Config/config_v1.yaml)  | 0.587 | 0.410 | 0.637 | 0.716 | 0.281 | 0.134 | 0.285 | 0.423     |
| V1 with TTA         | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Inference/predict_script_tta_v1.ipynb)       |  [Config](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Train/Config/config_v2.yaml)  |  0.616 | 0.440 | 0.672 | 0.736 | 0.286 | 0.146 | 0.314 | 0.397     |
| V2                  | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Inference/predict_script_v2.ipynb)       |  [Config](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Train/Config/config_v3.yaml)  |  0.639 | 0.457 | 0.697 | 0.763 | 0.294 | 0.141 | 0.316 | 0.425     |
| V3                  | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Inference/predict_script_v3.ipynb)       | [Config](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Train/Config/config_v4.yaml)  |   0.665 | 0.504 | 0.712 | 0.779 | 0.319 | 0.158 | 0.340 | 0.460     |  
| V4                  | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Inference/predict_script_v4.ipynb)       | [Config](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Train/Config/config_v5.yaml)  |   0.668 | 0.521 | 0.717 | 0.767 | 0.322 | 0.183 | 0.329 | 0.455     |
</details>

<details>
<summary> ColonoScopy 📌 Metric mAP50, 75</summary>
<br>
   
|              Version            | Link     |   mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|---------------------------------|----------|----------|--------------|--------------|--------------|--------|--------------|--------------|----------------|
| V1                  | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Inference/predict_script_v1.ipynb)     |    0.740 | 0.756 | 0.682 | 0.781 | 0.460 | 0.580 | 0.325 | 0.475     |
| V1 with TTA         | [NoteBook](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Detectron2/GastroScopy/Inference/predict_script_v1.ipynb)       |    0.742 | 0.745 | 0.685 | 0.797 | 0.449 | 0.597 | 0.291 | 0.458     |
| Version 3                  | 29       |                                                                 |
| Version 4                  | 1        |                                                                 |
</details>

#### EfficientDet_TEST
<details>
<summary>  GastroScopy 📌 Metric mAP50, 75</summary>
<br>

</details>

<details>
<summary>  ColonoScopy 📌 Metric mAP50, 75</summary>
<br>

### 🎯 Ensemble with WBF

### 🔗 Calibrated Confidence Score

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
