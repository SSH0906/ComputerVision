# ComputerVision

## simple_cartoon_converter.py
<details>
<summary>discription</summary>
이미지를 만화풍으로 바꾸는 프로그램입니다. (*이해도가 낮고 시간이 없어 gpt 코드를 거의 그대로 가져왔습니다.)

gpt로 만든 코드에서 아래와 같이 medianBlur 인자값(커널 크기)을 5에서 3으로 변경하여 기존 코드보다 뭉개지는 정도를 줄였습니다.

    gray = cv2.medianBlur(gray, 3)

또한, Cartoon창 외에 Original창을 띄워 원본 이미지와 비교할 수 있도록 아래 코드를 추가했습니다.

    cv2.imshow("Original", img)

본 알고리즘은 MilesMorales2.jpg 이미지는 큰 이질감 없이 만화풍으로 잘 전환 됩니다.
![MilesMorales2_toCartoon](https://github.com/user-attachments/assets/01d5c766-6ec3-4d80-a8d3-1513ff85f58e)

하지만 MilesMorales1.jpg 이미지와 같이 신체의 외곽(손, 다리 등)이 다른 그림과 겹쳐지는 경우 외곽선을 제대로 형성하지 못해 선명해야할 부분이 뭉개지는 문제가 있습니다.
![MilesMorales1_toCartoon](https://github.com/user-attachments/assets/d44a1fa4-6487-4ac0-adfe-ab1da13e1cbe)
![MilesMorales1_toCartoon_Prob](https://github.com/user-attachments/assets/4b51054c-4175-470b-b220-280ff575c46f)


그림 자체의 외곽 부분은 잘 인지하여 테두리를 두껍게 해주지만 내부의 선까진 두껍게 해주지 못해 손, 발이 접히거나 다른 신체와 겹칠 경우 해당 부분은 만화풍으로 제대로 전환하지 못한다는 한계점이 존재합니다.
</details>
***

### simple_video_recorder.py
천안시 고속철 입구 CCTV 영상을 불러와 녹화할 수 있는 프로그램입니다.

스페이스바를 누르면 좌측 상단에 붉은 원이 생기며 녹화를 시작합니다. 스페이스바를 다시 누르면 녹화가 종료되며 동영상 파일이 mp4 확장자로 저장됩니다.

'<' 키를 입력할 때마다 밝기가 조금씩 올라갑니다. '>' 키를 입력하면 밝기가 조금씩 내려갑니다. 조정된 밝기는 녹화 영상에도 적용되나, 녹화 도중엔 밝기를 조절할 수 없습니다.

ESC 키를 누르면 프로그램이 종료됩니다.

기본 상태:
https://github.com/user-attachments/assets/6e9ca832-7e9a-4251-aa74-cbb8ad4b6aca

녹화 시작 및 종료:
https://github.com/user-attachments/assets/19fc35ee-10ac-4ecd-951a-8e99ccbba277

밝기 조절:
https://github.com/user-attachments/assets/db958ad2-bf1e-4610-8536-f37dc1ea3def

