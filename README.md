# ComputerVision



<br>



## pose_estimation_and_AR.py
<details>
<summary>카메라로 촬영한 체스판을 calibration 후 체스판 위에 도형을 그리는 간단한 AR 프로그램입니다.</summary>
<br>
프로그램을 실행하면 체스판 동영상이 재생됩니다.
    
<strong>스페이스바</strong>를 누르면 영상이 정지되며 탐지된 교차점들을 표시하고, 정지 상태에서 <strong>엔터</strong>를 누르면 정지된 이미지를 저장하며 영상이 다시 재생됩니다. <strong>esc</strong>를 누르면 동영상 창이 닫히며 저장된 이미지를 바탕으로 calibration을 시작합니다. (esc를 누르지 않아도ㅡ약 28초 가량의ㅡ영상이 종료되면 calibration을 시작합니다.)

*저장된 이미지가 많지 않을 경우 calibration의 결과가 부정확할 수 있으며, 저장된 이미지가 아예 없을 경우 calibration을 수행하지 않습니다.*

calibration이 끝나면 terminal에 calibration 결과가 아래와 같이 출력됩니다.

![image](https://github.com/user-attachments/assets/c42e3445-7d61-4eb9-ba59-2bb549a04d9b)

결과를 출력한 뒤엔 이를 기반으로 체스판 특정 위치에 실시간으로 도형을 그려넣는 영상이 새 창에서 재생됩니다.

https://github.com/user-attachments/assets/09abdfac-715f-4da6-b928-bd5639523fbc

*그려넣은 도형은 게임 젤다의 전설에 등장하는 '트라이포스' 문양입니다.*

마찬가지로 <strong>스페이스바</strong>를 눌러 영상을 정지할 수 있으며, <strong>esc</strong>를 누르면 창이 닫히며 프로그램이 종료됩니다.

</details>



<br>



## camera_calibration_chessboard.py
<details>
<summary>카메라로 촬영한 체스판을 calibration 후 렌즈 왜곡을 보정하는 프로그램입니다.</summary>
<br>
프로그램을 실행하면 체스판 동영상이 재생됩니다.
    
<strong>스페이스바</strong>를 누르면 영상이 정지되며 탐지된 교차점들을 표시하고, 정지 상태에서 <strong>엔터</strong>를 누르면 정지된 이미지를 저장하며 영상이 다시 재생됩니다. <strong>esc</strong>를 누르면 동영상 창이 닫히며 저장된 이미지를 바탕으로 calibration을 시작합니다. (esc를 누르지 않아도ㅡ약 28초 가량의ㅡ영상이 종료되면 calibration을 시작합니다.)

*저장된 이미지가 많지 않을 경우 calibration의 결과가 부정확할 수 있으며, 저장된 이미지가 아예 없을 경우 calibration을 수행하지 않습니다.*

calibration이 끝나면 terminal에 calibration 결과가 아래와 같이 출력됩니다.
![image](https://github.com/user-attachments/assets/c42e3445-7d61-4eb9-ba59-2bb549a04d9b)

    *참고 설명*
    위 calibration의 결과는
    
    f_x=460.18198331
    f_y=459.02899464
    c_x=360.47390579
    c_y=357.2166374

    k_1=-0.0440973
    k_2=0.10024221
    k_3=-0.07440193
    p_1=0.00049893
    p_2=-0.00120213

    RMSE=0.8585390497240185

    를 뜻함

결과를 출력한 뒤엔 이를 기반으로 렌즈 왜곡을 보정한 영상이 새 창에서 재생됩니다.

*원본 영상의 왜곡 정도가 심하지 않아 보정 영상과 거의 차이가 없습니다.*

![image](https://github.com/user-attachments/assets/0b73d6f3-aef5-4b67-82a1-df3f3ab9b615)



마찬가지로 <strong>스페이스바</strong>를 눌러 영상을 정지할 수 있으며, <strong>tab</strong>을 눌러 원본 영상과 왜곡 보정 영상을 번갈아가며 볼 수 있습니다. <strong>esc</strong>를 누르면 창이 닫히며 프로그램이 종료됩니다.

</details>



<br>



## simple_cartoon_converter.py
<details>
<summary>이미지를 만화풍으로 바꾸는 프로그램입니다.(*이해도가 낮고 시간이 없어 gpt 코드를 거의 그대로 가져왔습니다.)</summary>
<br>
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



<br>



## simple_video_recorder.py
<details>
<summary>천안시 고속철 입구 CCTV 영상을 불러와 녹화할 수 있는 프로그램입니다.</summary>
<br>
<strong>스페이스바</strong>를 누르면 좌측 상단에 붉은 원이 생기며 녹화를 시작합니다. 스페이스바를 다시 누르면 녹화가 종료되며 동영상 파일이 mp4 확장자로 저장됩니다.

<strong>'<'</strong> 키를 입력할 때마다 밝기가 조금씩 올라갑니다. <strong>'>'</strong> 키를 입력하면 밝기가 조금씩 내려갑니다. 조정된 밝기는 녹화 영상에도 적용되나, 녹화 도중엔 밝기를 조절할 수 없습니다.

<strong>ESC</strong> 키를 누르면 프로그램이 종료됩니다.

기본 상태:
https://github.com/user-attachments/assets/6e9ca832-7e9a-4251-aa74-cbb8ad4b6aca

녹화 시작 및 종료:
https://github.com/user-attachments/assets/19fc35ee-10ac-4ecd-951a-8e99ccbba277

밝기 조절:
https://github.com/user-attachments/assets/db958ad2-bf1e-4610-8536-f37dc1ea3def
</details>
