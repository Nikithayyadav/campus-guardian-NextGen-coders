from ai import analyze

import streamlit as st
from datetime import datetime
from firebase import ref
import pandas as pd 
from streamlit_js_eval import get_geolocation

st.set_page_config(page_title="Campus Guardian", layout="wide")

st.markdown("## 🚨 Campus Guardian")
st.caption("AI-powered campus safety and emergency system")

# ---------------- Sidebar ----------------
st.sidebar.title("User Panel")
user_name = st.sidebar.text_input("Your Name")
user_role = st.sidebar.selectbox("Role", ["Student", "Admin"])

st.divider()

# ---------------- Auto Location ----------------
st.markdown("### 📍 Your Live Location")

location = get_geolocation()

if location:
    lat = location["coords"]["latitude"]
    lng = location["coords"]["longitude"]
    st.success(f"Location detected: {lat}, {lng}")
else:
    st.warning("Please allow location access in your browser.")

# ---------------- SOS ----------------
st.markdown("### 🚨 Emergency SOS")

emergency = st.selectbox(
    "Emergency Type",
    ["Harassment", "Medical", "Accident", "Lost", "Other"]
)

if st.button("🚨 SEND SOS", use_container_width=True):
    if user_name and location:
        data = {
            "name": user_name,
            "lat": float(lat),
            "lng": float(lng),
            "emergency": emergency,
            "time": str(datetime.now())
        }

        ai_result = analyze(emergency, lat, lng)
        data["ai_analysis"] = ai_result
        ref.push(data)
        st.success("SOS sent with AI risk analysis!")

    else:
        st.error("Enter your name and allow location access")

st.divider()

# ---------------- ADMIN PANEL ----------------
if user_role == "Admin":
    st.markdown("### 🛡️ Live SOS Alerts")

    data = ref.get()

    if data:
        rows = list(data.values())
        df = pd.DataFrame(rows)

        st.table(df)
        st.markdown("### 🧠 AI Danger Analysis")
        for i in df["ai_analysis"]:
            st.write(i)


        st.markdown("### 🗺️ Live Map")

        # Streamlit map needs columns named latitude & longitude
        map_df = df.rename(columns={"lat": "latitude", "lng": "longitude"})
        map_df["latitude"] = map_df["latitude"].astype(float)
        map_df["longitude"] = map_df["longitude"].astype(float)

        st.map(map_df[["latitude", "longitude"]])
    else:
        st.warning("No SOS alerts yet")
