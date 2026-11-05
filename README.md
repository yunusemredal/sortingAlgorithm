# 🚀 Sıralama Algoritmaları Görselleştiricisi (Sorting Algorithm Visualizer)

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![GUI Framework](https://img.shields.io/badge/GUI-Tkinter-brightgreen.svg)
![Tests](https://img.shields.io/badge/Tests-11%2F11%20Passed-success.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

Bilgisayar bilimlerinde temel teşkil eden sıralama algoritmalarını etkileşimli, dinamik ve gerçek zamanlı animasyonlarla görselleştiren modern bir masaüstü uygulamasıdır. Algoritmaların çalışma adımlarını, karşılaştırmalarını, yer değiştirmelerini ve asimptotik zaman karmaşıklıklarını pratik bir şekilde inceleme imkânı sunar.

---

## ✨ Temel Özellikler

- **8 Farklı Sıralama Algoritması:** Bubble, Insertion, Selection, Merge, Quick, Heap, Shell ve Counting Sort.
- **Çok İş Parçacıklı (Multi-threaded) Motor:** Algoritmalar arka planda (worker thread) çalışır; animasyon sırasında arayüz asla kilitlenmez, akıcı olarak yanıt vermeye devam eder.
- **Tam Etkileşimli Kontrol:**
  - ▶ **Başlat (Start):** Seçili algoritmayı çalıştırır.
  - ⏸ **Duraklat / Devam Et (Pause / Resume):** Çalışma anında animasyonu dondurur ve kaldığı yerden devam ettirir.
  - ⏹ **Sıfırla / Durdur (Stop / Reset):** Çalışan özyinelemeli algoritmaları güvenli bir şekilde kesintiye uğratarak arayüzü sıfırlar.
- **Dinamik Veri Dağılımları:**
  - 🎲 **Rastgele (Random):** Standart karmaşık dağılım.
  - 📈 **Neredeyse Sıralı (Nearly Sorted):** Araya eklemeli algoritmaların $O(n)$ davranışını test etmek için idealdir.
  - 📉 **Ters Sıralı (Reversed):** En kötü durum ($O(n^2)$) senaryolarını gözlemlemek için uygundur.
  - 🔄 **Tekrarlı Değerler (Few Unique):** Yinelenen elemanların sıralama kararlılığına (stability) etkisini inceleme fırsatı verir.
- **Canlı Metrik Panosu:**
  - Gerçek zamanlı **Karşılaştırma Sayacı** (Comparisons).
  - Gerçek zamanlı **Yer Değiştirme / Yazma Sayacı** (Swaps / Writes).
  - Milisaniyelik hassasiyette **Geçen Süre** sayacı.
- **Karmaşıklık Bilgi Kartları & Analiz Grafiği:**
  - Her algoritmanın En İyi, Ortalama, En Kötü Zaman ve Bellek karmaşıklık göstergeleri.
  - $O(n)$, $O(n \log n)$ ve $O(n^2)$ asimptotik eğrilerini çizen ve mevcut $n$ eleman sayısını kıyaslayan bağımsız analiz penceresi.
- **Duyarlı Tuval (Responsive Canvas):** Pencere yeniden boyutlandırıldığında çubuklar tuval sınırlarını aşmaz; çubuk genişliği ve aralıkları otomatik ölçeklenir.

---

## 📊 Desteklenen Algoritmalar ve Karmaşıklıkları

| Algoritma | En İyi Zaman | Ortalama Zaman | En Kötü Zaman | Bellek Karmaşıklığı | Kararlılık (Stable) |
|---|---|---|---|---|---|
| **Bubble Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Evet |
| **Insertion Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Evet |
| **Selection Sort** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Hayır |
| **Merge Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Evet |
| **Quick Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ | Hayır |
| **Heap Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | Hayır |
| **Shell Sort** | $O(n \log n)$ | $O(n^{3/2})$ | $O(n^2)$ | $O(1)$ | Hayır |
| **Counting Sort** | $O(n + k)$ | $O(n + k)$ | $O(n + k)$ | $O(n + k)$ | Evet |

---

## 🎨 Renk Anlamları

Görselleştirme sırasında çubukların aldığı renkler şu anlamlara gelir:
- 🔵 **Mavi (`#4299e1`):** Sıralanmamış / Boştaki elemanlar.
- 🟡 **Sarı (`#ecc94b`):** Karşılaştırılan elemanlar veya tarama imleci.
- 🔴 **Kırmızı (`#e53e3e`):** Yer değiştiren (swap), ötelenen veya geçici üzerine yazılan elemanlar.
- 🟠 **Turuncu (`#dd6b20`):** Quick Sort pivotu veya ekleme/seçim hedef yuvası.
- 🟣 **Mor (`#9f7aea`):** Seçim sıralamasında bulunan anlık en küçük eleman adayı.
- 🟢 **Yeşil (`#48bb78`):** Doğru yerine yerleşmiş ve sıralanmış nihai elemanlar.

---

## 🛠️ Kurulum ve Çalıştırma

### Gereksinimler
- Python 3.8 veya üzeri (Tkinter Python ile birlikte dahili olarak gelmektedir).

### Adım 1: Bağımlılıkları Yükleme (İsteğe Bağlı / Testler İçin)
```bash
pip install -r requirements.txt
```

### Adım 2: Uygulamayı Başlatma
```bash
python display.py
```

---

## 🧪 Otomatize Testler (Pytest)

Tüm sıralama algoritmaları; sınır durumlar (boş dizi, tek eleman, pre-sorted, ters sıralı, negatif sayılar ve rastgele büyük veri setleri) üzerinde otomatize testlerle doğrulanmıştır:

```bash
python -m pytest tests/test_algorithms.py -v
```

Test Çıktısı:
```text
tests/test_algorithms.py::test_comparison_sort_correctness[bubbleSort] PASSED
tests/test_algorithms.py::test_comparison_sort_correctness[insertionSort] PASSED
tests/test_algorithms.py::test_comparison_sort_correctness[selectionSort] PASSED
tests/test_algorithms.py::test_comparison_sort_correctness[mergeSort] PASSED
tests/test_algorithms.py::test_comparison_sort_correctness[quickSort] PASSED
tests/test_algorithms.py::test_comparison_sort_correctness[heapSort] PASSED
tests/test_algorithms.py::test_comparison_sort_correctness[shellSort] PASSED
tests/test_algorithms.py::test_counting_sort_correctness PASSED
tests/test_algorithms.py::test_quick_sort_legacy_signature PASSED
tests/test_algorithms.py::test_metrics_tracking PASSED
tests/test_algorithms.py::test_random_large_datasets PASSED
============================= 11 passed in 0.48s ==============================
```

---

## 📂 Proje Dizin Yapısı

```
sortingAlgorithm/
├── .gitignore                      # Geçici dosyalar ve yerel filtreler
├── README.md                       # Proje tanıtım ve kullanım kılavuzu
├── requirements.txt                # Bağımlılıklar (pytest, opsiyonel numpy/matplotlib)
├── display.py                      # Ana GUI uygulaması (Multi-threaded Tkinter)
├── algorithmPush.py                # Algoritma kayıt merkezi ve metadata kütüphanesi
├── img/                            # Arayüz simgeleri ve görseller
├── src/
│   ├── algorithms/                 # Sıralama algoritma motorları
│   │   ├── bubbleSort.py           # Optimize edilmiş Bubble Sort (erken bitişli)
│   │   ├── insertionSort.py        # Adım adım Insertion Sort
│   │   ├── selectionSort.py        # Dinamik karşılaştırmalı Selection Sort
│   │   ├── mergeSort.py            # Düzeltilmiş (tüm indisleri kapsayan) Merge Sort
│   │   ├── quickSort.py            # Düzeltilmiş renk haritalı Quick Sort
│   │   ├── heapSort.py             # İkili tepe (Binary Heap) Heap Sort
│   │   ├── shellSort.py            # Gap aralıklı Shell Sort
│   │   └── countingSort.py         # Sayma tabanlı Counting Sort
│   └── graf/
│       └── grafics.py              # Asimptotik Big-O karmaşıklık grafiği
└── tests/
    └── test_algorithms.py          # Otomatize Pytest birim testleri
```
