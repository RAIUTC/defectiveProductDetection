## 영상 데이터 프레임별로 이미지 데이터 생성
## 영상 데이터를 프레임별로 이미지 데이터로 변환하는 코드

import cv2
import os

# 영상 데이터 경로
video_path = 'C:/Users/82109/Desktop/2020-2/캡스톤/영상데이터/캡스��
# 프레임 이미지 데이터 저장 경로
image_path = 'C:/Users/82109/Desktop/2020-2/캡스톤/영상�
# 프레임 이미지 데이터 저장 경로가 없으면 생성
if not os.path.exists(image_path):
    os.makedirs(image_path)

# 영상 데이터 불러오기
cap = cv2.VideoCapture(video_path)

# 프레임 수 확인
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('frame_count:', frame_count)

# 프레임별 이미지 데이터로 저장
for i in range(frame_count):
    ret, frame = cap.read()
    cv2.imwrite(image_path + 'image_' + str(i) + '.jpg', frame)

# 영상 데이터 해제
cap.release()

# 영상 데이터 경로
video_path = 'C:/Users/82109/Desktop/2020-2/캡스톤/영상데이터/캡스��
# 프레임 이미지 데이터 저장 경로
image_path = 'C:/Users/82109/Desktop/2020-2/캡스톤/영상�
# 프레임 이미지 데이터 저장 경로가 없으면 생성
if not os.path.exists(image_path):
    os.makedirs(image_path)