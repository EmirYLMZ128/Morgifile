<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="App/Dashboard/src/assets/MainIcons/mainLogo4Dark.svg">
    <img alt="Morgifile Logo" src="App/Dashboard/src/assets/MainIcons/mainLogo.svg" width="128" height="128">
  </picture>
  <h1>Morgifile V4</h1>
</div>

[🇬🇧 English README](readme.md) | [🧩 Eklenti Dokümanı](Addon/README.md) | [📊 Dashboard Dokümanı](App/Dashboard/README.md)

Morgifile, web üzerindeki görselleri sorunsuz bir şekilde arşivlemek, kategorize etmek ve yönetmek için tasarlanmış güçlü bir **Firefox eklentisi + web dashboard** uygulamasıdır. Gerçek bir "Tasarımcı Asistanı" olarak hareket ederek görsel ilhamınızın her zaman güvende ve düzenli olmasını sağlar.

Proje; (izole bir arayüze sahip) bir Firefox eklentisi, yerel olarak çalışan bir Python sunucusu (FastAPI) ve toplanan verileri görselleştirip yönetmenizi sağlayan modern bir **Vue.js** dashboard arayüzünden oluşur.

---

## 🚀 Temel Özellikler

- **Anında Arşivleme:** Firefox eklentisini kullanarak herhangi bir web sitesindeki görseli **sağ tıklayarak** kaydedin.
- **Güçlü Backend:** Katı CORS politikalarını (ör. Instagram, Pinterest) aşmak için özel bir yerel proxy ile donatılmış **Python sunucusu** üzerinden görselleri işleyin.
- **SQLite Motoru:** Işık hızında ve güvenilir veri depolama.
- **Kalkan (Safe Storage):** Favori görsellerinizi fiziksel olarak yerel diskinize indirip arşivleyerek sonsuza kadar güvence altına alın.
- **Mezarlık (Graveyard) Sistemi:** Süresi dolan veya kırık linkleri anında tespit eden ve ana galerinizi tertemiz tutmak için sessizce özel bir Mezarlık kategorisine taşıyan otomatik temizleme mekanizması.
- **Akıllı Kopya Kontrolü:** URL analizi yaparak aynı görselin sisteme iki kez kaydedilmesini önler.
- **Tersine Görsel Arama:** Tek tıkla çalışan arama araçları (Google Lens, Yandex, TinEye) doğrudan dashboard içine entegre edilmiştir.

---

## 🧩 Proje Yapısı

- **[Firefox Extension](Addon/)**: Web sayfalarındaki görselleri algılar ve backend'e gönderir. **Shadow DOM** kullanılarak inşa edilmiştir.
- **[Python Local Server](App/)**: FastAPI ve Uvicorn ile geliştirilmiştir. Proxy isteklerini yönetir, WebSocket yayınlarını yapar ve verileri SQLite veritabanında saklar.
- **[Dashboard (Vue V4)](App/Dashboard/)**: Görsel kütüphanenizi yönetmek için **Vue 3 + Tailwind CSS** ile oluşturulmuş modern ve modüler arayüz.

---

## 🛠 Kullanılan Teknolojiler

- **Frontend:** Vue.js 3, Tailwind CSS, Vite
- **Backend:** Python, FastAPI, Uvicorn, SQLite
- **İletişim:** WebSockets, RESTful API
- **Tarayıcı:** Firefox Extension API

---

## ⚙️ Kurulum

1.  **Backend:** Python yerel sunucusunu çalıştırın (`python app.py`).
2.  **Eklenti:** `Addon` klasörünü `about:debugging` üzerinden Firefox'a yükleyin.
3.  **Dashboard:** 
    ```bash
    cd App/Dashboard
    npm install
    npm run dev
    ```
4.  Herhangi bir web sitesindeki görsele sağ tıklayarak arşivlemeye başlayın!

---

## 📌 Proje Durumu

Proje başarıyla **V4** sürümüne geçiş yapmıştır.
Temel mimari sağlamdır ve modüler Vue tabanlı dashboard'a geçiş tamamlanmıştır.

---

## 🗺 Roadmap

- **Arka Plan Sağlık Taraması (Health Check):** Kırık linkleri otomatik olarak tespit eden arka plan görevleri.
- **Yapay Zeka Prompt Asistanı:** Arşivlenen görsellerden AI araçları (Midjourney vb.) için detaylı promptlar oluşturma.
- **Renk Paleti Araçları:** Galeriden doğrudan baskın renkleri ve HEX kodlarını çıkarma.

---

## 🤝 Katkıda Bulunma

Morgifile, açık kaynaklı ve ticari olmayan bir projedir.
Özellik geliştirme, UI/UX iyileştirmeleri ve kod kalitesini artırma konularında katkıda bulunmak isteyen gönüllüler memnuniyetle karşılanır.

---

## 🤖 Not

Bu proje şu ana kadar **tamamen yapay zeka yardımı ile geliştirilmiştir**.

---

## 📄 Lisans

Bu proje kişisel ve ticari olmayan kullanım amaçlıdır.