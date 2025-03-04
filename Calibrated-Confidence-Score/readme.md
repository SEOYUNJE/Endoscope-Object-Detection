### Before Calibrated Confidence Score(WBF)

Before applying the Calibrated Confidence Score, we experimented with Weighted Box Fusion, which adjusts xmin, xmax, ymin, and ymax to refine bounding box predictions. This approach led to improved mAP metrics.

<GastroScopy>
  
- `YoloV11n` on 256X256, infer 256X256 - **mAP50: 0.658**, **mAP75: 0.354**
  
- `Detectron2` on 512X512, infer 512X512 - **mAP50: 0.671**, **mAP75: 0.373**

- `EfficientDet0` on 512X512 infer 512X512 - **mAP50: 0.689**, **mAP75: 0.376**

📌 After Applying Weighted-Box-Fusiones `mAP50` increases by `+0.05`, mAP75 increases by `+ 0.075`

=> `WBF` - **mAP50: 0.735**, **mAP75: 0.443**

<ColonoScopy>



### Bbox Confidence Score Order is Important

By simply adjusting the confidence scores of your bbox and not changing their xmin, xmax, ymin, ymax you can increase your mAP metrics. In the following example. the entire plot is 1class, each dot is 1 bbox and the numbers are confidence scores. If the confidence score for bbox D and G are changed then the mAP for this class increases by +0.12!! Therefore it is important to calibrate bbox probabilities.

![image](https://github.com/user-attachments/assets/837c1ffb-26bc-4f1d-8e97-5924064bacf1)

![image](https://github.com/user-attachments/assets/f869f981-6859-422b-bd0b-7d1d1278805c)

### Calibrated Confidence Scores

As you know, we have trained three models—YOLO, Detectron2, and EfficientDet—all of which utilize conditional class probabilities through softmax when classifying ulcer, polyp, and cancer.

Therefore, the confidence score predicted by your object detection model is given by:

                        Confidence Score = 𝑃(class∣detection)


Therefore to get the calibrated probability, you must use use Multiple independent binary probabilities with sigmoid. So we use our classifier and the formula 

=> [GastroScopy Classifier (Tensorflow)](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Calibrated-Confidence-Score/gastroscopy_tf_classify.ipynb)

=> [ColonoScopy Classifier (PyTorch Lightning)](https://github.com/SEOYUNJE/Endoscope-Object-Detection/blob/main/Calibrated-Confidence-Score/colonoscopy_pytorchlightning.ipynb)


                 Confidence Score=P(class∣detection)×σ(classifier output)

The first probability is derived from the **object detection model**, representing the likelihood of a detected object belonging to a specific class. The second probability comes from the **classifer model**, refining this prediction by providing and independent confidence estimate.

To explore the relatvie importance of these two components, we conducted experiments by adjusting their contributions in the final confidence score. As a result, we modified the formula as follows:

                 Confidence Score=P(class∣detection)^α×σ(classifier output)^β
wehre  α and 𝛽 control the balance between the object detection model and the classifier model, allowing for optimal confidence calibration. 

### Tracking mAP Metrics

📌 After Calibrated Confidence Score, mAP50 increases by +0.18, mAP75 increases by + 0.006

|  Alpha | Beta |   mAP@50 | mAP@50-Ulcer | mAP@50-Polyp |mAP@75-Cancer | mAP@75 | mAP@75-Ulcer | mAP@75-Polyp | mAP@75-Cancer  |
|--------|-------|----------|--------------|--------------|--------------|--------|--------------|--------------|----------------|
|   1.0  |  0.0  |    0.735 | 0.616 | 0.763 | 0.826 | 0.443 | 0.257 | 0.485 | 0.586     |
|   0.7  |  0.3  |     0.753 | 0.622 | 0.796 | 0.841 | 0.449 | 0.255 | 0.501 | 0.592   |
|   0.6  |  0.4  |     0.753 | 0.621 | 0.797 | 0.841 | 0.447 | 0.253 | 0.498 | 0.591     |
|   0.5  |  0.5  |     0.752 | 0.618 | 0.797 | 0.841 | 0.445 | 0.251 | 0.496 | 0.589   |
|   0.4  |  0.6  |     0.749 | 0.613 | 0.794 | 0.838 | 0.443 | 0.249 | 0.492 | 0.588     |
|   0.3  |  0.7  |     0.744 | 0.608 | 0.789 | 0.834 | 0.438 | 0.243 | 0.487 | 0.585     |                 
