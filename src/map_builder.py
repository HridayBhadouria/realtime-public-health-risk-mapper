import folium
from streamlit_folium import st_folium

def create_risk_map(lat, lon, air_quality, weather):
    m = folium.Map(location=[lat, lon], zoom_start=11)

    aqi_val = "N/A"
    pm25 = "N/A"
    
    if air_quality and "current" in air_quality:
        current_aq = air_quality["current"]
        aqi_val = current_aq.get("european_aqi", "N/A")
        pm25 = current_aq.get("pm2_5", "N/A")
        
        color = "green"
        if isinstance(aqi_val, (int, float)):
             if aqi_val > 40: color = "orange"
             if aqi_val > 60: color = "red"
             if aqi_val > 80: color = "purple"
        
        folium.Marker(
            [lat, lon],
            popup=f"<b>Air Quality</b><br>AQI: {aqi_val}<br>PM2.5: {pm25}",
            icon=folium.Icon(color=color, icon="cloud")
        ).add_to(m)

    folium.Circle(
        location=[lat, lon],
        radius=5000,
        color="blue",
        fill=True,
        fill_opacity=0.1,
        popup="Melbourne Metro Area"
    ).add_to(m)

    return m
