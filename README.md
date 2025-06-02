# Crunchbase API Python Client

This is a simple Python script to authenticate with the Crunchbase API, retrieve user session cookies, and fetch company details including similar companies and high-level financial information.

---

## 📦 Features

- Authenticate a user via Crunchbase API and retrieve session cookies.
- Use those cookies to request detailed company information.
- Fetch company details, financial highlights, and similar companies.
- Clean, readable console output.

---

## 📁 Project Structure

.
├── config.py
├── main.py
├── requirements.txt
├── .env
└── README.md

---

## ⚙️ Requirements

- Python 3.8+
- `requests`
- `python-dotenv` (if using .env for config)

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔐 Environment Setup

Create a .env file to securely store your credentials:

```
    EMAIL=your_email@example.com
    PASSWORD=your_password
```

## 🚀 How to Use

1️⃣ Update your .env file with valid Crunchbase credentials.
2️⃣ Run the script: `python main.py`
