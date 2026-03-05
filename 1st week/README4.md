## 2-3. 선택 범위만큼 새로운 이미지 생성

- 1. OpenCV 라이브러리를 불러온다.
- 2. cv.imread()를 사용하여 이미지를 읽어온다.
- 3. 이미지가 존재하지 않을 경우 프로그램을 종료한다.
- 4. 마우스를 클릭하고 있는 동안, 처음 클릭한 지점에서 드래그를 하면 직사각형을 생성한다.
- 5. 마우스 버튼을 놓으면, 그 위치를 저장, 직사각형 만큼의 범위를 따로 저장한다.
- 6. 따로 저장된 직사각형 범위를 새로운 이미지로 저장하여 출력한다.

###

## 코드(python)

```python
import cv2 as cv
import sys

img = cv.imread('soccer.jpg')

if img is None :
    sys.exit('파일이 존재하지 않습니다.')

drawing_red = False
drawing_blue = False
brush_size = 5

def draw(event, x, y, flags, param):

    global drawing_red, drawing_blue # 전역 변수로 선언하여 함수 내에서 사용할 수 있도록 함

    if event == cv.EVENT_LBUTTONDOWN: #왼쪽 버튼을 누르면
        drawing_red = True

    elif event == cv.EVENT_RBUTTONDOWN: #오른쪽 버튼을 누르면
        drawing_blue = True

    elif event == cv.EVENT_MOUSEMOVE: # 마우스가 움직이는 동안
        if drawing_red:
            cv.circle(img,(x,y),brush_size,(0,0,255),-1) # 빨간 점
        elif drawing_blue:
            cv.circle(img,(x,y),brush_size,(255,0,0),-1) # 파란 점

    elif event == cv.EVENT_LBUTTONUP: #왼쪽 버튼에서 손을 떼면
        drawing_red = False

    elif event == cv.EVENT_RBUTTONUP: #오른쪽 버튼에서 손을 떼면
        drawing_blue = False

    cv.imshow('Drawing', img)

cv.namedWindow('Drawing')
cv.imshow('Drawing',img)

cv.setMouseCallback('Drawing',draw)

while(True): #무한 루프를 돌면서 키 입력을 기다림
    if cv.waitKey(1)==ord('q'): #'q' 키를 누르면 루프를 종료
        break

cv.destroyAllWindows()

#저장 (지금 올린 코드 방식과 동일)
cv.imwrite('soccer_drawing.jpg', img)
```

###

## 결과물

![result](Cropped_2.jpg)
