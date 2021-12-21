import os.path
from glob import glob

import cv2
import numpy as np
import pathlib


def calibrate_chessboard(dir_path, image_format, square_size, width, height):
    '''Calibrate a camera using chessboard images.'''
    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    save_dir = os.path.join(os.path.split(dir_path)[0], "save")
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(8,6,0)
    objp = np.zeros((height*width, 3), np.float32)
    objp[:, :2] = np.mgrid[0:width, 0:height].T.reshape(-1, 2)

    objp = objp * square_size

    # Arrays to store object points and image points from all the images.
    objpoints = []  # 3d point in real world space
    imgpoints = []  # 2d points in image plane.

    # images = pathlib.Path(dir_path).glob(f'*.{image_format}')
    image_path = os.path.join(dir_path, "*{}".format(image_format))

    # Iterate through all images
    # for fname in images:
    for num, fname in enumerate(glob(image_path)):

        img = cv2.imread(str(fname))
        img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

        _, image_name = os.path.split(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(gray, (width, height), None)

        # If found, add object points, image points (after refining them)
        if ret:
            objpoints.append(objp)
            print("the image nums is {}, image name is {} \n".format(num, image_name))
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            cv2.drawChessboardCorners(img, (width, height), corners2, ret)
            # cv2.imshow('FoundCorners', img)
            cv2.imwrite(os.path.join(save_dir, image_name), img)
            # cv2.waitKey(0)
            imgpoints.append(corners2)


    # Calibrate camera
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    #相机内参数矩阵: mtx
    #畸变系数: dist
    # 图像的旋转向量,将将旋转向量转换为相对应的旋转矩阵 ，Rodrigues(rvecsMat[i],rotation_matrix);
    return [ret, mtx, dist, rvecs, tvecs]
