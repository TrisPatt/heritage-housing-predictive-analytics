import streamlit as st
import pandas as pd


def predict_sale_price(X_live, price_features, price_pipeline):
    """
    Predict the house sale price using the input features and regression
    pipeline.

    """
    # Filter input data to include only relevant features
    X_live_filtered = X_live.filter(price_features)

    # Predict sale price
    sale_price_prediction = price_pipeline.predict(X_live_filtered)

    # Display results
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

    # Filter features for inherited houses
    inherited_houses_filtered = inherited_houses[price_features]

    if "TotalBsmtSF" in inherited_houses_filtered.columns:
        inherited_houses_filtered["TotalBsmtSF"] = inherited_houses_filtered["TotalBsmtSF"].astype(int)

    if "GarageArea" in inherited_houses_filtered.columns:
        inherited_houses_filtered["GarageArea"] = inherited_houses_filtered["GarageArea"].astype(int)


    # Predict sale prices
    predictions = price_pipeline.predict(inherited_houses_filtered)

    # Create a DataFrame to display features and predictions
    results_df = inherited_houses_filtered.copy()
    results_df['Predicted Sale Price'] = predictions

    # Display the DataFrame in Streamlit
    st.dataframe(results_df)

    # Show a summary of total price
    total_price = predictions.sum()
    st.info(
        f"### Total Predicted Sale Price for All Inherited Houses: "
        f"**${total_price:,.2f}**"
    )
