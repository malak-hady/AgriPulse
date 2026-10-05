# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="AgriPulse",
    page_icon="🌱",
    layout="wide"
)

# -----------------------------
# Load data
# -----------------------------

hotspots = pd.read_csv(
    "agri_pulse_hotspots_final.csv"
)

# -----------------------------
# Header
# -----------------------------

st.title("🌱 AgriPulse")

st.subheader(
    "Explainable Crop Stress & Inspection Intelligence"
)

st.caption(
    "Sentinel-2 based monitoring — Ismailia, Egypt"
)

st.divider()

# -----------------------------
# KPI metrics
# -----------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Persistent Stress",
        "10,473 pixels"
    )

with col2:
    st.metric(
        "High Priority",
        "1,048 pixels"
    )

with col3:
    st.metric(
        "Actionable Hotspots",
        "35"
    )

with col4:
    st.metric(
        "Hotspot Area",
        "9.16 ha"
    )

st.divider()

# -----------------------------
# Hotspot Map
# -----------------------------

st.header("📍 Crop-Stress Hotspots")

st.caption(
    "High-priority areas identified from persistent Sentinel-2 crop-stress indicators."
)

m = folium.Map(
    location=[30.555, 32.175],
    zoom_start=12,
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}",
    attr="Esri"
)

# Add hotspot markers
for _, row in hotspots.iterrows():

    popup_text = f"""
    <b>{row['Hotspot']}</b><br>
    Rank: {row['Rank']}<br>
    Priority: {row['Priority']}<br>
    Area: {row['Area_Ha']} ha<br>
    Stress Score: {row['Stress_Score']:.4f}
    """

    folium.CircleMarker(
        location=[
            row["Latitude"],
            row["Longitude"]
        ],
        radius=7,
        popup=folium.Popup(
            popup_text,
            max_width=300
        ),
        tooltip=row["Hotspot"],
        fill=True,
        fill_opacity=0.8
    ).add_to(m)

st_folium(
    m,
    width="100%",
    height=600
)

st.divider()

# -----------------------------
# Dataset preview
# -----------------------------

st.header("Actionable Hotspots")

st.dataframe(
    hotspots,
    width="stretch",
    hide_index=True
)
