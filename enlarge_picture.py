import numpy
import numpy as np
import os
import cv2


eval_image_path = './diantou/diantou-images'
export_path = './diantou/yolov5-quant-images-diantou'

eval_image_path = r"E:\data\camera_calibration\test_on_line"
# image_dir = r"E:\data\tmp\check-pic1\check-pic1"
# image_dir = "E:\data\camera_calibration\images\images"
# image_dir = "E:\data\camera_calibration\chess"
# image_dir = "E:\data\camera_calibration\chess_photo"

# save_dir = os.path.join(os.path.split(image_dir)[0],"save_undist_check-pic1")
export_path = os.path.join(os.path.split(eval_image_path)[0],"test_on_line2")

if __name__ == "__main__":

    # import os
    #
    # from utils import load_coefficients
    # import cv2
    #
    # # Load coefficients
    # mtx, dist = load_coefficients('calibration_chessboard.yml')
    # # image_dir = r"E:\data\camera_calibration\test_on_line"
    # image_dir = r"E:\data\camera_calibration\test_on_line"
    # # image_dir = r"E:\data\tmp\check-pic1\check-pic1"
    # # image_dir = "E:\data\camera_calibration\images\images"
    # # image_dir = "E:\data\camera_calibration\chess"
    # # image_dir = "E:\data\camera_calibration\chess_photo"
    #
    # # save_dir = os.path.join(os.path.split(image_dir)[0],"save_undist_check-pic1")
    # save_dir = os.path.join(os.path.split(image_dir)[0], "save_undist_test_on_line2")
    # # save_dir = os.path.join(os.path.split(image_dir)[0],"save_undist")
    # try:
    #     os.mkdir(save_dir)
    # except OSError as error:
    #     print(error)
    # for image_name in os.listdir(image_dir):
    #     image_path = os.path.join(image_dir, image_name)
    #     original = cv2.imread(image_path)
    #     original = cv2.rotate(original, cv2.ROTATE_90_CLOCKWISE)
    #
    #     dst = cv2.undistort(original, mtx, dist, None, None)
    #     cv2.imwrite(os.path.join(save_dir, image_name), dst)

    if not os.path.exists(export_path):
        os.makedirs(export_path)
    for img in os.listdir(eval_image_path):
        image_path = os.path.join(eval_image_path, img)
        image = cv2.imread(image_path)
        # iw, ih    = image.shape[:2]*0.9
        h,  w, _  = image.shape
        iw, ih = w,h
        scale = 0.9#min(iw/w, ih/h)
        nw, nh  = int(scale * w), int(scale * h)
        image_resized = cv2.resize(image, (nw, nh))
        image_paded = np.full(shape=[ih, iw, 3], fill_value=255, dtype = np.uint8)
        dw, dh = (iw - nw) // 2, (ih-nh) // 2
        image_paded[dh:nh+dh, dw:nw+dw, :] = image_resized
        image = image_paded

        image = image.astype(numpy.uint8)
        save_path = os.path.join(export_path, img.rstrip(".jpg") + ".png")
        cv2.imwrite(save_path, image)

        # Image.Image.save(image, fp=save_path)