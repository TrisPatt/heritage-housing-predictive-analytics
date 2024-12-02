import streamlit as st


def project_summary_body():
    """ Project Summary contents"""
    
    st.write("## **Project Summary**")

    st.write("---")
    st.info(
        "### **Summary**  \n"
        "The objective of this project is to develop a machine learning "
        "application capable of predicting property values based on a provided dataset "
        "and its associated features. The client has inherited 4 houses in Ames, Iowa. "
        "The client would like to determine the value of these properties and other "
        "properties in the Ames area. The business requirements are shown below."
    )

    st.write("---")
    st.info(
        "### **Dataset**  \n"
        f"** The dataset represents housing records from Ames, Iowa.**  \n"
        f"It details house profile (Floor Area, Basement, Garage, Kitchen, "
        f"Lot, Porch, Wood Deck and Year Built) and its respective sale price "
        f"for houses built between 1872 and 2010.  \n"
        f"The dataset has almost 1.5 thousand rows.")
    
    st.write("---")
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/TrisPatt/heritage-housing-predictive-analytics)."
        )

    st.write("---") 
    st.success(
        "### **Business Requirements**  \n"
        "The project has 2 business requirements:  \n\n"
        "1. The client is interested in discovering how the house "
        "attributes correlate to the sale price. Therefore, the client "
        "expects data visualisations of the correlated "
        "variables against the sale price to show that.  \n"
        "2. The client is interested in predicting the house sale price "
        "from her four inherited houses and any other house in Ames, Iowa. ")
