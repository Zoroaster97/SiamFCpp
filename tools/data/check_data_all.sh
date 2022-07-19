#!/usr/bin/env bash
python ./videoanalyst/data/utils/check_data_all.py \
    --imgdir 'datasets/CamData/person/person-*/img' \
    --gt 'datasets/CamData/person/person-*/groundtruth.txt' \
    --rt 'logs/GOT-Benchmark/result/CamData/s7k*/person-*.txt'
    # --rt 'logs/GOT-Benchmark/result/CamData/camdata-test2-k1-ep0/person-*.txt'
    # --rt 'logs/GOT-Benchmark/result/CamData/siamfcpp_alexnet/person-*.txt'
