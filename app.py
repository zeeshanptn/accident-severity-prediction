import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("accident_severity_model_final_compressed.pkl")

st.title("🚗 Accident Severity Prediction")

st.write(
    "This application predicts accident severity using "
    "weather, location, time, and road-related features."
)
st.header("Accident Details")

start_lat = st.number_input("Latitude", value=40.0)
start_lng = st.number_input("Longitude", value=-75.0)

distance = st.number_input("Distance (miles)", value=0.1)
temperature = st.number_input("Temperature (°F)", value=65.0)
humidity = st.number_input("Humidity (%)", value=60.0)
pressure = st.number_input("Pressure (in)", value=30.0)
visibility = st.number_input("Visibility (miles)", value=10.0)
wind_speed = st.number_input("Wind Speed (mph)", value=8.0)

duration = st.number_input("Accident Duration (minutes)", value=30.0)
hour = st.slider("Hour of Day", 0, 23, 12)

traffic_signal = st.checkbox("Traffic Signal")
crossing = st.checkbox("Crossing")
stop = st.checkbox("Stop")
junction = st.checkbox("Junction")
state = st.selectbox(
    "State",
    ["CA", "OH", "WV"]
)

weather = st.selectbox(
    "Weather Condition",
    ["Clear", "Overcast", "Mostly Cloudy", "Partly Cloudy", "Scattered Clouds", "Light Rain", "Haze", "Rain", "Heavy Rain", "Fog"]
)

day = st.selectbox(
    "Day",
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
)

wind_direction = st.selectbox(
    "Wind Direction",
    ["CALM", "N", "NE", "E", "SE", "S", "SW", "W", "NW"]
)
# Create input dataframe
input_data = pd.DataFrame({
    "Start_Lat": [start_lat],
    "Start_Lng": [start_lng],
    "Distance(mi)": [distance],
    "Temperature(F)": [temperature],
    "Humidity(%)": [humidity],
    "Pressure(in)": [pressure],
    "Visibility(mi)": [visibility],
    "Wind_Speed(mph)": [wind_speed],
    "Duration_min": [duration],
    "Hour": [hour],

    "Traffic_Signal": [traffic_signal],
    "Crossing": [crossing],
    "Stop": [stop],
    "Junction": [junction],

    "State": [state],
    "Weather_Condition": [weather],
    "Day": [day],
    "Wind_Direction": [wind_direction],

    "Station": [False],
    "Sunrise_Sunset": ["Day"],
    "No_Exit": [False],
    "Turning_Loop": [False],
    "Amenity": [False],
    "Timezone": ["US/Eastern"],
    "Traffic_Calming": [False],
    "Civil_Twilight": ["Day"],
    "Astronomical_Twilight": ["Day"],
    "Nautical_Twilight": ["Day"],
    "Source": ["MapQuest"],
    "Roundabout": [False],
    "Give_Way": [False],
    "Railway": [False],
    "Bump": [False]
})

st.write("Input data:")
st.dataframe(input_data)
if st.button("Predict Accident Severity"):

    prediction = model.predict(input_data)

    st.success(f"Predicted Accident Severity: {prediction[0]}")
