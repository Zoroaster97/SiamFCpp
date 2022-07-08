# -*- coding: utf-8 -*-

import argparse
import os
import json
import cv2
# from videoanalyst.evaluation.got_benchmark.datasets import CamData


def make_parser():
    parser = argparse.ArgumentParser(description='Test')
    parser.add_argument('-i',
                        '--imgdir',
                        default='',
                        type=str,
                        help='image data dir')
    parser.add_argument('-g',
                        '--gt',
                        default='',
                        type=str,
                        help='ground-truth txt data')

    return parser


if __name__ == '__main__':
    # parsing
    parser = make_parser()
    parsed_args = parser.parse_args()
    with open(parsed_args.gt) as f:
        gts = f.readlines()
    for i, gt in enumerate(gts):
        gts[i] = gt.strip().split(',')
    imgs = os.listdir(parsed_args.imgdir)
    
    assert len(imgs) == len(gts)

    i = 0
    while True:
        img = cv2.imread(os.path.join(parsed_args.imgdir, imgs[i]))
        x, y, w, h = gts[i]
        x, y, w, h = int(float(x)), int(float(y)), int(float(w)), int(float(h))
        # print(x, y, w, h)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0,0,255), 2)
        cv2.imshow('img', img)
        key = cv2.waitKey()
        if key == ord('q'):
            break
        elif key == ord('w') and i < len(imgs) - 1:
            i += 1
        elif key == ord('s') and i > 0:
            i -= 1


    

    
