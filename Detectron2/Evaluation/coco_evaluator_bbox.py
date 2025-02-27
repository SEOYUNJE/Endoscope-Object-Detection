from detectron2.evaluation import COCOEvaluator, inference_on_dataset
from detectron2.data import build_detection_test_loader
from detectron2.checkpoint import DetectionCheckpointer
from detectron2.modeling import build_model

cfg = get_cfg()
cfg.MODEL.WEIGHTS = '/path/my_model/weights

## CocoEvaluator with Box 
evaluator = COCOEvaluator("gastroscopy_test", ("bbox",), False, output_dir=os.path.join(cfg.OUTPUT_DIR, 'inference'))

## TorchLoader
test_loader = build_detection_test_loader(cfg, "gastroscopy_test")

## Build and Load Model
model = build_model(cfg)
DetectionCheckpointer(model, save_dir=cfg.OUTPUT_DIR).resume_or_load(
            cfg.MODEL.WEIGHTS, resume=False
        )
model.eval()

## Evaluate Metrics
print(inference_on_dataset(model, test_loader, evaluator))
