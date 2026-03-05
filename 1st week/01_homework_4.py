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