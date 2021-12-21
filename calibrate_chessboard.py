# coding=utf-8
import argparse
from chessboard import calibrate_chessboard
from utils import save_coefficients

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('--image_dir',
                        default=r'E:\data\camera_calibration\chess_photo',
                        help='the input image dir')
    parser.add_argument("--col_nums", type=int, default=9,
                        help="the ")
    parser.add_argument("--row_nums", type=int, default=6,
                        help="check the picture is problem")
    parser.add_argument("--square_size", type=float, default=2.5,
                        help="square_size in centimeter")
    parser.add_argument('--image_format', type=str, default='.jpg',
                        help='image format ,default is .jpg')
    args = parser.parse_args()

    # Calibrate
    ret, mtx, dist, rvecs, tvecs = calibrate_chessboard(
        args.image_dir,
        args.image_format,
        args.square_size,
        args.col_nums,
        args.row_nums
    )
    # Save coefficients into a file
    save_coefficients(mtx, dist, "calibration_chessboard.yml")
    print("finish the calibration \n")