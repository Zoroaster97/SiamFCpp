#!/usr/bin/env bash
python ./videoanalyst/data/utils/check_data.py \
    --imgdir 'datasets/CamData/person/person-2/img' \
    --gt 'logs/GOT-Benchmark/result/CamData/siamfcpp_alexnet-camdata4-k2/person-2.txt'
    # --gt 'datasets/CamData/person/person-1/groundtruth.txt'
