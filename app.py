import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Campus Guardian", layout="wide")

st.markdown("## 🚨 Campus Guardian")
st.caption("AI-powered campus safety and emergency system")

# Sidebar
st.sidebar.title("User Panel")
user_name = st.sidebar.text_input("Your Name")
user_role = st.sidebar.selectbox("Role", ["Student", "Admin"])

st.divider()

# SOS SECTION
st.markdown("### 🚨 Emergency SOS")

col1, col2 = st.columns(2)

with col1:
    latitude = st.text_input("Latitude")
with col2:
    longitude = st.text_input("Longitude")

emergency = st.selectbox("Emergency Type", [
    "Harassment",
    "Medical",
    "Accident",
    "Lost",
    "Other"
])

if st.button("🚨 SEND SOS", use_container_width=True):
    if user_name and latitude and longitude:
        st.success("SOS sent successfully!")
        st.write("📍 Location:", latitude, ",", longitude)
        st.write("⚠️ Emergency:", emergency)
        st.write("🕒 Time:", datetime.now())
    else:
        st.error("Please fill all fields")

st.divider()

# Admin Dashboard
if user_role == "Admin":
    st.markdown("### 🛡️ Admin Dashboard")
    st.info("Live SOS requests will appear here")

    st.table({
        "Name": ["Nikitha", "Shashi"],
        "Emergency": ["Harassment", "Medical"],
        "Location": ["17.45, 78.39", "17.40, 78.42"]
    })
