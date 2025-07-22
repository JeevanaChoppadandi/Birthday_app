import streamlit as st
from datetime import datetime
import time

# Set page config
st.set_page_config(page_title="🎂 Geetha's Birthday Bash", page_icon="🎉", layout="centered")

# Countdown logic
now = datetime.now()
target_hour = 0  # Midnight
time_remaining = 60 * (60 - now.minute) + (60 - now.second)

if time_remaining > 0:
    st.title("🎈 Countdown to Geetha's Birthday!")
    st.info("Hang on... magic begins at midnight 🕛")
    progress = st.progress(0)
    for i in range(100):
        time.sleep(time_remaining / 100)
        progress.progress(i + 1)
    st.experimental_rerun()
else:
    st.balloons()
    st.success("🎉 HAPPY BIRTHDAY GEETHA!!😘🎂")
    st.markdown("## 🎂 Wishing you love, laughter & joy forever!")
    if st.button("💌 Open your first surprise"):
        st.switch_page("photo_page.py")