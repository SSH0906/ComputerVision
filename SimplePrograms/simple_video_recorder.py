import cv2 as cv
import numpy as np

# 천안시 교통정보 CCTV - 고속철 입구
video = cv.VideoCapture('http://210.99.70.120:1935/live/cctv023.stream/playlist.m3u8')

# 밝기 조절 변수
brightness = 1.0

while video.isOpened():
    valid, img = video.read()
    if not valid:
        break
    
    # 밝기 조정 적용
    img = cv.convertScaleAbs(img, alpha=brightness, beta=0)
    
    cv.imshow('video', img)
    
    key = cv.waitKey(1)
    if key == ord(' '):
        # 녹화 시작
        target = cv.VideoWriter()
        target_format = 'mp4'
        target_fourcc = 'XVID'
        target_file = 'RecordedVideo' + '.' + target_format
        h, w, *_ = img.shape
        target.open(target_file, cv.VideoWriter_fourcc(*target_fourcc), 30, (w, h))

        while video.isOpened():
            valid, img = video.read()
            if not valid:
                break

            # 밝기 조정 적용
            img = cv.convertScaleAbs(img, alpha=brightness, beta=0)
            target.write(img)

            # 녹화중 표시(붉은 원)
            center = (25, 25)
            cv.circle(img, center, radius=10, color=(0,0,255), thickness=-1)
            cv.imshow('video', img)

            # 녹화 종료
            if cv.waitKey(1) == ord(' '):
                target.release()
                break

    # 밝기 증가 (최대 3.0)
    elif key == ord('<'):
        brightness = min(brightness + 0.1, 3.0)

    # 밝기 감소 (최소 0.1)
    elif key == ord('>'):
        brightness = max(brightness - 0.1, 0.1)
    
    elif key == 27:
        break

video.release()
cv.destroyAllWindows()
