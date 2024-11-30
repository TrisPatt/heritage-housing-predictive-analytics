import streamlit as st


def conclusion_body():
    """Conclusion."""
    st.write("## **Conclusion**")

    st.write("---")

    st.success(
        "### **Conclusions and considerations**  \n"
        "The client outlined two key business requirements, both of which have "
        "been successfully addressed through this application:   \n\n"
        "**Correlation Study:**  \n "
        "The correlation analysis identified the features most strongly correlated "
        "with the target variable, Sale Price. "
        "This study provided valuable insights into which attributes significantly "
        "influence property values, aiding the client in understanding key "
        "drivers of sale prices.  \n\n"
        "**Predict Sale Price Module:**  \n"
        "The prediction module showcased the sale prices of the client’s four inherited "
        "houses, along with their total combined value.  \n"
        "A dynamic feature selection interface allows the client to input specific property "
        "attributes and predict sale prices for any house in Ames, Iowa. "
        "The client set a target R² score of 0.75 for the model's predictive performance. "
        "This target was exceeded, as demonstrated in the technical analyses summary, "
        "showcasing the model’s accuracy and reliability.  \n\n"
        "**Hypotheses Validation:**  \n"
        "The hypotheses formulated at the start of the project were tested and proven, "
        "confirming the relationships between certain features and sale price. For example: "
        "Overall Quality and Living Area were shown to have the highest correlations with "
        "sale price.  \n\n"
        "**Additional Considerations:**  \n"
        "Some impactful features, such as neighborhood area, were not included in the dataset. "
        "While neighborhood desirability is a significant factor in determining sale "
        "price, its inclusion would require subjective evaluation and external data, "
        "making it challenging to quantify and integrate into the model.  \n\n"
        "**Conclusion:**  \n"
        "This application provides the client with a robust tool to explore correlations, "
        "predict sale prices, and make data-driven decisions regarding property sales. "
        "The successful delivery of both business requirements demonstrates the value of "
        "leveraging machine learning for real estate analytics."
    )
