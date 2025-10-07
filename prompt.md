# 線性迴歸專案說明與部署指南

## 1. 專案概觀

本專案旨在建立一個互動式的網頁應用程式，用於展示簡單的線性迴歸。

**核心功能需求：**
- **模型：** 使用 Python 實作簡單線性迴歸 (`y = ax + b`)。
- **互動性：** 允許使用者透過網頁介面即時調整以下參數：
    - 斜率 `a`
    - 雜訊 (noise)
    - 資料點數量
- **流程：** 遵循 CRISP-DM 的步驟來建構。
- **框架：** 使用 Streamlit 建立網頁介面。

---

## 2. 部署說明

本節將引導您完成此 Streamlit 應用程式的部署流程。

### 2.1. 前置準備

請確認以下項目皆已完成：

- **應用程式檔案**：主要的應用程式檔案為 `app.py`。
- **相依套件 (Dependencies)**：所有需要的 Python 套件都已列在 `requirements.txt` 檔案中。
- **本機驗證**：已透過 `streamlit run app.py` 指令，確認應用程式可以在本機正常執行。
- **版本控制**：專案程式碼已上傳至 GitHub 儲存庫 (repository)，並且為最新版本。

### 2.2. 部署步驟 (使用 Streamlit Community Cloud)

1.  **前往 Streamlit Community Cloud**：
    在瀏覽器中開啟 [https://share.streamlit.io/](https://share.streamlit.io/)。

2.  **登入**：
    使用您的 GitHub 帳號登入。

3.  **建立新應用程式 (New app)**：
    點擊頁面上的 "New app" 按鈕。

4.  **選擇儲存庫 (Repository)**：
    從列表中選擇您存放此專案的 GitHub 儲存庫。

5.  **設定部署選項**：
    - **Branch**：確認分支是否正確 (例如 `main` 或 `master`)。
    - **Main file path**：確認主要檔案路徑為 `app.py`。

6.  **部署 (Deploy!)**：
    點擊 "Deploy!" 按鈕。

平台將會開始建置並部署您的應用程式。完成後，您將會得到一個公開的網址，讓所有人都可以存取您的應用程式。