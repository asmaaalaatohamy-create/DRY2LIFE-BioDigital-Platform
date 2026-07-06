# 🔬 Technical Documentation - DRY2LIFE

This document provides a technical overview of the **DRY2LIFE** Bio-Digital Intelligence Platform architecture, data flows, and technical stack.

## 🏗️ System Architecture

The platform consists of three integrated layers:
1.  **Data Acquisition Layer (IoT):** Simulates and collects physical field readings (EC, Moisture, Temperature) via sensors.
2.  **Intelligence & Decision Engine:** Written in Python, utilizes rule-based algorithms calibrated with Egyptian agricultural research data to classify soil stress and estimate crop yields.
3.  **Presentation Layer (UI):** Built using Streamlit and Plotly for responsive, real-time data visualization and user interaction.

## 🛠️ Tech Stack
*   **Frontend/Backend Framework:** Streamlit (>= 1.28.0)
*   **Data Analysis:** Pandas & NumPy
*   **Data Visualization:** Plotly Express
*   **Hardware Simulation Core:** ESP32 micro-controller architecture (as simulated in `iot_simulation.mp4`).

## 🤖 Yield Prediction Algorithm
The system uses an adaptive reduction model based on Electrical Conductivity (EC) thresholds:
*   **Without PGPR:** Yield starts degrading rapidly after a threshold of 3.5 dS/m at a rate of 15% reduction per dS/m.
*   **With PGPR:** Degradation slope is heavily reduced to only 5% per dS/m due to bacterial bio-remediation effects (chlorophyll retention and root protection).  
