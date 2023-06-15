import cv2
image = cv2.imread('solar-system.jpg')
print(image)
cv2.putText(image,'Sun',(40,50),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=[0,0,255])
cv2.putText(image,'Mercury',(110,180),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=.5,color=[255,255,255])
cv2.putText(image,'Venus',(200,170),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=.5,color=[255,255,255])
cv2.putText(image,'Earth',(280,160),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=.5,color=[255,255,255])
cv2.putText(image,'Mars',(380,170),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=.5,color=[255,255,255])
cv2.putText(image,'Jupiter',(500,60),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=.5,color=[255,255,255])
cv2.putText(image,'Saturn',(800,135),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=.5,color=[255,255,255])
cv2.putText(image,'Uranus',(960,140),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=.5,color=[255,255,255])
cv2.putText(image,'Neptune',(1100,140),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=.5,color=[255,255,255])
cv2.imshow('Frame',image)
cv2.waitKey(10000)
final = cv2.imwrite('Final.jpg',image)