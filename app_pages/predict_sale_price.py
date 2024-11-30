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
        f"*TotalBsmtSF*- Total basement square footage. Values are 0 - 6110  \n"
        f"*GarageArea*- Garage area measured in square feet. values are 0 - 1418  \n"
        f"*GrLivArea*- Ground Living area measured in square feet. Values are "
        f"334 - 5642.  \n"
        f"*YearBuilt*- Original construction date. Values are 1872 - 2010. "

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

    col1, col2, col3, col4 = st.beta_columns(4)
    col5, col6, col7, col8 = st.beta_columns(4)

    X_live = pd.DataFrame([], index=[0])

    # Feature: Overall Quality
    with col1:
        feature = "OverallQual"
        st_widget = st.number_input(
            label=feature,
            min_value=int(df[feature].min() * percentageMin),
            max_value=int(df[feature].max() * percentageMax),
            value=int(df[feature].median()),
        )
        X_live[feature] = st_widget

    # Feature: Total Basement Square Footage
    with col2:
        feature = "TotalBsmtSF"
        st_widget = st.number_input(
            label=feature,
            min_value=int(df[feature].min() * percentageMin),
            max_value=int(df[feature].max() * percentageMax),
            value=int(df[feature].median()),
            step=1,  
            format="%d"
        )
        X_live[feature] = int(st_widget) 

    # Feature: Garage Area
    with col3:
        feature = "GarageArea"
        st_widget = st.number_input(
        label=feature,
        min_value=int(df[feature].min() * percentageMin),
        max_value=int(df[feature].max() * percentageMax),
        value=int(df[feature].median()),
        step=1,  
        format="%d"  
        )
        X_live[feature] = int(st_widget)

    # Feature: Ground Living Area
    with col4:
        feature = "GrLivArea"
        st_widget = st.number_input(
            label=feature,
            min_value=int(df[feature].min() * percentageMin),
            max_value=int(df[feature].max() * percentageMax),
            value=int(df[feature].median()),
        )
        X_live[feature] = st_widget

    # Feature: Year Built
    with col5:
        feature = "YearBuilt"
        st_widget = st.number_input(
            label=feature,
            min_value=int(df[feature].min() * percentageMin),
            max_value=int(df[feature].max() * percentageMax),
            value=int(df[feature].median()),
        )
        X_live[feature] = st_widget

    st.write("### Input Features for Prediction: ")
    st.dataframe(X_live)

    return X_live
