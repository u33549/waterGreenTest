#geliştirmede kullanılan gpt sohbeti:
# https://chatgpt.com/share/679f3c78-41d8-800f-ac18-b41e94617406

import cv2
import numpy as np
import os

# Görüntüyü yükle
fileName="img_3.jpg"
image = cv2.imread("test_data/"+fileName)
image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
cv2.imshow("original", image)

if image is None:
    print("Hata: Görüntü yüklenemedi! Dosya yolunu kontrol et.")
    exit()

# Yeşil ve mavi kanalları al
green_channel = image[:, :, 1]  # Yeşil kanal (G)
blue_channel = image[:, :, 0]   # Mavi kanal (B)

# Eşikleme faktörleri
greenFact = 150
blueFact = 150

# Yeşil kanal eşikleme işlemi
green_channel[green_channel <= greenFact] = 0
green_channel[green_channel > greenFact] = 255

# Mavi kanal eşikleme işlemi
blue_channel[blue_channel <= blueFact] = 0
blue_channel[blue_channel > blueFact] = 255

# Güncellenmiş kanalları geri koy
image[:, :, 1] = green_channel
image[:, :, 0] = blue_channel

# LAB renk uzayına çevir (Kontrast artırma için)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# L kanalını al (aydınlık bilgisi)
l, a, b = cv2.split(lab)

# CLAHE (Adaptif Histogram Eşitleme) uygula
clahe = cv2.createCLAHE(clipLimit=150.0, tileGridSize=(8, 8)) #belli bir değerden sonra değişimi bırakıyor kafadan yüksek bir değer verdim
l_equalized = clahe.apply(l)

# Kanalları tekrar birleştir
lab_equalized = cv2.merge((l_equalized, a, b))

# BGR uzayına geri çevir
image_enhanced = cv2.cvtColor(lab_equalized, cv2.COLOR_LAB2BGR)

# **Sonucu Kaydetme**
output_folder = "test_result"
os.makedirs(output_folder, exist_ok=True)  # Klasör yoksa oluştur

output_path = os.path.join(output_folder, fileName)
cv2.imwrite(output_path, image_enhanced)

print(f"Sonuç başarıyla '{output_path}' olarak kaydedildi!")

# Sonucu göster
cv2.imshow("filtered", image_enhanced)
cv2.waitKey(0)
cv2.destroyAllWindows()
