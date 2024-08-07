from ultralytics import YOLO
import cv2
import random

# Modeli yükle
model = YOLO(r'C:\Users\yunus\Desktop\realtime\best.pt')

# Sınıf isimlerini ve renk paletini oluştur
class_names = model.names  # Modelin sınıf isimleri
color_palette = {i: (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for i in range(len(class_names))}

# Kamerayı başlat
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Genişliği ayarla
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Yüksekliği ayarla

while True:
    # Kameradan bir kare oku
    ret, frame = cap.read()
    if not ret:
        break

    # Modeli kullanarak karedeki nesneleri algıla
    results = model.predict(source=frame, save=False, save_txt=False)

    # Algılama sonuçlarını işle ve çiz
    for result in results:
        boxes = result.boxes  # Tespit edilen kutuları al
        for box in boxes:
            # Her kutu için koordinatları ve sınıfı al
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls = int(box.cls)  # Sınıfı int'e dönüştür
            conf = float(box.conf)  # Güven skorunu float'a dönüştür
            class_name = class_names[cls]  # Sınıf adını al
            color = color_palette[cls]  # Sınıfa göre renk al
            
            # Kutuları ve sınıf etiketlerini çizmek için OpenCV kullan
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)  # Kutuyu çiz
            label = f'{class_name} {conf:.2f}'
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)  # Sınıfı yaz

    # Sonuçları ekranda göster
    cv2.imshow('YOLOv8 Real-Time Detection', frame)

    # 'q' tuşuna basarak döngüyü sonlandır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı ve OpenCV penceresini serbest bırak
cap.release()
cv2.destroyAllWindows()

