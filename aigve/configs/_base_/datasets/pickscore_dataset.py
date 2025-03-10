# Copyright (c) IFM Lab. All rights reserved.

from mmengine.dataset.sampler import DefaultSampler
from datasets import PickScoreDataset


val_dataloader = dict(
    batch_size=4,
    num_workers=2,
    persistent_workers=True,
    drop_last=False,
    sampler=dict(type=DefaultSampler, shuffle=False),
    dataset=dict(
        type=PickScoreDataset,
        processor_name='Salesforce/blip-image-captioning-base',
        video_dir='/home/exouser/VQA_tool/VQA_Toolkit/data/toy/evaluate/',
        prompt_dir='/home/exouser/VQA_tool/VQA_Toolkit/data/toy/annotations/evaluate.json',
    )
)
