#!/usr/bin/env bash
python ./main/train_k_fold.py --config 'experiments/siamfcpp/train/camdata/siamfcpp_alexnet-trn-k-fold.yaml' -s 1 -e 20
