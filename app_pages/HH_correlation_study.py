import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import matplotlib.ticker as mtick
from src.data_management import load_house_prices_records

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")


def HH_correlation_study_body():
    # Load data
    df = load_house_prices_records()

    vars_to_study = [
        'OverallQual', 'GrLivArea', 'GarageArea',
        'TotalBsmtSF', 'YearBuilt', '1stFlrSF'
    ]

    st.write("### Heritage Housing Correlation Study")
    st.info(
        "* The client is interested in discovering how the house attributes "
        "correlate with the sale price. Therefore, the client expects data "
        "visualisations of the correlated variables against the sale price "
        "to show that. Click below to inspect the data."
    )

    # Inspect data
    if st.checkbox("Inspect dataset"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns. "
            "Find below the first 10 rows:"
        )
        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        "* A correlation study was conducted in the notebook to better understand "
        "how the variables are correlated to the sale price. \n"
        "The most correlated variables are: **{vars_to_study}**"
    )

    # From correlation study notebook
    st.info(
        "**Analysis Summary**  \n"
        "* The analysis indicates that the overall build quality of a property "
        "(OverallQual) exhibits the strongest correlation with the Sale Price "
        "(SalePrice). This relationship is clearly illustrated in the box plot "
        "and is further supported by the highest correlation coefficients "
        "observed in both the Pearson and Spearman correlation methods.  \n\n"
        "* The variables ground living area (GrLivArea), 1st floor square footage "
        "(1stFlrSF), total basement area (TotalBsmtSF), and garage area "
        "(GarageArea) also show significant correlations with Sale Price. "
        "The accompanying scatterplots demonstrate positive linear regression "
        "lines, suggesting that these features play a substantial role in "
        "determining the sale price of a property.  \n\n"
        "* The year built (YearBuilt) has positive correlation also, so it "
        "should not be overlooked."
    )

    st.info(
        "The following scatterplots show the correlation between each selected "
        "variable and the sale price. Click below to see the scatterplots."
    )

    # Filter the DataFrame for EDA
    df_eda = df.filter(vars_to_study + ['SalePrice'])

    # Add PriceCategory for additional analysis
    df_eda['PriceCategory'] = pd.qcut(
        df_eda['SalePrice'], q=3, labels=['Low', 'Medium', 'High']
    )

    # Generate and display plots
    if st.checkbox("Scatter plots"):
        st.write(scatter_plots(df_eda))

    st.write("---")

    st.info(
        "The following box plot displays the median and quartile ranges of SalePrice "
        "across different quality levels, highlighting the spread of values within "
        "each quality rating. Click below to view box plot."
    )

    if st.checkbox("Box plot"):
        st.write(box_plot(df_eda))


def scatter_plots(df_eda):
    # Create subplots
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()

    for i, var in enumerate([
        'OverallQual', 'GrLivArea', 'GarageArea', 'TotalBsmtSF',
        'YearBuilt', '1stFlrSF'
    ]):
        sns.regplot(
            data=df_eda,
            x=var,
            y='SalePrice',
            scatter_kws={'s': 10},
            line_kws={"color": "red"},
            ax=axes[i]
        )
        axes[i].set_title(f'SalePrice vs {var}')
        axes[i].set_xlabel(var)
        axes[i].set_ylabel('SalePrice')
        axes[i].yaxis.set_major_formatter(
            mtick.FuncFormatter(lambda x, _: f'{int(x/1000)}k')
        )

    # Adjust layout and display in Streamlit
    plt.tight_layout()
    st.pyplot(fig)


def box_plot(df_eda):
    # Create box plot for overall Quality
    plt.figure(figsize=(8, 6))
    sns.boxplot(
        data=df_eda, x='OverallQual', y='SalePrice', palette='viridis'
    )
    plt.title('SalePrice vs OverallQual')
    plt.xlabel('OverallQual')
    plt.ylabel('SalePrice')
    st.pyplot(plt)
