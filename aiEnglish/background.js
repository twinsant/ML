chrome.runtime.onInstalled.addListener(() => {
    chrome.contextMenus.create({
      id: "aiLookup",
      title: "用AI查找",
      contexts: ["selection"]
    });
  });
  
  chrome.contextMenus.onClicked.addListener((info, tab) => {
    if (info.menuItemId === "aiLookup") {
      chrome.scripting.executeScript({
        target: { tabId: tab.id },
        function: showDefinition,
        args: [info.selectionText]
      });
    }
  });
  
  function showDefinition(selectedText) {
    const div = document.createElement("div");
    div.style.position = "fixed";
    div.style.top = "10px";
    div.style.right = "10px";
    div.style.backgroundColor = "white";
    div.style.border = "1px solid black";
    div.style.padding = "10px";
    div.style.zIndex = 10000;
    div.innerText = `AI 释义: ${selectedText}`;
    document.body.appendChild(div);
  
    setTimeout(() => {
      document.body.removeChild(div);
    }, 5000);
  }