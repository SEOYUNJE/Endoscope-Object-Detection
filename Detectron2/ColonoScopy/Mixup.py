class MixUpAug(T.Augmentation):
    def __init__(self, cfg, src_weight = 0.5, dst_weight = 0.5):
        self.cfg = cfg
        self.sampler = DataDictSampler(cfg.DATASETS.TRAIN[0])
        self.src_weight = src_weight
        self.dst_weight = dst_weight

    def get_transform(self, image, dataset_dict):
        cfg = self.cfg

        ds_dict = self.sampler.get_items(n=1)[0] # random pick
        mu_image = utils.read_image(ds_dict['file_name'], format=cfg.INPUT.FORMAT)
        annotations = ds_dict['annotations']
        dataset_dict['annotations'] += annotations
        mu_boxes = np.array([
            BoxMode.convert(
                obj['bbox'], obj['bbox_mode'],
                BoxMode.XYXY_ABS)
            for obj in annotations
        ])

        return MixUpTransform(
             image = image,
             mu_image = mu_image,
             mu_boxes = mu_boxes,
             src_weight = self.src_weight,
             dst_weight = self.dst_weight,
            )
    def __repr__(self):
        return f'MixUp(src {self.src_weight}, dst {self.dst_weight})'

class MixUpTransform(T.Transform):
    def __init__(self, image, mu_image, mu_boxes,
                 src_weight = 0.5, dst_weight = 0.5):
        image_size = image.shape[:2]
        rse = T.ResizeShortestEdge([min(image_size)],
                                    min(image_size),
                                   "choice")
        aug_i = T.AugInput(image=mu_image, boxes = mu_boxes)
        rse(aug_i)
        mu_image, mu_boxes = aug_i.image, aug_i.boxes

        img = np.zeros_like(image).astype('float32')
        img[:mu_image.shape[0], :mu_image.shape[1],:] = mu_image

        self.mu_image = img
        self.mu_boxes = mu_boxes
        self.src_weight = src_weight
        self.dst_weight = dst_weight

    def apply_image(self, image):
        bl_tfm = T.BlendTransform(src_image = self.mu_image,
                                  src_weight = self.src_weight,
                                  dst_weight = self.dst_weight)
        return bl_tfm.apply_image(image)
        
    def apply_coords(self, coords):
        return coords
    def apply_box(self, boxes):
        boxes = np.vstack([boxes, self.mu_boxes])
        return boxes
