import cv2 as cv
import sys

img = cv.imread('soccer.jpg')

if img is None :
    sys.exit('파일이 존재하지 않습니다.')

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY) #BGR컬러 사진을 흑백 사진으로 변환 = Gray 사진
gray_small=cv.resize(gray,dsize=(0,0),fx=0.5,fy=0.5) #Gray 사진을 절반(0.5)으로 축소 = Gray_small 사진

cv.imwrite('soccer_gray.jpg',gray) # 새로 만든 Gray 사진을 soccer_gray라는 파일이름으로 저장
cv.imwrite('soccer_gray_small.jpg',gray_small) # 새로 만든 Gray_small 사진을 soccer_gray_small이라는 파일이름으로 저장

cv.imshow('Color image', img) #컬러 사진 표시
cv.imshow('Gray image', gray) #흑백 사진 표시
cv.imshow('Gray image small', gray_small) #작은 흑백 사진 표시

cv.waitKey()
cv.destroyAllWindows()

print(type(img))
print(img.shape)