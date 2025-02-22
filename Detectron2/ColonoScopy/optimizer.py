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
