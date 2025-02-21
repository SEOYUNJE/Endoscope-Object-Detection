# RGB_Superposition

So far, our focus has been on post-processing techniques such as calibrated confidence scoring and weighted boxes fusion. Weighted Boxes Fusion was applied to refine bounding box coordinates for more precise localization, while the Calibrated Confidence Score aimed to enhance the reliability of confidence estimates without altering the bounding boxes.

We observed a significant improvement across tow stages:

- **After applying Weighted Boxes Fusion**, mAP50 increased by +0.05, and mAP75 saw a +0.075 improvement
- **After calibrating confidence score**, mAP50 improved by +0.018, while mAP75 gained +0.006

This time, our focus shifted towards preprocessing techniques to further enhance our model's performance.

In our dataset, we observed the presence of polygon masks, which led us to explore the best way to integrate them into our preprocessing pipeline. After careful consideration, we decided to leverage mask images to refine the input representation.

To effectively incorporate mask information while preserving essential features, we opted for RGB-Superposition, a technique that enables the seamless fusion of mask data with RGB channels. This approach allows our model to leverage both spatial and structural information, ultimately enhancing its ability to make more precise predictions.

=> **`After applying RGB Superpositions in image, mAP50 increased by + 0.25, and mAP75 increased by + 0.55`**

### 📌 The process of creating an RGB Superposition Image

![image](https://github.com/user-attachments/assets/c0c00493-dc86-4a29-a837-285e7dc15e47)


### 📌 Generated RGB Superposition Image

![image](https://github.com/user-attachments/assets/17c0045c-d135-4de5-8d58-95f87bdb80e7)

![image](https://github.com/user-attachments/assets/c8a3d957-cc8a-462e-a77e-d391f27b333c)

![image](https://github.com/user-attachments/assets/5e49b63a-1edb-468b-b746-820dae0f2d86)


### Metrics 

|  Image Type |   Val mAP@50 | Val mAP@50-Ulcer | Val mAP@50-Polyp |Val mAP@75-Cancer | Val mAP@75 | Val mAP@75-Ulcer | Val mAP@75-Polyp | Val mAP@75-Cancer  |
|--------|-----------|--------------|--------------|--------------|--------|--------------|--------------|----------------|
|   original Image    |    0.683 | 0.627 | 0.624 | 0.797 | 0.334 | 0.260 | 0.295 | 0.447     |
|   MR+OG+OB   |     0.957 | 0.984 | 0.909 | 0.977 | 0.905 | 0.984 | 0.764 | 0.968   |
|   MR+OG+OR    |     0.951 | 0.991 | 0.882 | 0.979 | 0.895 | 0.991 | 0.724 | 0.970     |
|   MR+OB+OR    |     0.947 | 0.988 | 0.878 | 0.976 | 0.886 | 0.988 | 0.713 | 0.956   |
|   MG+OG+OB    |     0.950 | 0.978 | 0.895 | 0.977 | 0.894 | 0.978 | 0.734 | 0.971     |
|   MG+OG+OR    |     0.946 | 0.983 | 0.879 | 0.974 | 0.883 | 0.983 | 0.716 | 0.950    | 
|   MG+OB+OR    |     0.944 | 0.983 | 0.875 | 0.974 | 0.883 | 0.983 | 0.708 | 0.959    | 
|   MB+OG+OB    |     0.744 | 0.608 | 0.789 | 0.834 | 0.438 | 0.243 | 0.487 | 0.585    | 
|   MB+OG+OR    |     0.744 | 0.608 | 0.789 | 0.834 | 0.438 | 0.243 | 0.487 | 0.585    | 
|   MB+OB+OR    |     0.744 | 0.608 | 0.789 | 0.834 | 0.438 | 0.243 | 0.487 | 0.585    | 


### 📌 Example with Bbox

![image](https://github.com/user-attachments/assets/7e936296-cf26-4c0f-b8b4-547db0925b0e)
