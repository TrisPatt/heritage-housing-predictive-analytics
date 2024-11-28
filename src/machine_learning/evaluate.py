import streamlit as st
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns


def regression_performance(
    X_train,
    y_train,
    X_test,
    y_test,
    best_regressor_pipeline
):

    # Predictions for train and test sets
    train_pred = best_regressor_pipeline.predict(X_train)
    test_pred = best_regressor_pipeline.predict(X_test)

    # Train set performance
    st.info("Train Set")
    st.write(f"R2 Score: {r2_score(y_train, train_pred):.3f}")
    st.write(
        f"Mean Absolute Error: {mean_absolute_error(y_train, train_pred):,.2f}"
    )
    st.write(
        f"Mean Squared Error: {mean_squared_error(y_train, train_pred):,.2f}"
    )
    st.write(
        "Root Mean Squared Error: "
        f"{mean_squared_error(y_train, train_pred, squared=False):,.2f}"
    )

    # Test set performance
    st.info("Test Set")
    st.write(f"R2 Score: {r2_score(y_test, test_pred):.3f}")
    st.write(
        f"Mean Absolute Error: {mean_absolute_error(y_test, test_pred):,.2f}"
    )
    st.write(
        f"Mean Squared Error: {mean_squared_error(y_test, test_pred):,.2f}"
    )
    st.write(
        "Root Mean Squared Error: "
        f"{mean_squared_error(y_test, test_pred, squared=False):,.2f}"
    )


# Regression evaluation plots
def regression_evaluation_plots(
    X_train,
    y_train,
    X_test,
    y_test,
    best_regressor_pipeline
):
    # Train predictions
    train_pred = best_regressor_pipeline.predict(X_train)
    test_pred = best_regressor_pipeline.predict(X_test)

    plt.figure(figsize=(15, 6))

    plt.subplot(1, 2, 1)
    sns.scatterplot(x=y_train, y=train_pred)
    plt.plot(
        [y_train.min(), y_train.max()],
        [y_train.min(), y_train.max()],
        'r--', lw=2
    )
    plt.title('Train Set: Actual vs Predicted')
    plt.xlabel('Actual')
    plt.ylabel('Predicted')

    plt.subplot(1, 2, 2)
    sns.scatterplot(x=y_test, y=test_pred)
    plt.plot(
        [y_test.min(), y_test.max()],
        [y_test.min(), y_test.max()],
        'r--', lw=2
    )
    plt.title('Test Set: Actual vs Predicted')
    plt.xlabel('Actual')
    plt.ylabel('Predicted')

    st.pyplot(plt)
