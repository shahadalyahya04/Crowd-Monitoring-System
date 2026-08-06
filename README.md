# AI-Based Crowd Monitoring System 

This project was developed as part of the **SDAIA Academy Training Program**, focusing on applying computer vision techniques to real-world safety and monitoring challenges. The system detects crowd congestion in video streams using **YOLOv8**, **OpenCV**, and **Streamlit**, and automatically sends alerts to Telegram when the number of detected people exceeds a defined threshold.

<img width="1280" height="720" alt="crowd Detection" src="https://github.com/user-attachments/assets/266fdc4b-a50d-451b-b6be-961448c5ace4" />

---

## 📌 Project Description

The Crowd Monitoring System provides an intelligent solution for monitoring crowded environments such as events, malls, stadiums, and public gatherings.  
Using YOLOv8 object detection, the system identifies people in each video frame, counts them, and triggers an alert when congestion is detected.  
A snapshot of the crowded frame is saved and sent to a Telegram bot for immediate notification.

This project demonstrates practical skills in:
- Computer Vision  
- Real-time object detection  
- Python application development  
- Streamlit web interfaces  
- Telegram bot integration  
- Model deployment and monitoring
<img width="590" height="497" alt="Screenshot crowd" src="https://github.com/user-attachments/assets/4cedbdf6-fd54-47f0-ad23-c58402f0a981" />

---

## Model Details

- Model: YOLOv8
- Task: Object Detection
- Target Class: Person
- Framework: Ultralytics
- Input: Video frames
- Output: Bounding boxes and people count
---
## 🧠 Features

- Real-time person detection using YOLOv8
- Configurable congestion threshold
- Automated snapshot generation during congestion events
- Telegram-based emergency notifications
- Interactive Streamlit monitoring dashboard

---

## 🛠️ Technologies Used

| Component | Description |
|----------|-------------|
| **Python 3.11** | Core programming language |
| **YOLOv8 (Ultralytics)** | Object detection model |
| **OpenCV** | Video processing |
| **Streamlit** | Web interface |
| **PyTelegramBotAPI** | Telegram bot integration |

---
## Training Program Reference
This project was developed under the SDAIA Academy Training Program, focusing on AI and computer vision 

SDAIA Academy GitHub:
https://github.com/SDAIAAcademy

## Author
Shahad Alyahya 
