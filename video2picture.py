import cv2

videoCapture = cv2.VideoCapture()
videoCapture.open(r'E:\data\camera_calibration\video\21-06-04-12-56-22-306_video')


if videoCapture.isOpened():
    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
    #fps是帧率，意思是每一秒刷新图片的数量，frames是一整段视频中总的图片数量。
    print("fps=", fps, "frames=", frames)

    for i in range(int(frames)):
        ret,frame = videoCapture.read()
        cv2.imwrite(r"E:\data\camera_calibration\pic\21-06-04-12-56-22-306_video(%d).jpg"%i,frame)
