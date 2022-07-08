# -*- coding: utf-8 -*-

import argparse
import os
import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def make_parser():
    parser = argparse.ArgumentParser(description='Test')
    parser.add_argument('-rd',
                        '--report_dirs',
                        default='',
                        type=str,
                        help='report dirs')
    parser.add_argument('-s',
                        '--start',
                        default=0,
                        type=int,
                        help='start idx')
    parser.add_argument('-e',
                        '--end',
                        default=5,
                        type=int,
                        help='end idx')

    return parser


if __name__ == '__main__':
    # parsing
    parser = make_parser()
    parsed_args = parser.parse_args()

    all_success_score = []
    all_precision_score = []
    all_normalized_precision_score = []
    all_success_rate = []
    save_dir = os.path.dirname(parsed_args.report_dirs)
    for i in range(parsed_args.start, parsed_args.end):
        report_dir = parsed_args.report_dirs.replace('*', str(i))
        assert os.path.exists(report_dir), \
            'No reports found. Run "report" first' \
            'before plotting curves.'
        report_file = os.path.join(report_dir, 'performance.json')
        assert os.path.exists(report_file), \
            'No reports found. Run "report" first' \
            'before plotting curves.'

        # load pre-computed performance
        with open(report_file) as f:
            data = json.load(f)
            tracker_name = list(data.keys())[0]
            success_score = data[tracker_name]['overall']['success_score']
            precision_score = data[tracker_name]['overall']['precision_score']
            normalized_precision_score = data[tracker_name]['overall']['normalized_precision_score']
            success_rate = data[tracker_name]['overall']['success_rate']
            all_success_score.append(success_score)
            all_precision_score.append(precision_score)
            all_normalized_precision_score.append(normalized_precision_score)
            all_success_rate.append(success_rate)


    plt.xlabel("epoch")
    plt.ylabel("performance")
    plt.plot(all_success_score, label="success_score")
    plt.plot(all_precision_score, label="precision_score")
    plt.plot(all_normalized_precision_score, label="normalized_precision_score")
    plt.plot(all_success_rate, label="success_rate")
    plt.legend()
    plt.show()
    


    # succ_file = os.path.join(report_dir, 'success_plots' + '.png')
    # prec_file = os.path.join(report_dir, 'precision_plots' + '.png')
    # norm_prec_file = os.path.join(report_dir,
    #                                 'norm_precision_plots' + '.png')
    # key = 'overall'

    # # markers
    # markers = ['-', '--', '-.']
    # markers = [c + m for m in markers for c in [''] * 10]

    # # filter performance by tracker_names
    # performance = {
    #     k: v
    #     for k, v in performance.items() if k in tracker_names
    # }

    # # sort trackers by success score
    # tracker_names = list(performance.keys())
    # succ = [t[key]['success_score'] for t in performance.values()]
    # inds = np.argsort(succ)[::-1]
    # tracker_names = [tracker_names[i] for i in inds]

    # # plot success curves
    # thr_iou = np.linspace(0, 1, self.nbins_iou)
    # fig, ax = plt.subplots()
    # lines = []
    # legends = []
    # for i, name in enumerate(tracker_names):
    #     line, = ax.plot(thr_iou, performance[name][key]['success_curve'],
    #                     markers[i % len(markers)])
    #     lines.append(line)
    #     legends.append('%s: [%.3f]' %
    #                     (name, performance[name][key]['success_score']))
    # matplotlib.rcParams.update({'font.size': 7.4})
    # # legend = ax.legend(lines, legends, loc='center left', bbox_to_anchor=(1, 0.5))
    # legend = ax.legend(lines,
    #                     legends,
    #                     loc='lower left',
    #                     bbox_to_anchor=(0., 0.))

    # matplotlib.rcParams.update({'font.size': 9})
    # ax.set(xlabel='Overlap threshold',
    #         ylabel='Success rate',
    #         xlim=(0, 1),
    #         ylim=(0, 1),
    #         title='Success plots on CamData')
    # ax.grid(True)
    # fig.tight_layout()

    # # control ratio
    # # ax.set_aspect('equal', 'box')

    # print('Saving success plots to', succ_file)
    # fig.savefig(succ_file,
    #             bbox_extra_artists=(legend, ),
    #             bbox_inches='tight',
    #             dpi=300)

    # # sort trackers by precision score
    # tracker_names = list(performance.keys())
    # prec = [t[key]['precision_score'] for t in performance.values()]
    # inds = np.argsort(prec)[::-1]
    # tracker_names = [tracker_names[i] for i in inds]

    # # plot precision curves
    # thr_ce = np.arange(0, self.nbins_ce)
    # fig, ax = plt.subplots()
    # lines = []
    # legends = []
    # for i, name in enumerate(tracker_names):
    #     line, = ax.plot(thr_ce, performance[name][key]['precision_curve'],
    #                     markers[i % len(markers)])
    #     lines.append(line)
    #     legends.append('%s: [%.3f]' %
    #                     (name, performance[name][key]['precision_score']))
    # matplotlib.rcParams.update({'font.size': 7.4})
    # # legend = ax.legend(lines, legends, loc='center left', bbox_to_anchor=(1, 0.5))
    # legend = ax.legend(lines,
    #                     legends,
    #                     loc='lower right',
    #                     bbox_to_anchor=(1., 0.))

    # matplotlib.rcParams.update({'font.size': 9})
    # ax.set(xlabel='Location error threshold',
    #         ylabel='Precision',
    #         xlim=(0, thr_ce.max()),
    #         ylim=(0, 1),
    #         title='Precision plots on CamData')
    # ax.grid(True)
    # fig.tight_layout()

    # # control ratio
    # # ax.set_aspect('equal', 'box')

    # print('Saving precision plots to', prec_file)
    # fig.savefig(prec_file, dpi=300)

    # # added by user
    # # sort trackers by normalized precision score
    # tracker_names = list(performance.keys())
    # prec = [
    #     t[key]['normalized_precision_score'] for t in performance.values()
    # ]
    # inds = np.argsort(prec)[::-1]
    # tracker_names = [tracker_names[i] for i in inds]

    # # plot normalized precision curves
    # thr_nce = np.arange(0, self.nbins_nce)
    # fig, ax = plt.subplots()
    # lines = []
    # legends = []
    # for i, name in enumerate(tracker_names):
    #     line, = ax.plot(
    #         thr_nce, performance[name][key]['normalized_precision_curve'],
    #         markers[i % len(markers)])
    #     lines.append(line)
    #     legends.append(
    #         '%s: [%.3f]' %
    #         (name, performance[name][key]['normalized_precision_score']))
    # matplotlib.rcParams.update({'font.size': 7.4})
    # # legend = ax.legend(lines, legends, loc='center left', bbox_to_anchor=(1, 0.5))
    # legend = ax.legend(lines,
    #                     legends,
    #                     loc='lower right',
    #                     bbox_to_anchor=(1., 0.))

    # matplotlib.rcParams.update({'font.size': 9})
    # ax.set(xlabel='Normalized location error threshold',
    #         ylabel='Normalized precision',
    #         xlim=(0, thr_ce.max()),
    #         ylim=(0, 1),
    #         title='Normalized precision plots on CamData')
    # ax.grid(True)
    # fig.tight_layout()

    # # control ratio
    # # ax.set_aspect('equal', 'box')

    # print('Saving normalized precision plots to', norm_prec_file)
    # fig.savefig(norm_prec_file, dpi=300)
