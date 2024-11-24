import streamlit as st


def project_summary_body():
    """ Project Summary contents"""
    st.write("## **Project Summary**")

    # text based on README file - "Dataset Content" section
    st.info(
        "### **Dataset**  \n"
        "** The dataset represents housing records from Ames, Iowa.**  \n"
        "It details house profile (Floor Area, Basement, Garage, Kitchen, Lot, "
        "Porch, Wood Deck and Year Built) and its respective sale price for houses  "
        "built between 1872 and 2010.  \n"
        "The dataset has almost 1.5 thousand rows.")


    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](/workspace/heritage-housing-predictive-analytics/README.md).")
    

    # copied from README file - "Business Requirements" section
    st.success(
        "### **Business Requirements**  \n"
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in discovering how the house attributes correlate "
        f"to the sale price. Therefore, the client expects data visualisations of the correlated "
        f"variables against the sale price to show that.\n"
        f"* 2 - The client is interested in predicting the house sale price from her "
        f"four inherited houses and any other house in Ames, Iowa. ")