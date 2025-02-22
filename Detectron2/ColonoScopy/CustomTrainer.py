import yaml
import argparse
import json
import dataclasses
from dataclasses import dataclass, field
from typing import Dict
from distutils.util import strtobool
from pathlib import Path

import detectron2
from detectron2 import model_zoo # model library
from detectron2.config import get_cfg # Get a copy of the default config

## detectron dataset format 
from detectron2.data import DatasetCatalog # in catalog.py, # using strings in the config
from detectron2.data import MetadataCatalog
from detectron2.data.dataset_mapper import DatasetMapper
from detectron2.data import build_detection_train_loader, build_detection_test_loader


## Engine
from detectron2.engine import DefaultPredictor, DefaultTrainer # default
from detectron2.engine import launch # DDP

## Solver
from detectron2.solver import build_lr_scheduler, build_optimizer
from detectron2.solver.build import get_default_optimizer_params, maybe_add_gradient_clipping

## Evaluation
from detectron2.evaluation import COCOEvaluator # coco format
from detectron2.evaluation import PascalVOCDetectionEvaluator # pascal_voc format

## Utils
from detectron2.utils.logger import setup_logger # Initialize the detectron2 logger and set its verbosity level to "DEBUG"
from detectron2.utils.visualizer import Visualizer, ColorMode

setup_logger()

class MyTrainer(DefaultTrainer):
    @classmethod
    # It now calls :func: 'detectron2.data.build_detection_train_loader'
    def build_train_loader(cls, cfg, sampler=None):  
        augs = []
        augs.append(T.RandomRotation(angle=[-2.5,2.5]))
        augs.append(T.RandomApply(MixUpAug(cfg), prob=0))
        augs.append(T.RandomApply(MosaicAug(cfg), prob=0.25))
        min_size = cfg.INPUT.MIN_SIZE_TRAIN
        max_size = cfg.INPUT.MAX_SIZE_TRAIN
        sample_style = cfg.INPUT.MIN_SIZE_TRAIN_SAMPLING
        augs.append(T.ResizeShortestEdge(min_size, max_size, sample_style)) #
        return build_detection_train_loader(
            cfg, mapper=ExtendedDatasetMapper(cfg, True, augmentations=augs), sampler=sampler
            #cfg, mapper=AlbumentationsMapper(cfg, True, mixup_prob=0.05), sampler=sampler   
        )
        
    @classmethod
    def build_test_loader(cls, cfg, dataset_name):
        return build_detection_test_loader(
            cfg, dataset_name, mapper=DatasetMapper(cfg, False)
        )

    """Optimizer: SGD -> Adam"""
    @classmethod
    def build_optimizer(cls, cfg, model):
        params = get_default_optimizer_params(
        model,
        base_lr=cfg.SOLVER.BASE_LR,
        weight_decay_norm=cfg.SOLVER.WEIGHT_DECAY_NORM,
        bias_lr_factor=cfg.SOLVER.BIAS_LR_FACTOR,
        weight_decay_bias=cfg.SOLVER.WEIGHT_DECAY_BIAS,
        )
        return maybe_add_gradient_clipping(cfg, torch.optim.Adam)(
                             params,
                             lr = cfg.SOLVER.BASE_LR,
                             weight_decay = cfg.SOLVER.WEIGHT_DECAY,)
        
    @classmethod
    def build_evaluator(cls, cfg, dataset_name, output_folder=None):

        if output_folder is None:
            output_folder = os.path.join(cfg.OUTPUT_DIR, 'inference')

        return COCOEvaluator(dataset_name, ("bbox",), False, output_dir=output_folder)
