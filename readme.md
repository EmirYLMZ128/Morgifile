<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="App/Dashboard/src/assets/MainIcons/mainLogo4Dark.svg">
    <img alt="Morgifile Logo" src="App/Dashboard/src/assets/MainIcons/mainLogo.svg" width="128" height="128">
  </picture>
  <h1>Morgifile V4</h1>
</div>

[🇹🇷 Türkçe README](readme_Tr.md) | [🧩 Addon Docs](Addon/README.md) | [📊 Dashboard Docs](App/Dashboard/README.md)

Morgifile is a powerful **Firefox extension + web dashboard** application designed to seamlessly archive, categorize, and manage web images. Acting as a true "Designer's Assistant," it ensures your visual inspiration is always safe and organized.

The project consists of a Firefox extension (featuring an isolated UI), a locally running Python server (FastAPI), and a modern **Vue.js** dashboard interface that visualizes and manages the collected data.

---

## 🚀 Key Features

- **Instant Archiving:** Save images from any website via **right-click** using the Firefox extension.
- **Robust Backend:** Process images through a **local Python server** equipped with a custom proxy to bypass strict CORS policies (e.g., Instagram, Pinterest).
- **SQLite Engine:** Lightning-fast and reliable data storage.
- **Safe Storage:** Shield your favorite images by physically downloading and archiving them to your local disk.
- **The Graveyard System:** An auto-cleaning mechanism that detects expired or broken links and moves them to a dedicated Graveyard category.
- **Smart Duplicate Check:** Prevents saving the same image twice by analyzing URLs.
- **Reverse Image Search:** Integrated one-click search tools (Google Lens, Yandex, TinEye) directly inside the dashboard.

---

## 🧩 Project Structure

- **[Firefox Extension](Addon/)**: Detects images on web pages and sends them to the backend. Built with **Shadow DOM** to prevent CSS conflicts.
- **[Python Local Server](App/)**: Built with FastAPI and Uvicorn. Handles proxy requests, WebSocket broadcasts, and SQLite storage.
- **[Dashboard (Vue V4)](App/Dashboard/)**: A modern, modular interface built with **Vue 3 + Tailwind CSS** for managing your visual library.

---

## 🛠 Technologies Used

- **Frontend:** Vue.js 3, Tailwind CSS, Vite
- **Backend:** Python, FastAPI, Uvicorn, SQLite
- **Communication:** WebSockets, RESTful APIs
- **Browser:** Firefox Extension API

---

## ⚙️ Installation

1.  **Backend:** Run the Python local server (`python app.py`).
2.  **Extension:** Load the `Addon` folder into Firefox via `about:debugging`.
3.  **Dashboard:** 
    ```bash
    cd App/Dashboard
    npm install
    npm run dev
    ```
4.  Start archiving images by right-clicking on them!

---

## 📌 Project Status

The project has successfully transitioned to **V4**.
The core architecture is robust, and the transition to a modular Vue-based dashboard is complete.

---

## 🗺 Roadmap

- **Backend Health Check:** Automated background tasks to detect dead links.
- **AI Prompt Assistance:** Generate detailed prompts for AI tools (Midjourney, etc.) from archived images.
- **Color Palette Tools:** Extract dominant colors and HEX codes directly from the gallery.

---

## 🤝 Contributing

Morgifile is an open-source, non-commercial project.
Contributors are welcome to help improve features, UI/UX, and code quality.

---

## 🤖 Note

This project has been developed **entirely with the assistance of artificial intelligence**.

---

## 📄 License

This project is intended for personal and non-commercial development purposes.