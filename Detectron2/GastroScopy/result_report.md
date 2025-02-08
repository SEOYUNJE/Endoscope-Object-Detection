## [Detectron2 with CNN BackBone] My Journey to Test mAP50: 0.701 / mAP75: 0.343

I recently started studying two-stage models using the Detectron2 Library. Since it was my first time working with Detectron2, I initially struggled to get the hang of it. While searching for resources. I came across an excellent article and a well-organized GitHub repository that really helped me. I'd love to share them with you!

=> [Introduction how to use Detectron2](https://github.com/PacktPublishing/Hands-On-Computer-Vision-with-Detectron2)

=> [Introudction 2Stage Model Architecture](https://medium.com/@hirotoschwert/digging-into-detectron-2-part-4-3d1436f91266)

Now, let me show you my tricks and approach to developing a Detectron2 model.

### Part-1: Build Pipeline Notebook(Test mAP50: 0.587 / mAP75: 0.281)

First, I built a Detectron2 model using the backbone with the fewest parameters from the Model Zoo. Unfortunately, my dataset consists of only 1,597 gastroscopy training images, making it challenging to fine-tune a deeper model effectively. 
So I select **`faster_rcnn_R_5O_FPN_1x`**. But there are models you can experiment with your project

- **`faster_rcnn_R_50_FPN_3x`**
- **`faster_rcnn_R_101_FPN_3x`**
- **`faster_rcnn_X_101_32x8d_FPN_3x`**

### Part-2: To the Test mAP50: 0.616 / mAP75: 0.286

Detectron2 provieds built-in test-time augmentation(TTA) through `detectron2.modeling`. We can implement a TTA architecture using `GeneralizedRCNNWithTTA` and `DatasetMapperTTA`, incorporating augmentations like flipping and rescaling. After running several experiments, We discoverd that simply appyling flip augmentation yielded the best test mAP

**Note**: When Applying TTA, Heavy augmentation could worse your metric. 

### Part-3: To the Test mAP50 0.639 / mAP75 0.294

This time, We focus on applying augmentations using Albumentation library. If you're curious about how it works, feel free to explore [this resource](https://explore.albumentations.ai/) 

As you know, our dataset is quite small. To enhacne generalization performance, extensive data augmentation is essential.

Here are the Albumentations augmentations that proved to be effective

| Transform Type      | Augmentation |
|----------------------|-------------|
|  Flip Transfrom | **Horizontal Flip**   |
|  Image Enhancement Transform  | **Contrast Limited Adaptive Histogram Equalization**   |
|  Channel Transform | **ToGray**, **ChannleDropout**, **ChannelShift**, **RGBShift**   |
|  Dropout Transform  | **XYMasking**, **CoarseDropout**, **BBoxSafeRandomCrop**  |
|  Noisy Transform  | **RandomGravel**, **RandomSnow**  |

![image](https://github.com/user-attachments/assets/dcc2f298-5d66-4960-8f88-8d3fa53a2e58)

### Part-4: To the Test mAP50 0.665 / mAP75 0.319

In Part3, We experiment with simple augmentatins. This time, We took it as step further by incorporating more advanced techniques, specifically `MixUp Transform` and `Mosaic Transform`, to enhance generalization performance. 

For MixUp Transform, instead of using a fixed value of 0.5, we applied a more dynamic. approach by sampling from a beta distribution(`np.random.beta(2.0, 2.0)`. This allows for more diverse mixing ratios, potentially improving robustness.

For Mosaic Transform, rather than simply dividng images at the center coordinates, we implemented a custom mosaic transformation This approach provides more flexibility in image composition.

![image](https://github.com/user-attachments/assets/fb09ae8c-0b67-4a5f-af38-00e701974c0f)

### Part-5: To the Test mAP50 0.668 / mAP75 0.322

We refined our training configuraton by adjusting key hyperparameters such as `batch_size`, `base_lr_end`, `weight_decay`, `warmup_factor`, and `warmup_iters` to imporve training stability and convergence. 

| Config      |  Before      |    After      |  
|----------------------|-------------|---------------|
|  **Batch Size** |  16   |  8 |
|  **base_lr_end**  | 0   |  1e-9 |
|  **weight_decay** | 1e-5  | 1e-4 |
|  **warmup_factor**  | 1e-3 | 1e-4 |
|  **warmup_iters**  | max_iters//40  | max_iters//20 |

#### Why These Changes?

- `Batch Size (16 → 8)`: Since our dataset is relatively small, reducing the batch size helps prevent overfitting and allows the model to generalize better. Additionally, a smaller batch size often leads to noisier gradient updates, which can act as implicit regularization.

- `base_lr_end (0 → 1e-9)`: Previously, the learning rate would drop to zero at the end of training, which could cause premature convergence. Setting a small but nonzero value (1e-9) ensures a smoother transition and prevents sudden learning stagnation.

- `Weight Decay (1e-5 → 1e-4)`: Increasing weight decay helps prevent overfitting by adding stronger regularization, which is crucial given our limited dataset size.

- `Warmup Factor (1e-3 → 1e-4)`: A smaller warmup factor slows down the initial learning rate increase, leading to more stable weight updates at the beginning of training.

- `Warmup Iters (max_iters // 40 → max_iters // 20)`: Extending the warmup period allows the model to gradually adjust to the learning rate, reducing the risk of unstable updates early in training.

### Part-6: To the Test mAP50 0.701 / mAP75 0.343

In Part 6, We focused on optimizing the `loss function` and `image resolution`. Our first step was experimenthing with different bounding box(bbox) loss functions.
As you may know, there are five commonly used bbox regression loss functions. If you're interested in learning more about box regression losses in detail, [click here](https://medium.com/@gavin_xyw/those-bounding-box-regression-losses-in-object-detection-184595731b2e)

And this time, we change from `smooth_l1` to `ciou`. Let's see Each loss function

**Smooth_L1 Loss**

Smooth L1-los can be interpreted as a combination of L1-loss and L2-loss

![image](https://github.com/user-attachments/assets/9ce4442a-ecf9-4f80-8a4f-82a8e45a974f)

**CIoU Loss**

A good loss for bounding box regression should consider the important geometric factors, i.e, `overlap area`, `central point distance` and `aspect ratio`. By uniting the coorinates

- **IoU loss**: just consider the overlap area
- **GIoU loss**: it heavily relies on IoU loss
- **DIoU loss**: it aims at considering simultaneously the overlap area and central point distance of bounding boxes. 
- **CIoU loss**: it aims overlap_area, central point distance, aspect ratio 

**Image Resolution**

Next, we adjusted the image resolution, increasing from **[256,256]** to **[512,512]**. We conducted experiments with various image sizes, i.e, 256, 384, 512, 768 and 1024 to evaluate their impact on performance.
However, we found that simply using a larger image size did not always lead to improved mAP scores. After extensive testing, we determined that **[512,512]** was the optimal resoution, striking the right balance between performance and computational efficiency. 
Additionally, we considered a two-stage training approach where we first trained the model on smaller images and then fine-tuned it with larger ones. Unfortunately, this strategy did not yield better results.

**Pooler_resolution**: 

In the Box Head Stage, The base ROI pooler resolution was set to `14X14`. Increasing this resolution allows for capturing finer details and preserving more spatial information, which can potentially enhance mAP performance
![image](https://github.com/user-attachments/assets/14c31f7d-8d77-4cb6-8344-0737ed3e8ed5)
