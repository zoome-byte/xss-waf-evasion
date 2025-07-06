# 🛡️ WAF Evasion for XSS: A Practical Study

This repository contains a Python script and a sample web application designed to demonstrate how character-based Web Application Firewall (WAF) filters can be bypassed using cleverly crafted Cross-Site Scripting (XSS) payloads.

> 🚨 **Warning**: This project is intended for **educational and authorized testing** purposes only. Do not use it against systems without explicit permission.

---

## 📌 Objective

To research how WAFs detect and block XSS attacks, and to build a Python script that generates payloads capable of bypassing common character-based filters.

---

## 📁 Files

| File Name              | Description                                                  |
|------------------------|--------------------------------------------------------------|
| `payload_generator.py` | Python script that generates XSS payloads to bypass WAFs     |
| `sample_app.py`        | Flask-based vulnerable app with a basic WAF-like XSS filter  |
| `alert_box.png`        | Screenshot showing successful XSS pop-up via a bypassed filter |
| `url.png`              | Screenshot showing the URL with the payload embedded         |

---

## 🚀 How to Use

### 1. Run the vulnerable Flask app:
```bash
python sample_app.py
