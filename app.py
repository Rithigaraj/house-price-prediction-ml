import streamlit as st
import numpy as np
import joblib

# Load trained models
regression_model = joblib.load("house_price_regression_model.pkl")
classification_model = joblib.load("house_price_classification_model.pkl")


# Page settings
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# Title
st.title("🏠 House Price Prediction")
st.write("Enter the house details below to predict its price.")


# Input fields
st.subheader("House Details")

MedInc = st.number_input(
    "Median Income",
    min_value=0.0,
    value=5.0
)

HouseAge = st.number_input(
    "House Age",
    min_value=0.0,
    value=20.0
)

AveRooms = st.number_input(
    "Average Rooms",
    min_value=0.0,
    value=6.0
)

AveBedrms = st.number_input(
    "Average Bedrooms",
    min_value=0.0,
    value=1.0
)

Population = st.number_input(
    "Population",
    min_value=0.0,
    value=1000.0
)

AveOccup = st.number_input(
    "Average Occupancy",
    min_value=0.0,
    value=3.0
)

Latitude = st.number_input(
    "Latitude",
    value=34.05
)

Longitude = st.number_input(
    "Longitude",
    value=-118.25
)


# Prediction button
if st.button("🔮 Predict House Price"):

    # Create input array
    data = np.array([[
        MedInc,
        HouseAge,
        AveRooms,
        AveBedrms,
        Population,
        AveOccup,
        Latitude,
        Longitude
    ]])

    # Make predictions
    predicted_price = regression_model.predict(data)[0]
    predicted_category = classification_model.predict(data)[0]

    # Convert price to dollars
    price_in_dollars = predicted_price * 100000

    if predicted_category == 1:
        category = "High Price"
    else:
        category = "Low Price"

    # Display results
    st.success("Prediction completed!")

    st.subheader("Prediction Result")

    st.metric(
        "Predicted House Price",
        f"${price_in_dollars:,.2f}"
    )

    st.metric(
        "Price Category",
        category
    )