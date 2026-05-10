# 🧩 Morgifile Browser Extensions

Morgifile extensions are the entry point for your visual archiving. They live in your browser and allow you to capture images from any website with a single click.

## 🚀 Key Features

- **Context Menu Integration:** Right-click any image and select "Add to Morgifile" to save it instantly.
- **Shadow DOM UI:** Notifications and UI elements are encapsulated in a Shadow DOM to prevent styling conflicts with websites.
- **Real-time Communication:** Uses WebSockets to notify the dashboard immediately when a new image is added.
- **Proxy Bypass:** Sends image data to the local Python server, which handles CORS issues and physical storage.

## 🛠 How to Install (For Development)

### 🦊 Firefox
1.  Open Firefox and go to `about:debugging`.
2.  Click on **"This Firefox"** in the left sidebar.
3.  Click on **"Load Temporary Add-on..."**.
4.  Navigate to the `Addon/Firefox` folder and select the `manifest.json` file.

### 🌐 Chrome / Edge
1.  Open Chrome and go to `chrome://extensions`.
2.  Enable **"Developer mode"** in the top right.
3.  Click **"Load unpacked"**.
4.  Select the `Addon/Chrome-Beta-Version` folder.

## 📂 Structure

- `Firefox/`: Extension files optimized for Firefox (Manifest V2).
- `Chrome-Beta-Version/`: Extension files optimized for Chrome/Chromium (Manifest V3 - Beta).
- `content.js`: Handles right-clicks and UI notifications.
- `background.js`: Handles communication with the local server.

---

[⬅️ Back to Main README](../readme.md)

