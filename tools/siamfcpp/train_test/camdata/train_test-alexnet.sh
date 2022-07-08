#!/usr/bin/env bash
python ./main/train.py --config 'experiments/siamfcpp/train/camdata/siamfcpp_alexnet-trn.yaml'
python ./main/test.py --config 'experiments/siamfcpp/train/camdata/siamfcpp_alexnet-trn.yaml'
