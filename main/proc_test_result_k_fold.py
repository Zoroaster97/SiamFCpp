# -*- coding: utf-8 -*-

import argparse
import os
import json


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
    json_file = parsed_args.json
    txt_file = os.path.join(os.path.dirname(json_file.replace('k*', '')), 'performance.txt')

    x_set = [1, 4, 11, 15]
    x_success_score, y_success_score = [], []
    x_precision_score, y_precision_score = [], []
    x_normalized_precision_score, y_normalized_precision_score = [], []
    x_success_rate, y_success_rate = [], []
   
    
    for i in range(1, 21):
        with open(json_file.replace('*', str(i)),'r') as jf:
            data = json.load(jf)
            assert len(data.keys()) == 1
            exp_name = list(data.keys())[0]
        success_score = data[exp_name]['seq_wise']['person-{}'.format(i)]['success_score']
        precision_score = data[exp_name]['seq_wise']['person-{}'.format(i)]['precision_score']
        normalized_precision_score = data[exp_name]['seq_wise']['person-{}'.format(i)]['normalized_precision_score']
        success_rate = data[exp_name]['seq_wise']['person-{}'.format(i)]['success_rate']
        # speed_fps = data[exp_name]['seq_wise']['person-{}'.format(i)]['speed_fps']
        all_success_score.append(success_score)
        all_precision_score.append(precision_score)
        all_normalized_precision_score.append(normalized_precision_score)
        all_success_rate.append(success_rate)
        if i in x_set:
            x_success_score.append(success_score)
            x_precision_score.append(precision_score)
            x_normalized_precision_score.append(normalized_precision_score)
            x_success_rate.append(success_rate)
        else:
            y_success_score.append(success_score)
            y_precision_score.append(precision_score)
            y_normalized_precision_score.append(normalized_precision_score)
            y_success_rate.append(success_rate)
    
    with open(txt_file, 'w') as f:
        f.writelines('########\noverall\n'
                    + 'success_score: ' + str(sum(all_success_score) / 20) + '\n'
                    + 'precision_score: ' + str(sum(all_precision_score) / 20) + '\n'
                    + 'normalized_precision_score: ' + str(sum(all_normalized_precision_score) / 20) + '\n'
                    + 'success_rate: ' + str(sum(all_success_rate) / 20) + '\n')
        f.writelines('########\nperson-x\n'
                    + 'success_score: ' + str(sum(x_success_score) / 4) + '\n'
                    + 'precision_score: ' + str(sum(x_precision_score) / 4) + '\n'
                    + 'normalized_precision_score: ' + str(sum(x_normalized_precision_score) / 4) + '\n'
                    + 'success_rate: ' + str(sum(x_success_rate) / 4) + '\n')
        f.writelines('########\nperson-y\n'
                    + 'success_score: ' + str(sum(y_success_score) / 16) + '\n'
                    + 'precision_score: ' + str(sum(y_precision_score) / 16) + '\n'
                    + 'normalized_precision_score: ' + str(sum(y_normalized_precision_score) / 16) + '\n'
                    + 'success_rate: ' + str(sum(y_success_rate) / 16) + '\n')
        for i in range(20):
            f.writelines('########\nperson-{}\n'.format(i + 1)
                        + 'success_score: ' + str(all_success_score[i]) + '\n'
                        + 'precision_score: ' + str(all_precision_score[i]) + '\n'
                        + 'normalized_precision_score: ' + str(all_normalized_precision_score[i]) + '\n'
                        + 'success_rate: ' + str(all_success_rate[i]) + '\n')

