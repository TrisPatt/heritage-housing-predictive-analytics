import streamlit as st

def hypothesis_body():
    """ Hypothesis and validation"""
    st.write("Project Hypothesis and Validation")

    st.info(
        "**Hypothesis**  \n"
        "I would generally hypothesize that more expensive homes are likely to feature larger living spaces situated on " 
        "expansive lots in highly desirable neighborhoods. Additionally, homes with superior build quality and "
        "amenities, such as spacious garages or finished basements, are expected to command higher sale prices.  \n"
        "For this particular study, based on the available features in the dataset, I anticipate that factors such "
        "as ground living area, first-floor and second-floor living spaces, basement area, garage size, lot size "
        "and overall quality will have the most significant impact on sale price. While the dataset does not "
        "include explicit information about neighborhood characteristics, it is worth noting that "
        "neighborhood desirability is a complex factor to quantify and validate, often requiring subjective or external data inputs."
    )
    st.success(
        "**Validation**  \n"
        "The correlation study confirmed that overall quality, ground living area, first-floor living space, "
        "basement size, and garage area exhibited the strongest correlations with sale price. Additionally, the " 
        "year built demonstrated a significant positive correlation, indicating that newer homes tend to "
        "command higher prices.  \n"
        "Through careful analysis in the modelling and evaluation stage, including identifying key relationships and testing various "
        "methods and alghorithms, the data suggests that overall quality, basement area, garage area, and living spaces on "
        "the ground and second floors are the most important factors in predicting sale price."
    )
    