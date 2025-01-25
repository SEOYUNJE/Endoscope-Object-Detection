!pip install -q pycocotools

from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

class EndoscopeEval:
    def __init__(self, true_df):
        self.true_df = true_df
        self.image_ids = true_df['image_id'].unique()
        self.annotations = {
            'type': 'instances',
            'images': self.__gen_images(self.image_ids),
            'categories': self.__gen_categories(self.true_df), 
            'annotations': self.__gen_annotations(self.true_df, self.image_ids)
        }
        self.predictions = {
            'images': self.annotations['images'].copy(),
            'categories': self.annotations['categories'].copy(),
            'annotations': None,
        }
    def __gen_categories(self, df):
        print(f'{Fore.GREEN}#'*25)
        print('Generating category data...')
        print(f'#'*25)
  
        cats = df[['lesion', 'lesion_label']]
        cats = cats.drop_duplicates().sort_values(by='lesion_label').values

        results = []
        for cat in cats:
            results.append({
                'id': cat[1],
                'name': cat[0],
                'supercategory': 'none',
            })
        return results

    def __gen_images(self, image_ids):
        print(f'{Fore.GREEN}#'*25)
        print('Generating image data...')
        print('#'*25) 

        results = []
        for idx, image_id in enumerate(image_ids):
            results.append({
                'id': idx,
            })
        return results

    def __gen_annotations(self, df, image_ids):
        print(f'{Fore.GREEN}#'*25)
        print('Generating annotation data...')
        print('#'*25)

        k = 0
        results = []

        for idx, image_id in enumerate(image_ids):
            for i, row in df[df['image_id'] == image_id].iterrows():
                results.append({
                    'id': k,
                    'image_id': idx,
                    'category_id': row['lesion_label'],
                    'bbox': np.array([
                        row['x_min'],
                        row['y_min'],
                        row['x_max'],
                        row['y_max'],
                    ]),
                    'segmentation': [],
                    'ignore': 0,
                    'area': (row['x_max'] - row['x_min']) * (row['y_max'] - row['y_min']),
                    'iscrowd': 0,
                })

                k += 1
        return results 

    def __decode_prediction_string(self, pred_str):
        data = list(map(float, pred_str.split(" ")))
        data = np.array(data)
        return data.reshape(-1,6)
        
    def __gen_predictions(self, df, image_ids):
        print(f'{Fore.GREEN}#'*25)
        print('Generating predictions data...')
        print('#'*25)

        k = 0
        results = []
        for i, row in df.iterrows():
            image_id = row['image_id']
            preds = self.__decode_prediction_string(row['PredictionString'])

            for j, pred in enumerate(preds):
                results.append({
                     'id': k,
                     'image_id': int(np.where(image_ids == image_id)[0]),
                     'category_id': int(pred[0]),
                     'bbox': np.array([
                         pred[2], pred[3], pred[4], pred[5],
                     ]),
                     'segmentation': [],
                     'ignore': 0,
                     'area': (pred[4] - pred[2]) * (pred[5] - pred[3]),
                     'iscrowd': 0,
                     'score': pred[1],  
                })
                k += 1
        return results

    def evaluate(self, pred_df):
        if pred_df is not None:
            self.predictions['annotations'] = self.__gen_predictions(pred_df, self.image_ids)

        coco_ds = COCO()
        coco_ds.dataset = self.annotations
        coco_ds.createIndex()
        coco_dt = COCO()
        coco_dt.dataset = self.predictions
        coco_dt.createIndex()

        imgIds = sorted(coco_ds.getImgIds())
            
        cat_ids = sorted(coco_ds.getCatIds(catNms=self.true_df['lesion'].unique()))
        cocoEval = COCOeval(coco_ds, coco_dt, 'bbox')
        cocoEval.params.maxDets = [1, 100, 100]
        cocoEval.params.imgIds = imgIds
        cocoEval.params.useCats = True
        cocoEval.params.iouType = 'bbox'
        cocoEval.params.iouThrs = np.linspace(0.5, 0.95, 10)
        cocoEval.params.catIds = cat_ids

        cocoEval.evaluate()
        cocoEval.accumulate()
        cocoEval.summarize()

        return cocoEval
