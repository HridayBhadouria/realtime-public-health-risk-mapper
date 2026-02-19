import requests
import pandas as pd
from datetime import datetime
import streamlit as st
from bs4 import BeautifulSoup

# Open-Meteo API Endpoints
WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"
AIR_QUALITY_API_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"

def fetch_weather_data(lat, lon):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "precipitation", "weather_code", "wind_speed_10m"],
        "hourly": ["uv_index"],
        "timezone": "Australia/Melbourne",
        "forecast_days": 1
    }
    
    try:
        response = requests.get(WEATHER_API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        current = data.get("current", {})
        hourly = data.get("hourly", {})
        

        current_hour_iso = current.get("time") # e.g., "2023-10-27T10:00"
        try:
             # Find index of current time in hourly list, or just take the closest
             # For simplicity in this demo, we'll just take the max UV of the day or current specific hour if easy
            # But let's verify exact current hour logic later. 
            # For now, let's just return the data structure
            pass
        except:
             pass

        return data
    except requests.RequestException as e:
        st.error(f"Error fetching weather data: {e}")
        return None

def fetch_air_quality(lat, lon):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": ["pm10", "pm2_5", "ozone", "nitrogen_dioxide", "sulphur_dioxide", "european_aqi"],
        "timezone": "Australia/Melbourne"
    }
    
    try:
        response = requests.get(AIR_QUALITY_API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error fetching air quality data: {e}")
        return None

def fetch_health_alerts():
    """
    Scrapes the Victorian Department of Health alerts page for recent headlines.
    Current URL: https://www.health.vic.gov.au/news-and-events/cho-health-advisory-alerts
    """
    url = "https://www.health.vic.gov.au/news-and-events/cho-health-advisory-alerts"
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        alerts = []
        items = soup.find_all(['h2', 'h3'])
        for item in items:
            link = item.find('a')
            if link:
                title = link.get_text(strip=True)
                href = link.get('href')
                if "alert" in title.lower() or "advisory" in title.lower() or "warning" in title.lower():
                    if href.startswith('/'):
                        href = "https://www.health.vic.gov.au" + href
                    
                    if not any(a['link'] == href for a in alerts):
                        alerts.append({"title": title, "link": href})
                        
                if len(alerts) >= 5: break
        
        if not alerts:
             return [{"title": "Check Official Health Alerts Page", "link": url}]
            
        return alerts

    except Exception as e:
        return [{"title": "Could not fetch alerts (Check Source)", "link": url}]
