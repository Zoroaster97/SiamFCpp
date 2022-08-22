#!/usr/bin/env bash
python ./videoanalyst/data/utils/check_data.py \
    --imgdir 'H:\workspace\luotongan\SavedCamData\test\img' \
    --gt 'H:\workspace\luotongan\SavedCamData\test\save_box.txt'
    # --gt 'logs/GOT-Benchmark/result/CamData/s6k6/person-6.txt'
    # --gt 'logs/GOT-Benchmark/result/CamData/s6k4-ep0/person-4.txt'
    # --gt 'logs/GOT-Benchmark/result/CamData/camdata-test5/person-4.txt'
    # --gt 'logs/GOT-Benchmark/result/CamData/baseline/person-4.txt'
    # --gt 'datasets/CamData/person/person-1/groundtruth.txt'
