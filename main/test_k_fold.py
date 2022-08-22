# -*- coding: utf-8 -*-

import argparse
import os.path as osp

from loguru import logger

import torch, copy

from videoanalyst.config.config import cfg as root_cfg
from videoanalyst.config.config import specify_task
from videoanalyst.engine.builder import build as tester_builder
from videoanalyst.model import builder as model_builder
from videoanalyst.pipeline import builder as pipeline_builder


def make_parser():
    parser = argparse.ArgumentParser(description='Test')
    parser.add_argument('-cfg',
                        '--config',
                        default='',
                        type=str,
                        help='experiment configuration')
    parser.add_argument('-s',
                        '--start',
                        default=0,
                        type=int,
                        help='start idx')
    parser.add_argument('-e',
                        '--end',
                        default=20,
                        type=int,
                        help='end idx')

    return parser


def build_siamfcpp_tester(task_cfg):
    # build model
    model = model_builder.build("track", task_cfg.model)
    # build pipeline
    pipeline = pipeline_builder.build("track", task_cfg.pipeline, model)
    # build tester
    testers = tester_builder("track", task_cfg.tester, "tester", pipeline)
    return testers


def build_sat_tester(task_cfg):
    # build model
    tracker_model = model_builder.build("track", task_cfg.tracker_model)
    tracker = pipeline_builder.build("track",
                                     task_cfg.tracker_pipeline,
                                     model=tracker_model)
    segmenter = model_builder.build('vos', task_cfg.segmenter)
    # build pipeline
    pipeline = pipeline_builder.build('vos',
                                      task_cfg.pipeline,
                                      segmenter=segmenter,
                                      tracker=tracker)
    # build tester
    testers = tester_builder('vos', task_cfg.tester, "tester", pipeline)
    return testers


if __name__ == '__main__':
    # parsing
    parser = make_parser()
    parsed_args = parser.parse_args()

    # experiment config
    exp_cfg_path = osp.realpath(parsed_args.config)
    root_cfg.merge_from_file(exp_cfg_path)
    logger.info("Load experiment configuration at: %s" % exp_cfg_path)

    # resolve config
    root_cfg = root_cfg.test
    task, task_cfg = specify_task(root_cfg)
    # task_cfg.freeze()
    # for i in range(parsed_args.start, parsed_args.end + 1):
    for i in [15]:
    # for i in [1, 11, 15]:    # kx
    # for i in [2, 3, 5, 6]:    # ky
    # for i in [7, 8, 9, 10, 12, 13, 14, 16, 17, 18, 19, 20]:    # ky
        task_cfg_i = copy.deepcopy(task_cfg)
        exp_name = task_cfg_i.exp_name
        pretrain_model_path = task_cfg_i.model.task_model.SiamTrack.pretrain_model_path
        task_cfg_i.exp_name = exp_name.replace('*', str(i))
        task_cfg_i.tester.CamDataTester.exp_name = task_cfg_i.exp_name
        task_cfg_i.model.task_model.SiamTrack.pretrain_model_path = pretrain_model_path.replace('*', str(i))
        task_cfg_i.freeze()

        torch.multiprocessing.set_start_method('spawn', force=True)

        if task == 'track':
            testers = build_siamfcpp_tester(task_cfg_i)
        elif task == 'vos':
            testers = build_sat_tester(task_cfg_i)
        for tester in testers:
            tester.test(k_idx=i)
