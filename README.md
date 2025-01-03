# BikeML-API: Analyzing the Behavior of Bike-Sharing Users in Montreal

<img src="https://github.com/AFARNOOD/BikeML/blob/main/imgs/DALL%C2%B7E%202024-11-20%2011.40.15%20-%20A%20wide%20aspect%20ratio%2C%20minimalistic%20illustration%20of%20urban%20bike-sharing%20in%20Montreal.%20The%20design%20includes%20a%20simple%20bicycle%20next%20to%20a%20modern%20urban%20bike%20rac.webp" width="700" height="400">

---

## Contents

- [1. Overview](#overview)
- [2. Project Goals](#project-goals)
- [3. Project Features](#project-features)
- [4. Tools and Frameworks](#tools-and-frameworks)
- [5. Directory Structure](#directory-structure)
- [6. Reproducibility](#reproducibility)
- [7. How to Use the API](#api-usage)
- [8. Data Sources](#data-sources)

---

## 1. Overview <a name="overview"></a>

The **BikeML-API** explores the relationship between weather conditions and bike-sharing usage in Montreal. It includes a machine learning pipeline to predict trip durations based on weather and temporal features, as well as an API for serving predictions. The findings aim to help bike-sharing operators like BIXI optimize operations and user satisfaction.

---

## 2. Project Goals <a name="project-goals"></a>

The goals of this project are:
1. To analyze how weather conditions affect the duration of bike-sharing trips.
2. To build and deploy a machine learning model that predicts trip durations.
3. To provide actionable insights for bike-sharing companies to optimize bike availability.

---

## 3. Project Features <a name="project-features"></a>

- **Weather and Trip Data Integration**: Combining weather observations with BIXI trip data for comprehensive analysis.
- **Machine Learning Model**: A Random Forest model trained to predict trip durations.
- **API Deployment**: A Flask API for serving predictions based on user-input weather and temporal features.

---

## 4. Tools and Frameworks <a name="tools-and-frameworks"></a>

### Tools:
- **Python**: Data preprocessing, model training, and API development.
- **Jupyter Notebooks**: For exploratory data analysis (EDA) and feature engineering.

### Libraries:
- **Scikit-learn**: Model development and evaluation.
- **Flask**: Deployment of the prediction API.
- **Pandas/NumPy**: Data manipulation.
- **Matplotlib/Seaborn**: Visualization.

### Other Tools:
- **Git LFS**: For tracking large files in the repository.
- **Docker** (Optional): For containerizing the API.

---

## 5. Directory Structure <a name="directory-structure"></a>

```plaintext
BikeML-API/
│
├── data/
│   ├── bixi_data_2021.csv                      # BIXI bike-sharing trip data (Git LFS tracked)
│   ├── weather_data_2021.csv                   # Weather data for Montreal (Git LFS tracked)
│   ├── refined_combined_data_with_features.xls # Final processed dataset (Git LFS tracked)
│   └── ...
│
├── imgs/                                       # (Optional) Visualization images
│   └── ...
│
├── models/
│   ├── bike_duration_predictor.pkl             # Trained model for predictions
│   ├── tuned_random_forest.pkl                 # Tuned Random Forest model
│   └── ...
│
├── notebooks/
│   ├── BikeML01.ipynb                          # Data preprocessing and feature engineering
│   ├── BikeML02.ipynb                          # Model training and evaluation
│   └── ...
│
├── app.py                                      # Flask API script
├── predict_request.ps1                         # Script for making POST requests to the API
├── requirements.txt                            # Python dependencies
├── Dockerfile                                  # Dockerfile for containerization (optional)
└── README.md                                   # Project description and instructions

plaintext

```

---

## 6. Reproducibility <a name="reproducibility"></a>

### Steps to Reproduce:
1. Clone this repository:
   ```bash
   git clone https://github.com/AFARNOOD/BikeML-API.git
   cd BikeML-API

2. Set up Python dependencies:
   ```bash
   pip install -r requirements.txt

3. Download the required datasets or ensure they are placed in the `data/` directory.
4. Run the Jupyter Notebooks in the `notebooks/` directory to preprocess the data or retrain the model.


## 7. How to Use the API <a name="api-usage"></a>

To use the API for predictions, follow these steps:

1. **Run the Flask App**:
   Ensure the Flask API is running locally. Start the API by executing the following command in your terminal:

   ```bash
   python app.py
      ```

   The server will run on `http://127.0.0.1:5000`.

2. **Send a POST Request**:
   Use the provided `predict_request.ps1` script or your preferred tool (e.g., Postman, cURL) to send a request with input data for prediction. The input JSON must include the following features:

   ```json
   {
       "max_temp_c": 20,
       "min_temp_c": 7,
       "temp_range_c": 18,
       "total_precip_mm": 2,
       "snow_on_grnd_cm": 0,
       "spd_of_max_gust_kmh": 10,
       "is_rainy": 1,
       "is_snowy": 0,
       "is_windy": 0,
       "start_hour": 9,
       "start_weekday": 1,
       "is_weekend": 0
   }
   ```
   
3. **Example PowerShell Command**:
   Run the following command in PowerShell to send the prediction request:

   ```powershell
   Invoke-RestMethod -Uri http://127.0.0.1:5000/predict `
       -Method POST `
       -ContentType "application/json" `
       -Body '{"max_temp_c": 20, "min_temp_c": 7, "temp_range_c": 18, "total_precip_mm": 2, "snow_on_grnd_cm": 0, "spd_of_max_gust_kmh": 10, "is_rainy": 1, "is_snowy": 0, "is_windy": 0, "start_hour": 9, "start_weekday": 1, "is_weekend": 0}'
   ```

4. **Example cURL Command**:
   If you prefer using cURL, run this command in your terminal:

   ```powershell
   curl -X POST http://127.0.0.1:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"max_temp_c": 20, "min_temp_c": 7, "temp_range_c": 18, "total_precip_mm": 2, "snow_on_grnd_cm": 0, "spd_of_max_gust_kmh": 10, "is_rainy": 1, "is_snowy": 0, "is_windy": 0, "start_hour": 9, "start_weekday": 1, "is_weekend": 0}'

   ```

5. **Expected Output**:
   The API will respond with the predicted trip duration in seconds. Example response:

   ```powershell
   {
    "predicted_duration_sec": 789
   }
   ```


> **Note**: For other tools or environments, ensure the JSON request body matches the required format and is sent as a POST request to the `/predict` endpoint.

---

## 8. Data Sources <a name="data-sources"></a>

This project uses two primary datasets:

1. **Weather Data**:
   - Source: Environment and Climate Change Canada (ECCC).
   - Description: Includes daily and hourly weather data for Montreal in 2021.
   - Features: Temperature, precipitation, wind speed, and other climatic conditions.

   [Download Weather Data](https://climate.weather.gc.ca/)

2. **BIXI Data**:
   - Source: BIXI Montreal Open Data Portal.
   - Description: Contains detailed trip records of BIXI bike-sharing users for 2021.
   - Features: Trip start and end times, station locations, and duration.

   [Download BIXI Data](https://bixi.com/en/open-data)

