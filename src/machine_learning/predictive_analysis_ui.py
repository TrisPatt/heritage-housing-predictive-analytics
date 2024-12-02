import streamlit as st
import pandas as pd


def predict_sale_price(X_live, price_features, price_pipeline):
    """
    Predict the house sale price using the input features and regression
    pipeline.

    """

    X_live_filtered = X_live.filter(price_features)

    sale_price_prediction = price_pipeline.predict(X_live_filtered)

    st.write("### House Price Prediction")
    st.info(
        f"The predicted sale price for the input house is: "
        f"**${sale_price_prediction[0]:,.2f}**"
    )

    return sale_price_prediction


def predict_inherited_houses(inherited_houses, price_features, price_pipeline):
    """
    Predict sale prices for inherited houses and display features alongside
    predictions.

    """
    st.write("### Inherited Houses Features and Predicted Prices")

    inherited_houses_filtered = inherited_houses[price_features]

    if "TotalBsmtSF" in inherited_houses_filtered.columns:
        inherited_houses_filtered["TotalBsmtSF"] = (
            inherited_houses_filtered["TotalBsmtSF"].astype(int)
    )

    if "GarageArea" in inherited_houses_filtered.columns:
        inherited_houses_filtered["GarageArea"] = (
            inherited_houses_filtered["GarageArea"].astype(int)
    )

    predictions = price_pipeline.predict(inherited_houses_filtered)

    results_df = inherited_houses_filtered.copy()
    results_df['Predicted Sale Price'] = predictions

    st.dataframe(results_df)

    total_price = predictions.sum()
    st.info(
        f"### Total Predicted Sale Price for All Inherited Houses: "
        f"**${total_price:,.2f}**"
    )
