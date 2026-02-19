# 🚑 Melbourne Public Health Risk Mapper

A real-time dashboard built with Python and Streamlit to monitor public health risks in Melbourne, Australia. This tool aggregates data from various sources to provide a unified view of environmental and health-related risks.

![App Screenshot](file:///Users/imperial/.gemini/antigravity/brain/8bc7c71f-7104-4acd-8be3-ae907fbfc623/streamlit_app_loaded_1771013676217.png)

## 🌟 Features

-   **Interactive Risk Map**: Visualize health risks across Melbourne with real-time markers.
-   **Air Quality Monitoring**: Real-time PM2.5, PM10, and Ozone levels (via Open-Meteo).
-   **Weather & UV Conditions**: Live temperature, wind speed, precipitation, and UV index.
-   **Health Alerts**: Automated scraping of official Victorian Department of Health alerts and advisories.
-   **Dynamic Controls**: Adjust location (Latitude/Longitude) and refresh data on demand.

## 🛠️ Technology Stack

-   **Backend**: Python 3.10+
-   **Framework**: [Streamlit](https://streamlit.io/)
-   **Mapping**: [Folium](https://python-visualization.github.io/folium/) & [streamlit-folium](https://github.com/randyzwitch/streamlit-folium)
-   **Data Sources**: 
    -   [Open-Meteo API](https://open-meteo.com/) (Weather & Air Quality)
    -   [Victorian Department of Health](https://www.health.vic.gov.au/) (Health Alerts)

## 🚀 Getting Started

### Prerequisites

-   Python 3.10 or higher installed.
-   `pip` package manager.

### Installation

1.  **Clone the repository** (or navigate to the project directory):
    ```bash
    cd realtime-public-health-risk-mapper
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

Launch the Streamlit dashboard by running:

```bash
streamlit run app.py
```

The app will be available in your browser at `http://localhost:8501`.

## 📂 Project Structure

```text
realtime-public-health-risk-mapper/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── src/
│   ├── data_fetchers.py    # Logic for API calls and scraping
│   └── map_builder.py      # Folium map generation logic
└── assets/                 # (Optional) Static assets
```

## ⚖️ Disclaimer

This tool is for informational purposes only. Always refer to official government sources (EPA Victoria, BOM, Vic Health) for critical safety information and emergency alerts.
