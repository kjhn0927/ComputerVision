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

if img is None:
    sys.exit('파일이 존재하지 않습니다.')

drawing_red = False
drawing_blue = False
brush_size = 3

# 드래그 관련 변수
dragging = False
ix, iy = -1, -1

def draw(event, x, y, flags, param):

    global drawing_red, drawing_blue
    global dragging, ix, iy, img

    if event == cv.EVENT_LBUTTONDOWN:
        drawing_red = True
        dragging = True
        ix, iy = x, y   # 시작 좌표 저장

    elif event == cv.EVENT_RBUTTONDOWN:
        drawing_blue = True

    elif event == cv.EVENT_MOUSEMOVE:
        # 드래그 중이면 사각형 표시
        if dragging:
            temp = img.copy()
            cv.rectangle(temp,(ix,iy),(x,y),(0,255,0),2)
            cv.imshow('Drawing',temp)
            return

    elif event == cv.EVENT_LBUTTONUP:
        drawing_red = False
        dragging = False

        # ROI 추출
        roi = img[iy:y, ix:x]

        if roi.size != 0:
            cv.imshow('Cropped', roi)
            cv.imwrite('cropped.jpg', roi)

    elif event == cv.EVENT_RBUTTONUP:
        drawing_blue = False

    cv.imshow('Drawing', img)


cv.namedWindow('Drawing')
cv.imshow('Drawing',img)

cv.setMouseCallback('Drawing',draw)

while(True):
    if cv.waitKey(1)==ord('q'):
        break

cv.destroyAllWindows()

cv.imwrite('soccer_drawing.jpg', img)
```

###

## 결과물

![result](Cropped_2.png)
