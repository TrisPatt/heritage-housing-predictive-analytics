import streamlit as st


def project_summary_body():
    """ Project Summary contents"""
    st.write("## **Project Summary**")

    # text based on README file - "Dataset Content" section
    st.info(
        "### **Dataset**  \n"
        f"** The dataset represents housing records from Ames, Iowa.**  \n"
        f"It details house profile (Floor Area, Basement, Garage, Kitchen, "
        f"Lot, Porch, Wood Deck and Year Built) and its respective sale price "
        f"for houses built between 1872 and 2010.  \n"
        f"The dataset has almost 1.5 thousand rows.")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file]("
        f"/workspace/heritage-housing-predictive-analytics/README.md)."
        )

    # copied from README file - "Business Requirements" section
    st.success(
        "### **Business Requirements**  \n"
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in discovering how the house "
        f"attributes correlate to the sale price. Therefore, the client "
        f"expects data visualisations of the correlated "
        f"variables against the sale price to show that.\n"
        f"* 2 - The client is interested in predicting the house sale price "
        f"from her four inherited houses and any other house in Ames, Iowa. ")
