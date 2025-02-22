from detectron2.data import DatasetMapper
import albumentations as A
import copy
import detectron2.data.transforms as T
import detectron2.data.detection_utils as utils
from detectron2.structures import BoxMode

class DataDictSampler():
    def __init__(self, name_ds_train):
        ds = DatasetCatalog.get(name_ds_train)
        self.ds = ds
        
    def get_items(self, n=3):
        indices = np.random.randint(
            0, len(self.ds)-1, n
        )
        return [copy.deepcopy(self.ds[_]) for _ in indices]

## Extended 변경점: Apply dataset_dict
class ExtendedAugInput(T.AugInput):
    def __init__(self, image, *, boxes=None, sem_seg=None, dataset_dict=None):
        super().__init__(image, sem_seg=sem_seg, boxes=boxes)
        self.dataset_dict = dataset_dict
        self.is_train = True

## Extended 변경점: 
class ExtendedDatasetMapper(DatasetMapper):
    """기존 bbox -> transformed bbox로 변경"""
    def _convert_annotations(self, dataset_dict, boxes, image_shape):
        annos = []
        for i, annotation in enumerate(dataset_dict.pop('annotations')):
            bbox = boxes[i]
            annotation['bbox'] = bbox
            annotation['bbox_mode'] = BoxMode.XYXY_ABS
            annos.append(annotation)
        instances = utils.annotations_to_instances(
            annos, image_shape, mask_format=self.instance_mask_format
        )
        if self.recompute_boxes:
            instance.gt_boxes = instances.gt_masks.get_bounding_boxes()
        dataset_dict['instances'] = utils.filter_empty_instances(instances)

    def __call__(self, dataset_dict):
        dataset_dict = copy.deepcopy(dataset_dict)
        image = utils.read_image(dataset_dict['file_name'], format=self.image_format)

        if "sem_seg_file_name" in dataset_dict:
            sem_seg_gt = utils.read_image(
                 dataset_dict.pop("sem_seg_file_name"), "L"
                 ).squeeze(2)
        else:
            sem_seg_gt = None

        boxes = np.array([
            BoxMode.convert(
                obj['bbox'],
                obj['bbox_mode'], BoxMode.XYXY_ABS)
            for obj in dataset_dict['annotations']])

        aug_input = ExtendedAugInput(image,
                                     sem_seg = sem_seg_gt,
                                     dataset_dict = dataset_dict,
                                     boxes = boxes)
        transforms = self.augmentations(aug_input)
        image = aug_input.image 
        
        dataset_dict = aug_input.dataset_dict
        boxes = aug_input.boxes

        image_shape = image.shape[:2]
        dataset_dict['image'] = torch.as_tensor(image.transpose(2,0,1).astype(np.float32))

        if "annotations" in dataset_dict:
            self._convert_annotations(dataset_dict, boxes, image_shape)
        
        return dataset_dict
