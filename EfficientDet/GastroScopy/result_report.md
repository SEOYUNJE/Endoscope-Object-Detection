# My Journey to Test mAP50: 0.671 / mAP75: 0.373

I chose the `EfficientDet` model primarily due to the limited size of my dataset, which consists of only about 1,300 training images. Given the small dataset, selecting a model that performs well with fewer training samples was crucial. Among the three models I considered - `YOLO`,`Detectron2`, and `EfficientDet` , EfficientDet demonstrated the best mAP score, making it the most suitable choice for my task. its efficiency in handling small datasets while maintaining high detection performance ultimately led me to select it over the alternatives

[Tensorflow EfficientDet Github](https://github.com/xuannianz/EfficientDet)

[Pytorch EfficientDet Github](https://github.com/rwightman/efficientdet-pytorch)

### Part-1: Build Pipeline Notebook(Test mAP50: 0.399 / mAP75: 0.139)

The Pytorch EfficientDet GitHub repository provides a variety of models, each optimized for different use cases. 

- `tf-efficientdet_lite`: A lightweight version of EfficientDet optimized for mobile deployment
  
- `tf_efficientdet`: The Tensorflow-based implementation of EfficientDet

- `efficientdet`: The PyTorch implementation of EfficientDet
  
- `efficientdetv2`: An improved version of EfficientDet with enhanced performances.
   
- `resdet`: 1 Stage Detection Model with ResNet backbone
  
- `cspresext`: 1 Stage Detection Model with CSP-ResNext bacbkone

- `cspresdet`: 1 Stage Detection Model with CSP-Resnet backbone

- `cspdarkdet`: 1 Stage Detection Model with CSP-DarkNet backbone

=> we utilized default_detection model_configs, which defines the backbone as **tf_efficientnet_b0** and the model as **tf_efficientdet_d0** for fast experiment.


### Part-2: Train Config(Test mAP50: 0.591 / mAP75: 0.213)

| config      | value |
|----------------------|-------------|
|  🏋️‍♂️ train batch_size | **16**   |
|  🧪 valid_batch_size  | **32**   |
|  📉 scheduler_type | **CosineAnnealingLR**   |
|  🚀 base_lr  | **1e-3**  |
|  🔽 min_lr  | **1e-9**  |
|  🏗 weight_decay  | **1e-5**  |
|  🚀optimizer  | **AdamW** |

This setup ensures a well-balanced training process with CosineAnnealingLR for smooth learning rate adjustments, maintaining efficiency and stability throughout training. 🔥

### Part-3: FPN Architecture(Test mAP50: 0.624 / mAP75: 0.279)

In this time, we focused on **`Feature Pyramid Nework(FPN)`**.

In our experiments; we considere five key factors, each influencing different aspects of the FPN design

![image](https://github.com/user-attachments/assets/f025cb4a-e898-4d94-b3d9-91b124d8633b)

1) `FPN Architecture`: This refers to the overall structure and design of the FPN, including how the feature pyramids are constructed and integrated within the network.

   - **FPN(Feature Pyramid Network)**
   - **BiFPN(Bidrectional Feature Pyramid Network)** - We Used
   - **PAN(Path Aggregation Network)**
   - **QUPN(Quasi-Pyramid Network)**
     
2) `FPN Node Weighted Method`: This facotr explores the different methods for weighting the nodes within the pyrammid, which can impact how features are prioritized at each level.
   - **sum**: In configurations with `fpn-cell-repeats=1`, the sum method occasionally outperforms fast-attentions.
   - **fast-attn**: this method offers a balanced results, providing competitive performance without the complexity of more intricate methods. 
   - **attn**: this method often yields comparable or slightly lower metrics than the fast-attn method.

3) `FPN Channel`: This refers to the number of channels used at each pyramid level, directly impacting the model's capacity to capture and process information. The default setting was 64, but we experimented with expansions to 128,256,384,512,640 and 768. Notably, in tf-efficientdet-d0, a channel size of 384 yielded the best performance.

4) `FPN Cell Repeats`: This involves adjusting the number of repetitions of cells within the network, affecting the depth and capacity of the FPN architecture. In Bi-FPN, we experimented with repetitions ranging from 1 to 5, and found that repeating the block 3 times yielded the highest mAP.


### Part-4: HeadNet and Some Tricks(Test mAP50: 0.620 / mAP75: 0.293)

### Part-5: Deeper Parameter, Higher Resolution(Test mAP50: 0.689 / mAP75: 0.376)
