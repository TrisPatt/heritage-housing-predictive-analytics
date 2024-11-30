import streamlit as st


def hypothesis_body():
    """ Hypotheses and validation"""
    st.write("## **Project Hypotheses and Validation** \n\n")
    st.write("---")
    st.success(

        f"**Hypothesis 1: Living Space and Sale Price**  \n"
        f"The amount of living space significantly impacts sale price. Larger "
        f"living areas on the ground floor, first floor, and second floor will "
        f"correlate with higher property values. \n\n"
        f"**Validation:**\n"
        f"Both Pearson and Spearman correlation methods revealed high correlations "
        f"between ground living area and sale price, with ground living area "
        f"ranking second only to overall quality in terms of influence.\n"
        f"Scatterplots displayed steep positive regression lines for ground "
        f"living area and first floor square footage, providing robust visual "
        f"evidence supporting the hypothesis.  \n"
        f"**Conclusion: **"
        f"The hypothesis that living space significantly affects sale price is strongly "
        f"supported by statistical and visual analyses, highlighting the importance "
        f"of these features in determining property value."
    )
    st.write("---")
    st.success(

        f"**Hypothesis 2: Amenities and Sale Price**  \n"
        f"The presence and size of amenities, such as garages and basements, "
        f"positively influence sale price. Properties with larger, "
        f"well-finished amenities are expected to command higher values.\n\n"
        f"**Validation:**\n"
        f"Both total basement square footage and garage area ranked among the top "
        f"five features based on Pearson and Spearman correlation methods, "
        f"indicating strong relationships with sale price. "
        f"The scatterplot for total basement square footage showed a steep positive "
        f"regression line, with data points forming a relatively tight cluster. "
        f"his pattern highlights a strong correlation with sale price. "
        f"The scatterplot for garage area exhibited a steady positive regression line, "
        f"further supporting the hypothesis that garage size influences property value.  \n"
        f"**Conclusion:**  "
        f"The validation results support the hypothesis that amenities, particularly "
        f"garages and basements, significantly impact sale price. "
        f"These features play a critical role in "
        f"determining property value."
    )
    st.write("---")
    st.success(

        f"**Hypothesis 3: Build Quality and Sale Price**  \n"
        f"The quality of a property’s construction directly impacts its "
        f"value, with higher-quality builds commanding higher sale prices.\n\n"
        f"**Validation:** "
        f"Overall quality exhibited the highest correlation with sale price among "
        f"all features, as measured by Pearson and Spearman methods. "
        f"This underscores the critical role of build quality in determining "
        f"property value. "
        f"The box plot demonstrated a clear trend; Higher quality ratings were "
        f"associated with significantly higher sale prices. "
        f"The spread of values within each quality rating further highlighted the " 
        f"importance of build quality, with top-tier properties showing both higher "
        f"median prices and a narrower range of sale prices. \n\n"
        f"**Conclusion:**  "
        f"The hypothesis that build quality has a substantial impact on sale price is "
        f"strongly supported by the analysis. Both statistical methods and visualizations "
        f"confirm that higher build quality consistently correlates with higher "
        f"property value."
        
    )
    st.write("---")
    st.success(

        f"**Hypothesis 4: Property Age and Sale Price**  \n"
        f"Newer properties tend to attract higher sale prices, reflecting a "
        f"preference for newer construction.\n\n"
        f"**Validation:** "
        f"The scatterplot for Year Built showed a positive, steady correlation with "
        f"sale price. While the correlation was not as steep as observed for other "
        f"features, the data formed a strong linear cluster, suggesting a "
        f"significant relationship. "
        f"Even outliers followed the general trend, with much newer houses "
        f"corresponding to notably higher sale prices. "
        f"The Spearman method ranked Year Built as the 4th highest feature correlated "
        f"with sale price, highlighting its importance. "
        f"The Pearson method placed Year Built among the top 7 features "
        f" out of 22, further supporting its influence. \n\n"
        f"**Conclusion:**  "
        f"The hypothesis that newer properties attract higher sale prices is supported "
        f"by both statistical and visual analyses. While the correlation is not as "
        f"strong as some other features, the results demonstrate a clear trend, "
        f"emphasizing the value of modern construction in the housing market"
    )
    st.write("---")
    st.info(
        f"**Additional factors/ Limitations**  \n\n"
        f"I acknowledge that neighborhood area is not included in this "
        f"dataset. I hypothesize that neighborhood characteristics play a "
        f"significant role in determining sale price and should be "
        f"considered as an important factor by the client alongside the "
        f"results provided in this report. "
        f"It is important to note, however, that measuring neighborhood "
        f"desirability can be a complex task. This factor often requires "
        f"subjective judgment or external data inputs, "
        f"such as socio-economic indicators, proximity to amenities, or crime "
        f"rates, which are not readily available in the current dataset. "
        f"As such, the absence of this variable may limit the "
        f"comprehensiveness of the analysis. "
        f"Future studies could incorporate external data sources or proxy "
        f"variables to better account for the influence of neighborhood on "
        f"property values."
    )
