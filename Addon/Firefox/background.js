const MENU_ID = "logImageURL";
const ICON_ACTIVE = {
  "16": "icons/16.png",
  "32": "icons/32.png",
  "48": "icons/48.png",
  "128": "icons/128.png"
};
const ICON_DISABLED = {
  "16": "icons/16Pas.png",
  "32": "icons/32Pas.png",
  "48": "icons/48Pas.png",
  "128": "icons/128Pas.png"
};

function getHostname(url) {
  try {
    return new URL(url).hostname;
  } catch {
    return null;
  }
}

function refreshContextMenu(enabled) {
  chrome.contextMenus.removeAll(() => {
    if (enabled) {
      chrome.contextMenus.create({
        id: MENU_ID,
        title: "🔗 Add to Morgifile",
        contexts: ["all"]
      });
    }
  });
}

function updateContextMenu(tabId, tab) {
  if (!tab?.url) return;

  const hostname = getHostname(tab.url);
  if (!hostname) return;

  chrome.storage.local.get(hostname, (res) => {
    const disabled = res[hostname] === true;

    chrome.browserAction.setIcon({
      tabId,
      path: disabled ? ICON_DISABLED : ICON_ACTIVE
    });

    refreshContextMenu(!disabled);
  });
}

/* TAB EVENTS */
chrome.tabs.onActivated.addListener(({ tabId }) => {
  chrome.tabs.get(tabId, (tab) => updateContextMenu(tabId, tab));
});

chrome.tabs.onUpdated.addListener((tabId, info, tab) => {
  if (info.status === "complete") {
    updateContextMenu(tabId, tab);
  }
});

/* INSTALL */
chrome.runtime.onInstalled.addListener(() => {
  refreshContextMenu(true);
  // ❌ No notification
});

/* CONTEXT MENU */
chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === MENU_ID && tab?.id) {
    chrome.tabs.sendMessage(tab.id, {
      action: "LOG_NEAREST_IMAGE"
    });
  }
});
