import streamlit as st
import pandas as pd
import numpy as np
from src.data_management import (
    load_house_prices_records,
    load_inherited_houses,
    load_pkl_file,
)
from src.machine_learning.predictive_analysis_ui import (
    predict_sale_price,
    predict_inherited_houses,
)


def predict_sale_price_body():
    """Predict sale price contents."""

    st.title("House Price Prediction Interface")
    st.write("---")
    st.write("## **Predict Sale Price**")

    # Load model and features
    version = 'v2'
    file_path = (
        f"outputs/ml_pipeline/predict_SalePrice/{version}/"
        "best_regressor_pipeline.pkl"
    )
    price_pipeline = load_pkl_file(file_path)

    price_features = (
        pd.read_csv(
            f"outputs/ml_pipeline/predict_SalePrice/{version}/X_train.csv"
            )
        .columns
        .to_list()
    )

    st.info(
        f"The client is interested in predicting the house sale price for "
        f"her four inherited houses and any other house in Ames, Iowa.  \n"
        f"The features below are the most highly correlated features in "
        f"relation to sale price. Enter values for each specific feature and "
        f"click predict sale price to see the predicted value for the "
        f"property."
    )
    st.info(
        f"**Key**  \n"
        f"*Overall Quality*- values from 1-10, where 1 is very poor and "
        f"10 is very excellent.  \n"
        f"*TotalBsmtSF*- Total basement square footage. Values are 0 - 7000  \n"
        f"*GarageArea*- Garage area measured in square feet. values are 0 - 1800  \n"
        f"*GrLivArea*- Ground Living area measured in square feet. Values are "
        f"300 - 6000.  \n"
        f"*YearBuilt*- Original construction date. Values are 1800 - 2025. "

    )
    st.write("---")

    # Generate Live Data
    X_live = DrawInputsWidgets()

    # Predict single house sale price
    if st.button("Predict Sale Price for Single House"):
        predict_sale_price(X_live, price_features, price_pipeline)

    st.write("---")

    st.info(
        "Click below to see the predicted value of each of the 4 "
        "inherited houses:"
    )

    # Predict inherited houses sale price
    st.write("### Predict Prices for Inherited Houses")
    if st.checkbox("Predict for Inherited Houses"):
        inherited_houses = load_inherited_houses()
        predict_inherited_houses(
            inherited_houses, price_features, price_pipeline
            )


def DrawInputsWidgets():
    """Generate widgets to input live data."""
    df = load_house_prices_records()
    percentageMin, percentageMax = 0.4, 2.0

    feature_ranges = {
        "OverallQual": {"min": 1, "max": 10, "default": 5},
        "TotalBsmtSF": {"min": 0, "max": 7000, "default": 1000},
        "GarageArea": {"min": 0, "max": 1800, "default": 500},
        "GrLivArea": {"min": 300, "max": 6000, "default": 1500},
        "YearBuilt": {"min": 1800, "max": 2025, "default": 2000},
    }

    col1, col2, col3, col4 = st.beta_columns(4)
    col5, col6, col7, col8 = st.beta_columns(4)

    X_live = pd.DataFrame([], index=[0])

    with col1:
        feature = "OverallQual"
        st_widget = st.number_input(
            label=f"{feature} (1-10)",
            min_value=feature_ranges[feature]["min"],
            max_value=feature_ranges[feature]["max"],
            value=feature_ranges[feature]["default"],
            step=1,
        )
        X_live[feature] = st_widget

    with col2:
        feature = "TotalBsmtSF"
        st_widget = st.number_input(
            label=f"{feature} (sq ft)",
            min_value=feature_ranges[feature]["min"],
            max_value=feature_ranges[feature]["max"],
            value=feature_ranges[feature]["default"],
            step=10,  
            format="%d",
        )
        X_live[feature] = int(st_widget)

    with col3:
        feature = "GarageArea"
        st_widget = st.number_input(
            label=f"{feature} (sq ft)",
            min_value=feature_ranges[feature]["min"],
            max_value=feature_ranges[feature]["max"],
            value=feature_ranges[feature]["default"],
            step=10,  
            format="%d",
        )
        X_live[feature] = int(st_widget)

    with col4:
        feature = "GrLivArea"
        st_widget = st.number_input(
            label=f"{feature} (sq ft)",
            min_value=feature_ranges[feature]["min"],
            max_value=feature_ranges[feature]["max"],
            value=feature_ranges[feature]["default"],
            step=10,  
        )
        X_live[feature] = int(st_widget)

    with col5:
        feature = "YearBuilt"
        st_widget = st.number_input(
            label=f"{feature} (Year)",
            min_value=feature_ranges[feature]["min"],
            max_value=feature_ranges[feature]["max"],
            value=feature_ranges[feature]["default"],
            step=1,  
        )
        X_live[feature] = int(st_widget)

    st.write("### Input Features for Prediction: ")
    st.dataframe(X_live)

    return X_live