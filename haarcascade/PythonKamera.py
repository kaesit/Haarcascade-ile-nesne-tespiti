import cv2


kamera = cv2.VideoCapture(0)
mycascade = cv2.CascadeClassifier('C:\opencv\mycascade\classifier\\cascade.xml')
font1 = cv2.FONT_HERSHEY_SIMPLEX
while True:
     ret,goruntu = kamera.read()

     goruntu = cv2.flip(goruntu, 1)
    
     gri_Kare = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)

     signs = mycascade.detectMultiScale(gri_Kare, 1.3, 7)
     for (i, j, x, y) in signs:
          cv2.rectangle(goruntu, (i, j), (i + x, j + y), (255, 0, 0), 2)
          cv2.putText(goruntu, "Saga Don", (i, j), font1, 1, (255, 0, 0), cv2.LINE_4)
     cv2.imshow("Kamera", goruntu)     
     #waitKey fonksiyonu parametresinde ki milisaniye değerine göre çekim yapar
     #0xFF ise bir tuşa basıldığında  koşula bağlı verilecek tepki için yazılır
     #'ord' ise tek karakter içindir. 
     if cv2.waitKey(1) & 0xFF == ord('q'):
          break


kamera.release()

cv2.destroyAllWindows()
