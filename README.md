# İşaret Dili Tercümanı Projesi

Bu proje, YOLOv8 kullanarak 10 kelimeyi tanıyan bir işaret dili tercümanı geliştirmeyi amaçlamaktadır. Proje, işaret dili öğrenmek isteyen kişiler için mobil bir uygulama olarak tasarlanmıştır ve gerçek zamanlı işaret dili çevirisi yapabilen bir AI modeli içermektedir.

## Proje Hakkında

İşaret dili tercümanı projesi, özel olarak oluşturulmuş bir veri seti kullanılarak geliştirilmiştir. Veri seti, Roboflow platformu kullanılarak özenle etiketlenmiştir ve modelin yüksek doğrulukla çalışabilmesi için gerekli olan tüm ön işleme adımları gerçekleştirilmiştir.

Modelin eğitimi, 100 epoch boyunca Google Colab üzerinde gerçekleştirilmiştir. Eğitim sürecinde elde edilen sonuçlar ve modelin performansı aşağıda detaylandırılmıştır.

## Veri Seti

Proje için kullanılan veri setine aşağıdaki bağlantıdan ulaşabilirsiniz:

[İşaret Dili Veri Seti - Kaggle](https://www.kaggle.com/datasets/yunusemrealsancak/sign-language-dataset)

## İlk Denemeler

Projenin ilk aşamalarında yapılan denemeler aşağıda gösterilmiştir:

![İlk Denemeler](https://github.com/YUNUSEMREALSANCAK/sign-language-interpreter-with-object-dedection/blob/main/trainn.jpeg)

## Confusion Matrix

Modelin doğruluğunu ve başarımını değerlendirmek için oluşturulan confusion matrix aşağıda verilmiştir:

![Confusion Matrix](https://github.com/YUNUSEMREALSANCAK/sign-language-interpreter-with-object-dedection/blob/main/confuconmatrix.png)

## K-Nearest Neighbors (KNN) Bilgisi

Projenin KNN algoritması ile yapılan değerlendirmesi aşağıda gösterilmiştir:

![KNN](https://github.com/YUNUSEMREALSANCAK/sign-language-interpreter-with-object-dedection/blob/main/knn.jpeg)



## Kullanım

Projenin nasıl kullanılacağına dair talimatlar ve daha fazla bilgi için lütfen [dokümantasyonu](https://github.com/YUNUSEMREALSANCAK/sign-language-interpreter-with-object-dedection) inceleyin.

1. **Gereksinimler**:
   - Python 3.8+
   - YOLOv8
   - Roboflow
   - Google Colab

2. **Kurulum**:
   ```bash
   git clone https://github.com/YUNUSEMREALSANCAK/sign-language-interpreter-with-object-dedection.git
   cd sign-language-interpreter-with-object-dedection
   pip install -r requirements.txt

