# -*- coding: utf-8 -*-

import argparse
import os
# from glob import glob
import cv2


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
    parser.add_argument('-r',
                        '--rt',
                        default='',
                        type=str,
                        help='result txt data')

    return parser


if __name__ == '__main__':
    # parsing
    parser = make_parser()
    parsed_args = parser.parse_args()

    x_list = [1, 4, 11, 15]
    p_idx = 1
    checking = True
    while checking:
        p = x_list[p_idx]
        gt_file = parsed_args.gt.replace('*', str(p))
        with open(gt_file) as f:
            gts = f.readlines()
        for i, gt in enumerate(gts):
            gts[i] = gt.strip().split(',')
        rt_file = parsed_args.rt.replace('*', str(p))
        with open(rt_file) as f:
            rts = f.readlines()
        for i, rt in enumerate(rts):
            rts[i] = rt.strip().split(',')
        imgdir = parsed_args.imgdir.replace('*', str(p))
        imgs = os.listdir(imgdir)
        
        assert len(imgs) == len(gts) == len(rts) and len(imgs) > 0
        print('checking', imgdir)

        i, check_gt = 0, False
        while True:
            img = cv2.imread(os.path.join(imgdir, imgs[i]))
            x, y, w, h = gts[i] if check_gt else rts[i]
            x, y, w, h = int(float(x)), int(float(y)), int(float(w)), int(float(h))
            # print(x, y, w, h)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0,0,255), 2)
            cv2.imshow('img', img)
            key = cv2.waitKey()
            if key == ord('q'):
                checking = False
                break
            elif key == ord('w') and i < len(imgs) - 1:
                i += 1
            elif key == ord('s') and i > 0:
                i -= 1
            elif key == ord('d') and p_idx < 3:
                p_idx += 1
                break
            elif key == ord('a') and p_idx > 0:
                p_idx -= 1
                break
            elif key == ord('g') and not check_gt:
                check_gt = True
                print('Checking GT')
            elif key == ord('r') and check_gt:
                check_gt = False
                print('Checking Result')


    

    
