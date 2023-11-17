import streamlit as st
import requests

def taxifare_predict(pickup_datetime, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count):
    url = "https://taxifare.lewagon.ai/predict"
    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }
    response = requests.get(url, params=params)
    return response.json()



def front_end():
    st.title("Taxi Fare Prediction App")

    # Input the prediction
    pickup_datetime = st.text_input("Pickup Datetime (YYYY-MM-DD HH:mm:ss)", value = "2013-07-06 17:18:00")
    pickup_longitude = st.number_input("Pickup Longitude", value=-73.950655)
    pickup_latitude = st.number_input("Pickup Latitude", value=40.783282)
    dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.984365)
    dropoff_latitude = st.number_input("Dropoff Latitude", value=40.769802)
    passenger_count = st.number_input("Passenger Count", value=1)

    # Button to calculate prediction
    if st.button("calculate"):
        prediction = taxifare_predict(pickup_datetime, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count)
        st.success(f"Predicted Fare: {prediction}")

if __name__ == "__main__":
    front_end()
