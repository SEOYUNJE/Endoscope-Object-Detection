class MosaicAug(T.Augmentation):
    def __init__(self, cfg):
        self.cfg = cfg
        self.sampler = DataDictSampler(cfg.DATASETS.TRAIN[0])

    def get_transform(self, image, dataset_dict):
        cfg = self.cfg
        mo_items = self.sampler.get_items(n=3) # n = 3
        mo_images = []
        mo_boxes = []
        for ds_dict in mo_items:
            mo_image = utils.read_image(ds_dict['file_name'], format=cfg.INPUT.FORMAT)
            mo_images.append(mo_image)
            annotations = ds_dict['annotations']

            mo_boxes.append(np.array([
                BoxMode.convert(
                    obj['bbox'],
                    obj['bbox_mode'], BoxMode.XYXY_ABS)
                for obj in annotations
            ]))
            dataset_dict['annotations'] += annotations
        return MosaicTransform(mo_images, mo_boxes)

class MosaicTransform(T.Transform):
    def __init__(self, mo_images, mo_boxes):
        self.mo_images = mo_images # default: 3 images
        self.mo_boxes = mo_boxes

    def get_loc_info(self, image):
        images = [image] + self.mo_images # 3 images + 1 original_image
        heights = [i.shape[0] for i in images] 
        widths =  [i.shape[1] for i in images]

        ch = max(heights[0], heights[1]) # original vs mosaic
        cw = max(widths[0], widths[2]) # original vs mosaic
        h = (max(heights[0], heights[1]) + 
             max(heights[2], heights[3]))
        w = (max(widths[0], widths[2]) +
             max(widths[1], widths[3]))
        # pad or start coordinates 
        y0, x0 = ch - heights[0], cw - widths[0]
        y1, x1 = ch - heights[1], cw
        y2, x2 = ch, cw - widths[2]
        y3, x3 = ch, cw 
        x_pads = [x0, x1, x2, x3]
        y_pads = [y0, y1, y2, y3]
        return (h, w, ch, cw, widths, heights, x_pads, y_pads)

    def apply_image(self, image):
        self.loc_info = self.get_loc_info(image)
        h, w, ch, cw, widths, heights, x_pads, y_pads = self.loc_info
        output = np.zeros((h,w,3)).astype(np.uint8)
        images = [image] + self.mo_images
        for i, img in enumerate(images):
            output[y_pads[i]: y_pads[i] + heights[i],
                   x_pads[i]: x_pads[i] + widths[i],
                   :] = img
        return output
        
    def apply_coords(self, coords):
        return coords
    def apply_box(self, boxes):
        boxes = [boxes] + self.mo_boxes
        _, _, _, _, _, _, x_pads, y_pads = self.loc_info
        for i, bbox in enumerate(boxes):
            bbox += np.array([x_pads[i], y_pads[i], x_pads[i], y_pads[i]])
            
        boxes = np.vstack(boxes)
        return boxes
