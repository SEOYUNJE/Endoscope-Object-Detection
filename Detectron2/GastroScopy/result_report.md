## [Detectron2] My Journey to Test mAP50: 0.701 / mAP75: 0.343

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
