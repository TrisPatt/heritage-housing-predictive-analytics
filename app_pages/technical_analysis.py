import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from src.data_management import load_pkl_file
from src.machine_learning.evaluate import (regression_performance,
                                           regression_evaluation_plots)


def technical_analysis_body():
    """
    Perform and Display Technical Analysis of the Regression Model's
    Performance.

    - Load and display the final machine learning pipeline used for training.
    - Evaluate the model using R² score, Mean Absolute Error (MAE), Mean
    Squared Error (MSE), and Root Mean Squared Error (RMSE) on both training
    and test sets.
    - Provide a visual summary of model evaluation through scatterplots of
    actual vs predicted values.
    - Highlight the importance of features in influencing the sale price
    predictions using a feature importance bar chart.

    """

    st.write("## **Technical Analysis- Model Performance**")

    st.write("---")

    version = 'v2'
    price_pipeline = load_pkl_file(
        f'outputs/ml_pipeline/predict_SalePrice/{version}/'
        'best_regressor_pipeline.pkl'
    )

    price_features = pd.read_csv(
        f"outputs/ml_pipeline/predict_SalePrice/{version}/X_train.csv"
    ).columns.to_list()

    feat_importance_path = (
        f"outputs/ml_pipeline/predict_SalePrice/{version}/features_importance.png"
    )
    feat_importance = plt.imread(feat_importance_path)

    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_SalePrice/{version}/X_train.csv"
    )
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_SalePrice/{version}/X_test.csv"
    )
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_SalePrice/{version}/y_train.csv"
    ).squeeze()
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_SalePrice/{version}/y_test.csv"
    ).squeeze()

    st.info(f"The final pipeline used to train the model was as follows:  \n")
    st.image("assets/imgs/pipeline_steps.jpg",
             caption="Pipeline steps", use_column_width=True)

    st.write("---")
    st.write("### Model Performance")
    st.success(
        f"* The target model performance was 0.75 for both train and test "
        f"sets.  \n"
        f"* The model exceeded the target as shown below."
    )

    regression_performance(X_train, y_train, X_test, y_test, price_pipeline)

    st.success(
        "The model explains 92.2% of the variance in the target variable "
        "within the training data, and 82.2% of variance on unseen test "
        "data.  \n"
        "On average, the model's predictions deviate by approximately $14,050 "
        "from the actual values on train set and approximately $20,224 from "
        "the actual values in the test set.  \n"
        ""
    )

    st.write("### Evaluation Plots")

    st.write(
        "The following evaluation scatterplots illustrate the relationship "
        "between actual and predicted values for the train and test sets. "
        "The clustering of points near the regression line demonstrates "
        "the model's accuracy and strong predictive performance."
    )

    regression_evaluation_plots(X_train, y_train, X_test,
                                y_test, price_pipeline)

    st.write("---")

    st.write("### Feature Importance")

    st.write(
        "The following bar chart highlights the importance of each selected "
        "feature in relation to its correlation with the sale price. "
    )

    st.image(feat_importance, caption="Feature Importance",
             use_column_width=True)
