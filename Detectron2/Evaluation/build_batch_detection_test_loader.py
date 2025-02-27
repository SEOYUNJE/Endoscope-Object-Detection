@classmethod
def build_test_loader(cls, cfg, dataset_name):
    return build_detection_test_loader(
          cfg, dataset_name, mapper=AlbumentationsMapper(is_train = False),
          batch_size = 4,
          num_workers = 2
        )
