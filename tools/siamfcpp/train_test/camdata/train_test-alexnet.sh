#!/usr/bin/env bash
python ./main/train.py --config 'experiments/siamfcpp/train/camdata/siamfcpp_alexnet-trn.yaml' --resume latest
python ./main/test.py --config 'experiments/siamfcpp/train/camdata/siamfcpp_alexnet-trn.yaml'
