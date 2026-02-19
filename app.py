import streamlit as st
from src.data_fetchers import fetch_weather_data, fetch_air_quality, fetch_health_alerts
from src.map_builder import create_risk_map
from streamlit_folium import st_folium
import pandas as pd

# Page Config
st.set_page_config(page_title="Melbourne Health Risk Mapper", layout="wide")

# Title and Description
st.title("🚑 Melbourne Public Health Risk Mapper")
st.markdown("Real-time monitoring of Air Quality, Weather conditions, and Public Health Alerts.")

# Sidebar Controls
st.sidebar.header("Settings")
lat = st.sidebar.number_input("Latitude", value=-37.8136)
lon = st.sidebar.number_input("Longitude", value=144.9631)

if st.sidebar.button("Refresh Data"):
    st.experimental_rerun()

# Fetch Data
with st.spinner("Fetching latest data..."):
    weather_data = fetch_weather_data(lat, lon)
    aq_data = fetch_air_quality(lat, lon)
    alerts = fetch_health_alerts()

# Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Interactive Map")
    map_obj = create_risk_map(lat, lon, aq_data, weather_data)
    st_folium(map_obj, width=800, height=500)

with col2:
    st.subheader("Current Conditions")
    
    # Air Quality Card
    if aq_data and "current" in aq_data:
        curr = aq_data["current"]
        st.info(f"**PM2.5**: {curr.get('pm2_5')} µg/m³")
        st.info(f"**PM10**: {curr.get('pm10')} µg/m³")
        st.info(f"**Ozone**: {curr.get('ozone')} µg/m³")
    else:
        st.warning("Air Quality data unavailable")

    # Weather Card
    if weather_data and "current" in weather_data:
        curr_w = weather_data["current"]
        st.metric("Temperature", f"{curr_w.get('temperature_2m')} °C")
        st.metric("Wind Speed", f"{curr_w.get('wind_speed_10m')} km/h")
        st.write(f"Precipitation: {curr_w.get('precipitation')} mm")
    else:
        st.warning("Weather data unavailable")

# Health Alerts Section
st.subheader("📢 Victorian Health Alerts")
if alerts:
    for alert in alerts:
        st.error(f"**[{alert['title']}]({alert['link']})**")
else:
    st.success("No major health alerts detected (or source unreachable).")
    
st.markdown("---")
st.caption("Data Sources: Open-Meteo, Victorian Department of Health")
