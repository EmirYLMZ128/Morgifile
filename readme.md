<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="App/Dashboard/src/assets/MainIcons/mainLogo4Dark.svg">
    <img alt="Morgifile Logo" src="App/Dashboard/src/assets/MainIcons/mainLogo.svg" width="128" height="128">
  </picture>
  <h1>Morgifile V4</h1>
  <p><strong>The Ultimate One-Click Visual Inspiration Archive for Designers & Advertisers</strong></p>

  <p>
    <a href="https://github.com/EmirYLMZ128/Morgifile/releases/latest">
      <img src="https://img.shields.io/github/v/release/EmirYLMZ128/Morgifile?color=blue&label=Desktop%20App" alt="Latest Desktop Release" />
    </a>
    <a href="https://chromewebstore.google.com/detail/morgifile/icgiihngfimipelnnmcelcidjjoifdbo">
      <img src="https://img.shields.io/badge/Chrome%20Extension-Web%20Store-green?logo=googlechrome&logoColor=white" alt="Chrome Extension" />
    </a>
    <a href="https://addons.mozilla.org/en-US/firefox/addon/morgifile/">
      <img src="https://img.shields.io/badge/Firefox%20Extension-Add--ons-orange?logo=firefox&logoColor=white" alt="Firefox Extension" />
    </a>
    <a href="LICENSE">
      <img src="https://img.shields.io/github/license/EmirYLMZ128/Morgifile?color=red" alt="License" />
    </a>
  </p>

  <h4>
    🇹🇷 <a href="readme_Tr.md">Türkçe README</a> │ 🧩 <a href="Addon/README.md">Addon Docs</a> │ 📊 <a href="App/Dashboard/README.md">Dashboard Docs</a>
  </h4>

  ---
</div>

## 🎯 About The Project

As a **designer** or **advertiser**, inspiration can strike anywhere while browsing the web. **Morgifile** acts as your digital canvas assistant. It bridges the gap between active web browsing and organized moodboarding, allowing you to instantly archive visual content without losing your creative momentum.

With a seamless browser extension (available for **Chrome** and **Firefox**), a local **Python FastAPI backend server**, and a stunning **Vue 3 dashboard**, Morgifile downloads, catalogs, and secures your visual assets directly to your local hardware.

---

## ⚡ Core Value: One-Click Instant Archiving

Unlike traditional screenshot tools or complex cloud savers, Morgifile prioritizes speed and raw creative workflow:
* **Zero Disruption:** Just right-click any image on any webpage and select save.
* **No Background Switching:** The extension processes everything silently via an isolated Shadow DOM UI.
* **CORS & Proxy Engine:** Bypasses strict CORS policies to seamlessly download protected images from platforms like Instagram, Pinterest, and Behance using a built-in local proxy.

---

## 🚀 Key Features

| Feature | Description |
| :--- | :--- |
| **🛡️ Safe Local Storage** | Downloads and mirrors physical image files straight to your disk. No broken cloud links. |
| **🪦 Automated Graveyard** | Live-checks link health. If an image is deleted, corrupted, or unreachable at the source, it is marked as dead and moved to the Graveyard view automatically. |
| **🎨 Dynamic Color Palette** | Instantly extracts 5 dominant HEX color codes directly inside the dashboard gallery view with a single click. |
| **🔍 Multi-Engine Search**| Instantly find high-res variants or origins via Google Lens, Yandex, or TinEye with one click inside your dashboard. |
| **🧠 Smart De-Duplication**| Removes image parameters and checks signatures to prevent saving duplicate files. |
| **📡 Real-Time Sync** | WebSocket communication ensures the exact second you click save in the extension, the dashboard updates. |

---

## 🏗️ Technical Architecture

Morgifile uses a lightweight but robust three-tier architecture:

```
[ Browser Extensions ]  ---> ( WebSockets / REST ) --->  [ FastAPI Local Server ]
(Chrome & Firefox Shadow DOM)                              │ (SQLite Engine)
                                                           ▼
[ Vue 3 Dashboard ]    <--------------------------------- [ Safe Local Storage ]
```

* **Frontend Dashboard:** Vue.js 3, Tailwind CSS, Vite (Modern, highly visual grid layouts)
* **Local Backend Engine:** Python, FastAPI, Uvicorn, SQLite
* **Browser Layer:** WebExtensions API (Manifest V3 for Chrome, Manifest V2 for Firefox)

---

## ⚙️ Installation & Setup

Get up and running in three simple steps:

### 1. Install the Browser Extension
Add the extension to your preferred browser to enable one-click archiving:
* 🌐 **[Install Chrome Extension](https://chromewebstore.google.com/detail/morgifile/icgiihngfimipelnnmcelcidjjoifdbo)** *(Supports Google Chrome, Brave, Edge, Opera)*
* 🦊 **[Install Firefox Extension](https://addons.mozilla.org/en-US/firefox/addon/morgifile/)**

### 2. Download the Desktop Application
Download and run the latest precompiled release for your operating system to start the local backend server (running silently in your system tray):
* 💻 **[Download for Windows (.exe)](https://github.com/EmirYLMZ128/Morgifile/releases/latest)**
* 🍎 **[Download for macOS (.dmg / .app)](https://github.com/EmirYLMZ128/Morgifile/releases/latest)**

### 3. Start Saving!
Right-click any image on the web and save it directly into your categories. Open the dashboard via the system tray icon to view and manage your gallery!

---

## 🗺️ Product Roadmap

- [ ] **AI Prompt Generator:** Generate the exact prompts required to recreate or describe the saved image with a single click.
- [ ] **Tinder Mode:** A fun, swipe-based interface to easily organize, categorize, and clean up your saved visual library.
- [ ] **Custom Tagging & Sidebar Filtering:** Add custom tags to images and filter/list them via a dedicated tagging menu on the sidebar, similar to the color matching system.

---

## 🤖 AI Development Disclaimer

This project has been developed entirely with the strategic assistance of **artificial intelligence**, optimizing clean modern coding patterns alongside rapid human architectural review.

## 📄 License

Distributed under the **GPL-3.0 License**. Intended cleanly for personal and non-commercial development use-cases.