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
   
    I. [Gastroscopy EDA](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#-gastroscopy-eda)
   
    II. [Colonoscopy EDA](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#-colonoscopy-eda)

4. Train

5. Eval

6. Test 

7. [Citing](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#-citing)

8. [Contact](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/README.md#-contact)

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
=> 
</details>


<details> 
<summary>구축목적</summary>
<br>
=> 리소스 자원의 한계로 인해 4만장의 대용량 데이터셋 학습에 무리가 있음. 이에 리소스 자원 내 모델 학습 및 최적화를 위해 소규모 데이터셋을 구축함. 
</details>

<details>
<summary>데이터 구축 규모</summary>
<br>
위 내시경 이미지 합성데이터 2,000장(암 1,000장, 용종 500장, 궤양 500장)

![image](https://github.com/user-attachments/assets/a8e9376f-9f14-4d3f-98ef-1ce7da305a82)

</details>


#### Colonoscopy Dataset

<details> 
<summary>주소</summary>
<br>
=> 
</details>

<details> 
<summary>구축목적</summary>
<br>
=> 리소스 자원의 한계로 인해 4만장의 대용량 데이터셋 학습에 무리가 있음. 이에 리소스 자원 내 모델 학습 및 최적화를 위해 소규모 데이터셋을 구축함. 
</details>

<details>
<summary>데이터 구축 규모</summary>
<br>
대장 내시경 이미지 합성데이터 2,000장(암 1,000장, 용종 500장, 궤양 500장)

</details>


### 💡 Exploratory Data Analysis

#### Gastroscopy EDA

#### Colonoscopy EDA


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
