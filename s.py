import streamlit as st
import time

# Add some festive vibes 🎉
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂", layout="centered")

# Progress bar like a countdown
st.title("🎁 Birthday Countdown!")
progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.02)
    progress_bar.progress(i + 1)

# Spinner while loading fun
with st.spinner("Getting the cake ready... 🍰"):
    time.sleep(3)

# Birthday messages
st.success("🎉 Surprise!")
st.title("Happy Birthday, [Friend's Name]!")
st.header("Wishing you a day filled with joy, love, and endless cake! 🍰")
st.subheader("You deserve all the happiness in the world today and always.")
st.text("Here's a little something to make you smile 😊")

# Markdown styling
st.markdown("**You're not just a year older, you're a year better!**")
st.markdown("*May your day be as amazing as your friendship is to me.*")

# Fun effects 🥳
st.balloons()
st.snow()

# Clickable birthday cheer
if st.button("🎁 Click for a surprise"):
    st.info("Here's to many more birthdays and adventures together! 🎈")

# Footer note
st.write("---")
st.caption("Made with ❤️ by Jeevana")