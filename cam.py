import cv2

# Включаем первую камеру
cap = cv2.VideoCapture(0)

# "Прогреваем" камеру, чтобы снимок не был тёмным
for i in range(30):
    cap.read()

# Делаем снимок    
ret, frame = cap.read()

try:
	cv2.imwrite('cam1.png', frame)  
except Exception as e:
	print('camera unavailable')

# Отключаем камеру
cap.release()