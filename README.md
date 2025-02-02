# Su Üzerindeki Nesneleri Tespit Etme Algoritması

Bu proje, **su üzerindeki nesneleri tespit etmek** için OpenCV kullanılarak geliştirilmiş bir görüntü işleme algoritmasını içerir. Algoritma, su ve nesneler arasındaki **renk ve parlaklık farklılıklarını** kullanarak belirli manipülasyonlar uygular.

## 📌 **Algoritma Açıklaması**
Algoritma, su üzerindeki nesneleri belirlemek için şu adımları uygular:

### **1️⃣ Yeşil Kanal Manipülasyonu**
- Su genellikle **yeşil ve mavi renklerin karışımından** oluşur.
- Bu nedenle, yeşil kanal üzerinde **eşikleme** uygulanır:
  - **Yeşil değeri belirli bir eşiğin altında ise → `0` yapılır (siyah)**
  - **Yeşil değeri eşiğin üzerinde ise → `255` yapılır (beyaz)**  
  📌 **Amaç:** **Su ve nesneler arasındaki kontrastı artırmak.**

### **2️⃣ Mavi Kanal Manipülasyonu**
- Su genellikle **mavi tonlarında** olduğu için mavi kanal da işlenir.
- **Daha düşük parlaklıktaki (mavi ışığı soğuran) bölgeler nesne olabilir.**
- **Mavi değeri belirli bir eşik altında ise → `0` yapılır (siyah)**
- **Mavi değeri eşiğin üzerinde ise → `255` yapılır (beyaz)**  
  📌 **Amaç:** **Su üzerindeki nesneleri belirgin hale getirmek.**

### **3️⃣ Parlaklık (L Kanalı) İşlemi**
- Su yüzeyi **güneş ışığını yansıtır**, ancak nesneler ışığı **soğurur**.
- Bu yüzden **parlaklık farkı** kullanılarak nesneler daha görünür hale getirilir.
- **LAB renk uzayına** geçilerek **L (lightness) kanalı** üzerinden **CLAHE (Adaptif Histogram Eşitleme)** uygulanır.  
  📌 **Amaç:** **Kontrastı artırarak su yüzeyindeki nesneleri daha belirgin hale getirmek.**

### **4️⃣ Sonuçları Kaydetme**
- İşlenmiş görüntü **`test_result/output.jpg`** olarak kaydedilir.
- Eğer `"test_result"` klasörü yoksa otomatik oluşturulur.

## 🔧 **Gereksinimler**
Bu projeyi çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekir:

```bash
pip install opencv-python numpy
