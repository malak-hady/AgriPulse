# 🌱 AgriPulse

## Explainable Crop Stress & Inspection Intelligence

AgriPulse is a remote-sensing based crop monitoring system designed to identify areas showing persistent indicators of potential crop stress and prioritize them for field inspection and irrigation assessment.

## 🎯 Problem

Agricultural managers need to know which areas may require closer inspection.

AgriPulse analyzes multi-date Sentinel-2 imagery to detect persistent changes in vegetation and moisture-related indicators.

## 💡 Solution

- Sentinel-2 Level-2A imagery
- NDVI
- NDMI
- SCL vegetation masking
- Multi-date change detection
- Persistent stress detection
- Stress scoring
- High-priority hotspot extraction
- Interactive geographic visualization

## 🛰️ Data

**Analysis Period:** 5 August 2026 → 16 September 2026

**Area of Interest:** 10 × 10 km — Ismailia, Egypt

Selected observations:
- 5 August 2026
- 25 August 2026
- 16 September 2026

## 🔬 Methodology

1. Sentinel-2 multi-date imagery selection
2. Vegetation masking using SCL
3. NDVI calculation
4. NDMI calculation
5. Temporal change detection
6. Potential crop-stress identification
7. Persistent stress detection
8. Stress score calculation
9. High-priority hotspot extraction
10. Interactive map visualization

## 📊 Results

| Metric | Result |
|---|---:|
| Persistent Stress | 10,473 pixels |
| High Priority | 1,048 pixels |
| Actionable Hotspots | 35 |
| Hotspot Area | 9.16 ha |

## 🗺️ Dashboard

The AgriPulse dashboard provides:
- Key performance indicators
- Interactive crop-stress map
- Hotspot locations
- Hotspot ranking
- Area of each hotspot
- Stress score
- Latitude and longitude
- Analysis methodology

## ⚠️ Interpretation

AgriPulse identifies areas showing persistent remote-sensing indicators of potential crop stress.

The results are intended to prioritize field inspection and irrigation assessment.

They do not confirm crop stress or irrigation requirements without ground validation.

## 🧰 Technologies

- Python
- Pandas
- Xarray
- Rasterio / Rioxarray
- Sentinel-2
- Streamlit
- Folium
- OpenStreetMap

## 📁 Project Structure

```text
AgriPulse/
├── AgriPulse_Project.ipynb
├── app.py
├── agri_pulse_hotspots_final.csv
├── agri_pulse_summary.json
├── README.md
└── sample_data/
```

## 🚀 Running the Dashboard

```bash
pip install streamlit pandas folium streamlit-folium
streamlit run app.py
```

## 🌱 Future Improvements

- Hyperspectral observations where available
- Additional temporal observations
- Field-level ground validation
- Weather and irrigation data integration
- Machine-learning based stress classification
- Automated monitoring and alerts

## 👥 Project

**AgriPulse — Explainable Crop Stress & Inspection Intelligence**

Precision Agriculture & Crop Intelligence