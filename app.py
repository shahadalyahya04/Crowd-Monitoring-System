import streamlit as st
import tempfile
import cv2

from crowd_detector import detect_crowd



st.title("🚦  Crowd Monitoring System")

st.write("Upload an event video to detect crowd congestion.")

uploaded_video = st.file_uploader(
    "Choose a video",
    type=["mp4", "avi", "mov"]
)

threshold = st.slider(
    "Crowd Alert Threshold",
    min_value=5,
    max_value=10,
    value=15
)

if uploaded_video is not None:

    temp_file = tempfile.NamedTemporaryFile(delete=False)

    temp_file.write(uploaded_video.read())

    st.success("Video uploaded successfully.")

    if st.button("Start Detection"):

        frame_window = st.empty()

        people_text = st.empty()

        alert_box = st.empty()

        for frame, people_count, alert in detect_crowd(
            temp_file.name,
            threshold
        ):

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            frame_window.image(
                frame,
                channels="RGB",
                use_container_width=True
            )

            people_text.metric(
                "People Detected",
                people_count
            )

            if alert:

                alert_box.error(
                    "🚨 Crowd Alert! High congestion detected."
                )

            else:

                alert_box.success(
                    "✅ Crowd level is normal."
                )

st.markdown("---")
