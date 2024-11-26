import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from src.data_management import load_pkl_file
from src.machine_learning.evaluate import regression_performance, regression_evaluation_plots

def technical_analysis_body():
    """Technical analysis for regression model."""
    st.write("## **Technical Analysis**")

    version = 'v2'
    price_pipeline = load_pkl_file(
        f'outputs/ml_pipeline/predict_SalePrice/{version}/best_regressor_pipeline.pkl'
    )
    
    price_features = pd.read_csv(
        f"outputs/ml_pipeline/predict_SalePrice/{version}/X_train.csv"
    ).columns.to_list()

    # Load feature importance visualization
    feat_importance_path = f"outputs/ml_pipeline/predict_SalePrice/{version}/features_importance.png"
    feat_importance = plt.imread(feat_importance_path)

    # Load train/test data
    X_train = pd.read_csv(f"outputs/ml_pipeline/predict_SalePrice/{version}/X_train.csv")
    X_test = pd.read_csv(f"outputs/ml_pipeline/predict_SalePrice/{version}/X_test.csv")
    y_train = pd.read_csv(f"outputs/ml_pipeline/predict_SalePrice/{version}/y_train.csv").squeeze()
    y_test = pd.read_csv(f"outputs/ml_pipeline/predict_SalePrice/{version}/y_test.csv").squeeze()

    # Display Feature Importance
    st.write("### Feature Importance")
    st.image(feat_importance, caption="Feature Importance", use_column_width=True)

    # Display Regression Performance
    st.write("### Model Performance")
    regression_performance(X_train, y_train, X_test, y_test, price_pipeline)

    # Display Evaluation Plots
    st.write("### Evaluation Plots")
    regression_evaluation_plots(X_train, y_train, X_test, y_test, price_pipeline)
