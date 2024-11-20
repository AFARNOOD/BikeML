# Analyzing The Behavior Of The Bike Sharing Service Users In Montreal

![Alt text]("https://github.com/AFARNOOD/BikeML/blob/main/imgs/DALL%C2%B7E%202024-11-20%2011.40.15%20-%20A%20wide%20aspect%20ratio%2C%20minimalistic%20illustration%20of%20urban%20bike-sharing%20in%20Montreal.%20The%20design%20includes%20a%20simple%20bicycle%20next%20to%20a%20modern%20urban%20bike%20rac.webp" width="600" height="400")

## LIST

## Contents

- [1. Overview](#overview)
- [2. Project Goals](#goals)
- [3. Approach](#approach)
- [4. Anticipated Insights](#insights)
- [5. Data Sources](#data)
   - [5.1. Data Acquisition](#data-acquisition)
- [6. Weather and Bike-Sharing](#weather-bike-sharing)
   - [6.1. Feature Overview](#feature-overview)
- [7. Tools and Techniques](#tools)
- [8. Reproducibility and Setup](#setup)
   - [8.1. Data Preparation](#data-prep)

 ---

## 1. Overview <a name="overview"></a>

This project explores the interplay between weather conditions and bike-sharing users' trip patterns, focusing on how factors like temperature, humidity, and cloud cover impact user behaviour. By leveraging machine learning, we aim to uncover meaningful insights that support the optimization of bike-sharing companies' operations.

---

## 2. Project Goals <a name="goals"></a>

The primary aim of this project is to analyze how weather variables influence the duration and frequency of bike trips. By building predictive models, we hope to provide actionable insights to improve user satisfaction and operational efficiency.

---

## 3. Approach <a name="approach"></a>

To achieve these goals, machine learning methods will be applied to analyze the relationships between trip characteristics and climatic conditions. By training models on relevant datasets, we can identify trends and correlations that enhance our understanding of user preferences under various weather scenarios.

---

## 4. Anticipated Insights <a name="insights"></a>

- Understanding user behavior in relation to changing weather conditions.
- Identifying patterns that could help BIXI optimize bike availability during different seasons.
- Informing potential strategies to encourage usage in less favorable weather.

---

## 5. Data Sources <a name="data"></a>

This project utilizes data from two key sources:

1. **Climate Data**:
   - Daily and hourly weather data for Montreal, sourced from Environment and Climate Change Canada (ECCC).
   - Focused on 2022 weather observations for Trudeau Airport (CYUL).

   [Data Source](https://www.canada.ca/en/environment-climate-change.html)

2. **BIXI Data**:
   - Open data on BIXI bike trips for 2021, including station locations and trip details.
   - Accessible via BIXI's open data portal.

   [Data Source](https://bixi.com/en/open-data)

---

### 5.1. Data Acquisition <a name="data-acquisition"></a>

Data was gathered from the sources above, ensuring a comprehensive dataset for analysis. This includes detailed weather parameters such as temperature, humidity, and wind chill, along with granular trip data from the BIXI system.

---

## 6. Weather and Bike-Sharing <a name="weather-bike-sharing"></a>

This project analyzes various weather and trip features, such as:

- **Climate Data Features**:
  - Temperature (min, max, average).
  - Humidity and cloud cover.
  - Wind chill and humidex.

- **BIXI Data Features**:
  - Station names and geographic coordinates.
  - Start and end times of trips.
  - Boroughs of trip origins and destinations.

### 6.1. Feature Overview <a name="feature-overview"></a>

A complete description of the features used in the analysis is available in the project repository.

---

## 7. Tools and Techniques <a name="tools"></a>

The following tools and concepts are used:

- **Python** for data manipulation and analysis.
- **Scikit-learn** and **XGBoost** for machine learning.
- **FastAPI** for model deployment and serving predictions.
- **Machine Learning Pipelines** to streamline the workflow.

---

## 8. Reproducibility and Setup <a name="setup"></a>

To reproduce the analysis and results, follow these steps:

### 8.1. Data Preparation <a name="data-prep"></a>

1. Clone the project repository.
2. Download the dataset by running the provided data acquisition notebook or script.
3. Ensure the downloaded data is stored in the appropriate directory.

> Note: Running the data processing notebook may require significant memory and time (approximately 10–15 minutes).

---
