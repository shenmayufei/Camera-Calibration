import os

from utils import load_coefficients
import cv2

# Load coefficients
mtx, dist = load_coefficients('calibration_chessboard.yml')
# image_dir = r"E:\data\camera_calibration\test_on_line"
image_dir = r"E:\data\camera_calibration\test_on_line2"
# image_dir = r"E:\data\tmp\check-pic1\check-pic1"
# image_dir = "E:\data\camera_calibration\images\images"
# image_dir = "E:\data\camera_calibration\chess"
# image_dir = "E:\data\camera_calibration\chess_photo"

# save_dir = os.path.join(os.path.split(image_dir)[0],"save_undist_check-pic1")
save_dir = os.path.join(os.path.split(image_dir)[0],"save_undist_test_on_line3")
# save_dir = os.path.join(os.path.split(image_dir)[0],"save_undist")
try:
    os.mkdir(save_dir)
except OSError as error:
    print(error)
for image_name in os.listdir(image_dir):
    image_path = os.path.join(image_dir, image_name)
    original = cv2.imread(image_path)
    original = cv2.rotate(original,cv2.ROTATE_90_CLOCKWISE)

    dst = cv2.undistort(original, mtx, dist, None, None)
    cv2.imwrite(os.path.join(save_dir,image_name), dst)
