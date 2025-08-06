# 🏛️ Court Data Fetcher & Mini-Dashboard

A simple Flask web app to fetch and display Indian court case data based on:
- Case Type
- Case Number
- Filing Year

Supports **Faridabad District Court** (https://districts.ecourts.gov.in/faridabad) via scraping.

---

## 🚀 Features

- 🔎 Simple web form for user input
- 📥 Scrapes real case metadata and recent orders
- 📄 PDF download link for latest order/judgment
- 🧠 CAPTCHA bypass using **manual entry via Selenium**
- 💾 SQLite logging of all queries and raw HTML responses
- 💅 Clean UI with responsive design and loading animation

---

## ⚙️ Tech Stack

- **Python 3**
- **Flask**
- **Selenium** (for dynamic scraping)
- **BeautifulSoup**
- **SQLite**
- HTML/CSS + Vanilla JavaScript

---

## 🧠 CAPTCHA Handling Strategy

- We use **Selenium** to launch the court website in a real browser.
- CAPTCHA is solved **manually by the user**, as allowed per the task spec.
- After solving CAPTCHA in the browser, the user **presses Enter in the terminal** to continue scraping.

This is a **legal, ethical and human-assisted approach** approved by the assignment.

---

## 🛠️ Setup Instructions

### 1. Clone and Install
```bash
git clone https://github.com/yourusername/court-dashboard.git
cd court-dashboard
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate on Linux/macOS
pip install -r requirements.txt
