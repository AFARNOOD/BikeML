# Save this as "predict_request.ps1"

# Define the API endpoint
$api_url = "http://127.0.0.1:5000/predict"

# Define the request body (adjust the values if needed)
$request_body = @{
    max_temp_c = 20
    min_temp_c = 7
    temp_range_c = 18
    total_precip_mm = 2
    snow_on_grnd_cm = 0
    spd_of_max_gust_kmh = 10
    is_rainy = 1
    is_snowy = 0
    is_windy = 0
    start_hour = 9
    start_weekday = 1
    is_weekend = 0
} | ConvertTo-Json -Depth 1

# Send the POST request to the API
$response = Invoke-RestMethod -Uri $api_url -Method POST -ContentType "application/json" -Body $request_body

# Display the prediction
Write-Output "Predicted Trip Duration:"
Write-Output $response
