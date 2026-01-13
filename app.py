import streamlit as st
from datetime import datetime
from firebase import ref

st.set_page_config(page_title="Campus Guardian", layout="wide")

st.markdown("## 🚨 Campus Guardian")
st.caption("AI-powered campus safety and emergency system")

# Sidebar
st.sidebar.title("User Panel")
user_name = st.sidebar.text_input("Your Name")
user_role = st.sidebar.selectbox("Role", ["Student", "Admin"])

st.divider()

# =========================
# SOS SECTION
# =========================
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
        data = {
            "name": user_name,
            "lat": latitude,
            "lng": longitude,
            "emergency": emergency,
            "time": str(datetime.now())
        }

        # Save to Firebase
        ref.push(data)

        st.success("SOS sent successfully to campus security!")
    else:
        st.error("Please fill all fields")

st.divider()

# =========================
# ADMIN DASHBOARD
# =========================
if user_role == "Admin":
    st.markdown("### 🛡️ Live SOS Alerts")

    data = ref.get()

    if data:
        rows = list(data.values())
        st.table(rows)
    else:
        st.info("No SOS alerts yet")
