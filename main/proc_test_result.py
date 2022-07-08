# -*- coding: utf-8 -*-

import argparse
import os
import json
import matplotlib.pyplot as plt


def make_parser():
    parser = argparse.ArgumentParser(description='Test')
    parser.add_argument('-j',
                        '--json',
                        default='',
                        type=str,
                        help='experiment configuration')

    return parser


if __name__ == '__main__':
    # parsing
    parser = make_parser()
    parsed_args = parser.parse_args()

    all_success_score = []
    all_precision_score = []
    all_normalized_precision_score = []
    all_success_rate = []
    all_speed_fps = []
    json_file = parsed_args.json
    txt_file = os.path.join(os.path.dirname(json_file), 'performance_each_sample.txt')
   
    with open(json_file,'r') as jf:
        data = json.load(jf)
        assert len(data.keys()) == 1
        exp_name = list(data.keys())[0]
        for i in range(1, 21):
            success_score = data[exp_name]['seq_wise']['person-{}'.format(i)]['success_score']
            precision_score = data[exp_name]['seq_wise']['person-{}'.format(i)]['precision_score']
            normalized_precision_score = data[exp_name]['seq_wise']['person-{}'.format(i)]['normalized_precision_score']
            success_rate = data[exp_name]['seq_wise']['person-{}'.format(i)]['success_rate']
            speed_fps = data[exp_name]['seq_wise']['person-{}'.format(i)]['speed_fps']
            all_success_score.append(success_score)
            all_precision_score.append(precision_score)
            all_normalized_precision_score.append(normalized_precision_score)
            all_success_rate.append(success_rate)
            all_speed_fps.append(speed_fps)
    
    with open(txt_file, 'w') as f:
        for i in range(20):
            f.writelines('########\nperson-{}\n'.format(i + 1)
                        +'success_score: ' + str(all_success_score[i]) + '\n'
                        +'precision_score: '+str(all_precision_score[i]) + '\n'
                        +'normalized_precision_score: '+str(all_normalized_precision_score[i])+'\n'
                        +'success_rate: '+str(all_success_rate[i])+'\n'
                        +'speed_fps: '+str(all_speed_fps[i])+'\n')

