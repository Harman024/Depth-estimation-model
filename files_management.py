import csv
import numpy as np
import cv2


def get_projection_matrices():
    """Frame Calibration Holder
    3x4    p_left, p_right      Camera P matrix. Contains extrinsic and intrinsic parameters.
    """
#     p_left = np.array([[640.0,   0.0, 640.0, 2176.0], 
#                        [  0.0, 480.0, 480.0,  552.0], 
#                        [  0.0,   0.0,   1.0,    1.4]])
#     p_right = np.array([[640.0,   0.0, 640.0, 2176.0], 
#                        [   0.0, 480.0, 480.0,  792.0], 
#                        [   0.0,   0.0,   1.0,    1.4]])

    # 640 is half of 1280 - resolution of image - width 
    # 360 is half of 720 - resoltuion of image - height
    p_left = np.array([[640.0,   0.0, 640.0, 2176.0], 
                           [  0.0, 360.0, 360.0,  552.0], 
                           [  0.0,   0.0,   1.0,    1.4]])
    p_right = np.array([[640.0,   0.0, 640.0, 2176.0], 
                           [   0.0, 360.0, 360.0,  792.0], 
                           [   0.0,   0.0,   1.0,    1.4]])
    return p_left, p_right 


def read_left_image():
    return cv2.imread("Left_Right.jpg")[...,::-1]


def read_right_image():
    return cv2.imread("right.jpg")[...,::-1]


def get_obstacle_image():
    img_left_colour = read_left_image()
    return img_left_colour[300:700, 400:1000, :]
