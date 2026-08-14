<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="App/Dashboard/src/assets/MainIcons/mainLogo4Dark.svg">
    <img alt="Morgifile Logo" src="App/Dashboard/src/assets/MainIcons/mainLogo.svg" width="128" height="128">
  </picture>
  <h1>Morgifile V4</h1>
  <p><strong>Tasarımcılar & Reklamcılar İçin Tek Tıkla Görsel İlham Arşivleme Asistanı</strong></p>

  <p>
    <a href="https://github.com/EmirYLMZ128/Morgifile/releases/latest">
      <img src="https://img.shields.io/github/v/release/EmirYLMZ128/Morgifile?color=blue&label=Masa%C3%BCst%C3%BC%20Uygulamas%C4%B1" alt="Son Masaüstü Sürümü" />
    </a>
    <a href="https://chromewebstore.google.com/detail/morgifile/icgiihngfimipelnnmcelcidjjoifdbo?hl=tr">
      <img src="https://img.shields.io/badge/Chrome%20Eklentisi-Web%20Ma%C4%9Fazas%C4%B1-green?logo=googlechrome&logoColor=white" alt="Chrome Eklentisi" />
    </a>
    <a href="https://addons.mozilla.org/tr/firefox/addon/morgifile/">
      <img src="https://img.shields.io/badge/Firefox%20Eklentisi-Eklentiler-orange?logo=firefox&logoColor=white" alt="Firefox Eklentisi" />
    </a>
    <a href="LICENSE">
      <img src="https://img.shields.io/github/license/EmirYLMZ128/Morgifile?color=red" alt="Lisans" />
    </a>
  </p>

  <h4>
    🇬🇧 <a href="readme.md">English README</a> │ 🧩 <a href="Addon/README.md">Eklenti Dokümanı</a> │ 📊 <a href="App/Dashboard/README.md">Dashboard Dokümanı</a>
  </h4>

  ---
</div>

## 🎯 Proje Hakkında

Bir **tasarımcı** veya **reklamcı** olarak, web'de gezinirken ilhamın nerede geleceği belli olmaz. **Morgifile**, dijital tuval asistanınız olarak hareket etmek için tasarlanmıştır. Aktif web aramaları ile düzenli ruh panoları (moodboards) arasındaki boşluğu doldurarak, yaratıcı iş akışınızı bozmadan görselleri anında arşivlemenizi sağlar.

Tarayıcı eklentisi (**Chrome** ve **Firefox** destekli), yerel olarak çalışan güçlü bir **Python FastAPI arka uç sunucusu** ve göz alıcı bir **Vue 3 paneli (dashboard)** ile Morgifile; görsellerinizi doğrudan yerel diskinize indirir, kategorize eder ve güvende tutar.

---

## ⚡ Temel Değer: Tek Tıkla Anında Arşivleme

Geleneksel ekran görüntüsü araçlarının veya karmaşık bulut tabanlı kaydedicilerin aksine, Morgifile hız ve yaratıcı iş akışını ön planda tutar:
* **Sıfır Kesinti:** Herhangi bir web sayfasındaki görselin üzerine sağ tıklayın ve kaydet'i seçin.
* **Sekme Değiştirmeye Gerek Yok:** Eklenti, izole bir Shadow DOM arayüzü sayesinde her şeyi arka planda sessizce işler.
* **CORS & Proxy Motoru:** Instagram, Pinterest ve Behance gibi platformların katı CORS korumalarını yerleşik yerel proxy sunucusuyla aşarak görselleri sorunsuz şekilde indirir.

---

## 🚀 Öne Çıkan Özellikler

| Özellik | Açıklama |
| :--- | :--- |
| **🛡️ Güvenli Yerel Depolama (Kalkan)** | Görselleri fiziksel olarak yerel diskinize indirip yedekler. Kırık veya silinen bulut linkleri tarihe karışır. |
| **🪦 Otomatik Mezarlık (Graveyard)** | Kaynak URL'lerin durumunu kontrol eder. Görsel kaynak siteden silinmiş veya bozulmuşsa, otomatik olarak Mezarlık görünümüne taşınır. |
| **🎨 Dinamik Renk Paleti** | Dashboard paneli üzerinden tek tıkla görselin en baskın 5 rengini HEX kodlarıyla birlikte çıkarır. |
| **🔍 Çoklu Motorla Tersine Arama** | Tek tıkla Google Lens, Yandex veya TinEye üzerinden görselin yüksek çözünürlüklü alternatiflerini veya kaynağını bulur. |
| **🧠 Akıllı Kopya Kontrolü** | Görsel URL'lerini ve yapısal desenlerini analiz ederek aynı görselin sisteme tekrar kaydedilmesini engeller. |
| **📡 Gerçek Zamanlı Eşitleme** | WebSocket bağlantısı sayesinde tarayıcıdan kaydet dediğiniz an panel saniyesinde güncellenir. |

---

## 🏗️ Teknik Mimari

Morgifile, hafif ama dayanıklı 3 katmanlı bir mimariye sahiptir:

```
[ Tarayıcı Eklentileri ]  ---> ( WebSockets / REST ) --->  [ FastAPI Yerel Sunucu ]
(Chrome & Firefox Shadow DOM)                                │ (SQLite Veritabanı)
                                                             ▼
[ Vue 3 Dashboard Paneli ] <-------------------------------- [ Güvenli Yerel Depolama ]
```

* **Ön Uç Dashboard Paneli:** Vue.js 3, Tailwind CSS, Vite (Modern, yüksek görselliğe sahip grid yapısı)
* **Yerel Arka Uç Motoru:** Python, FastAPI, Uvicorn, SQLite
* **Tarayıcı Katmanı:** WebExtensions API (Chrome için Manifest V3, Firefox için Manifest V2)

---

## ⚙️ Kurulum & Çalıştırma

Sistemi 3 kolay adımda kurup kullanmaya başlayın:

### 1. Tarayıcı Eklentisini Kurun
Tek tıkla arşivleme özelliğini etkinleştirmek için öncelikle eklentiyi tarayıcınıza ekleyin:
* 🌐 **[Chrome Eklentisini Kur](https://chromewebstore.google.com/detail/morgifile/icgiihngfimipelnnmcelcidjjoifdbo?hl=tr)** *(Google Chrome, Brave, Edge, Opera destekler)*
* 🦊 **[Firefox Eklentisini Kur](https://addons.mozilla.org/tr/firefox/addon/morgifile/)**

### 2. Masaüstü Uygulamasını İndirin
İşletim sisteminiz için en son derlenmiş sürümü indirip çalıştırın (uygulama sistem tepsisinde sessizce arka plan sunucusunu başlatacaktır):
* 💻 **[Windows için İndir (.exe)](https://github.com/EmirYLMZ128/Morgifile/releases/latest)**
* 🍎 **[macOS için İndir (.dmg / .app)](https://github.com/EmirYLMZ128/Morgifile/releases/latest)**

### 3. Kaydetmeye Başlayın!
Web üzerindeki görsellere sağ tıklayıp istediğiniz kategoriye kaydedin. Tepsiden paneli açarak kütüphanenizi yönetmeye başlayın!

---

## 🗺️ Yol Haritası (Roadmap)

- [ ] **Prompt Generator:** Tek tıkla kaydedilen görselin yeniden üretimi veya tarifi için gerekli promptu (görsel üreteç girdisini) tek tıkla oluşturma.
- [ ] **Tinder Mode:** Kaydettiğiniz görselleri kolayca temizlemek, beğenmek veya düzenlemek için eğlenceli, kaydırma (swipe) tabanlı bir mod.
- [ ] **Özel Etiketleme (Tagging) & Yan Menü Filtreleme:** Görsellere özel etiketler ekleme ve yan menüde bulunan etiket menüsünden (renk eşleştirme sistemine benzer şekilde) görselleri etiketlerine göre seçip listeleme.

---

## 🤖 Yapay Zeka Geliştirme Notu

Bu proje, modern kodlama kalıplarını optimize etmek ve hızlı mimari incelemeyi kolaylaştırmak amacıyla tamamen **yapay zeka desteğiyle** geliştirilmiştir.

## 📄 Lisans

**GPL-3.0 Lisansı** ile dağıtılmaktadır. Kişisel ve ticari olmayan geliştirme amaçlı kullanılması hedeflenmiştir.