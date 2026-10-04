import cv2
import os
from ultralytics import YOLO
from datetime import datetime
import telebot

# Telegram Bot Setup
TOKEN = ""
CHAT_ID = 8599447519
bot = telebot.TeleBot(TOKEN)

def send_telegram_alert(person_count, image_path=None):
    message = f"🚨 Crowd Alert Detected!\nPeople Count: {person_count}"
    bot.send_message(CHAT_ID, message)

    if image_path:
        with open(image_path, "rb") as img:
            bot.send_photo(CHAT_ID, img)

# Load YOLO model
model = YOLO("yolov8n.pt")

# Create folder for snapshots
os.makedirs("snapshots", exist_ok=True)

def detect_crowd(video_path, threshold=15):

    cap = cv2.VideoCapture(video_path)
    alert = False

    while True:

        success, frame = cap.read()
        if not success:
            break

        results = model(frame, verbose=False)
        people_count = 0

        for result in results:
            for box in result.boxes:
                cls = int(box.cls[0])

                if cls == 0:
                    people_count += 1
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

        cv2.putText(
            frame,
            f"People: {people_count}",
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255,0,0),
            2
        )

        if people_count >= threshold:

            alert = True

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"snapshots/{timestamp}.jpg"

            cv2.imwrite(filename, frame)

            cv2.putText(
                frame,
                "CROWD ALERT!",
                (20,80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,0,255),
                3
            )

            send_telegram_alert(people_count, filename)

        yield frame, people_count, alert

    cap.release()

