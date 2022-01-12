import cv2

kamera = cv2.videoCapture(0)

while True:
  goruntu = kamera.read()
  
  cv2.imshow("Kamera", goruntu)
  if cv2.waitKey(1) and 0xFF == ord('q'):
    break
    
kamera.release()

cv2.destoroyAllWindows()
