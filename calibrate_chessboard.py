from chessboard import calibrate_chessboard
from utils import load_coefficients, save_coefficients

# Parameters
# IMAGES_DIR = 'E:\data\camera_calibration\images\images'  #for test
IMAGES_DIR = 'E:\data\camera_calibration\chess_photo'  # for xiaoxun camera
# IMAGES_DIR = 'E:\data\camera_calibration\chess_all'  # for xiaoxun camera
IMAGES_FORMAT = '.jpg'
SQUARE_SIZE = 2.5  #square_size: size, in centimeter, of each square of the real chessboard. Use a ruler and try to be as accurate as possible.
# SQUARE_SIZE = 1.6  #square_size: size, in centimeter, of each square of the real chessboard. Use a ruler and try to be as accurate as possible.
WIDTH = 6
HEIGHT = 9

# Calibrate 
ret, mtx, dist, rvecs, tvecs = calibrate_chessboard(
    IMAGES_DIR,
    IMAGES_FORMAT, 
    SQUARE_SIZE, 
    WIDTH, 
    HEIGHT
)
# Save coefficients into a file
save_coefficients(mtx, dist, "calibration_chessboard.yml")