import cv2

CROP_SIZE = 100
capture = cv2.VideoCapture('C:\\Users\\Fabian\\Desktop\\miku.mp4')

while capture.isOpened():
    ret, frame = capture.read()
    h, w = frame.shape[:-1]

    h_mid, w_mid = h // 2, w // 2
    c = CROP_SIZE // 2

    cropped = frame[h_mid - c: h_mid + c, w_mid - c: w_mid + c]
    cv2.imshow('webcam', cropped)
    # cv2.imshow('webcam2', frame)
    cv2.waitKey(0)
