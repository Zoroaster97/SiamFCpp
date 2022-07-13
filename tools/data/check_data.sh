#!/usr/bin/env bash
python ./videoanalyst/data/utils/check_data.py \
    --imgdir 'datasets/CamData/person/person-4/img' \
    --gt 'logs/GOT-Benchmark/result/CamData/s6k4-ep0/person-4.txt'
    # --gt 'logs/GOT-Benchmark/result/CamData/camdata-test5/person-4.txt'
    # --gt 'logs/GOT-Benchmark/result/CamData/baseline/person-4.txt'
    # --gt 'datasets/CamData/person/person-1/groundtruth.txt'
