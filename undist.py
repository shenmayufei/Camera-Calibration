import os
import cv2
import argparse
from utils import load_coefficients

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('--image_dir', type=str,
                        default=r'E:\data\camera_calibration\test_on_line2',
                        help='the input image dir')

    parser.add_argument('--parameter_file', type=str,
                        default=r'calibration_chessboard.yml',
                        help='distort parameter file')
    args = parser.parse_args()
    # Load coefficients
    mtx, dist = load_coefficients(args.parameter_file)
    dir_path, dir_name = os.path.split(args.image_dir)
    save_dir = os.path.join(dir_path, dir_name + '_undist')
    try:
        print("mkdir {}".format(save_dir))
        os.mkdir(save_dir)
    except OSError as error:
        print(error)
    for image_name in os.listdir(args.image_dir):
        image_path = os.path.join(args.image_dir, image_name)
        original = cv2.imread(image_path)
        original = cv2.rotate(original,cv2.ROTATE_90_CLOCKWISE)

        dst = cv2.undistort(original, mtx, dist, None, None)
        cv2.imwrite(os.path.join(save_dir,image_name), dst)
    print("finish undist \n")