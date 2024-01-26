
import os
import cv2

GST_STR = 'nvarguscamerasrc \
        ! video/x-raw(memory:NVMM), width=3280, height=2464, format=(string)NV12, framerate=(fraction)21/1 \
        ! nvvidconv ! video/x-raw, width=(int)1920, height=(int)1080, format=(string)BGRx \
        ! videoconvert \
        ! appsink'

dir_path = 'images'
base_path = 'images/pic'
ext = 'jpg'

def main():
    cap = cv2.VideoCapture(GST_STR, cv2.CAP_GSTREAMER)

    os.makedirs(dir_path, exist_ok=True)

    n = 0
    while True:
        ret, frame = cap.read()
        cv2.imwrite('{}_{}.{}'.format(base_path, n, ext), frame)
        n += 1

if __name__ == "__main__":
    main()