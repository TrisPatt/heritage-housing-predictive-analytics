import streamlit as st


def hypothesis_body():
    """ Hypotheses and validation"""
    st.write("## **Project Hypotheses and Validation** \n\n")
    st.write("---")
    st.success(

        f"**Hypothesis 1: Living Space and Sale Price**  \n"
        f"The amount of living space significantly impacts sale price. Larger "
        f"living areas on the ground floor, first floor, and second floor "
        f"will correlate with higher property values. \n\n"
        f"**Validation:**\n"
        f"Both Pearson and Spearman correlation methods revealed high "
        f"correlations between ground living area and sale price, with "
        f"ground living area ranking second only to overall quality in terms "
        f"of influence.\n"
        f"Scatterplots displayed steep positive regression lines for ground "
        f"living area and first floor square footage, providing robust visual "
        f"evidence supporting the hypothesis.  \n"
        f"**Conclusion: **"
        f"The hypothesis that living space significantly affects sale price "
        f"is strongly supported by statistical and visual analyses, "
        f"highlighting the importance of these features in determining "
        f"property value."
    )
    st.write("---")
    st.success(

        f"**Hypothesis 2: Amenities and Sale Price**  \n"
        f"The presence and size of amenities, such as garages and basements, "
        f"positively influence sale price. Properties with larger, "
        f"well-finished amenities are expected to command higher values.\n\n"
        f"**Validation:**\n"
        f"Both total basement square footage and garage area ranked among "
        f"the top five features based on Pearson and Spearman correlation "
        f"methods, indicating strong relationships with sale price. "
        f"The scatterplot for total basement square footage showed a steep "
        f"positive regression line, with data points forming a relatively "
        f"tight cluster. his pattern highlights a strong correlation with "
        f"sale price. The scatterplot for garage area exhibited a steady "
        f"positive regression line, further supporting the hypothesis that "
        f"garage size influences property value.  \n"
        f"**Conclusion:**  "
        f"The validation results support the hypothesis that amenities, "
        f"particularly garages and basements, significantly impact sale "
        f"price. These features play a critical role in "
        f"determining property value."
    )
    st.write("---")
    st.success(

        f"**Hypothesis 3: Build Quality and Sale Price**  \n"
        f"The quality of a property’s construction directly impacts its "
        f"value, with higher-quality builds commanding higher sale "
        f"prices.\n\n"
        f"**Validation:** "
        f"Overall quality exhibited the highest correlation with sale price "
        f"among all features, as measured by Pearson and Spearman methods. "
        f"This underscores the critical role of build quality in determining "
        f"property value. "
        f"The box plot demonstrated a clear trend; Higher quality ratings "
        f"were associated with significantly higher sale prices. "
        f"The spread of values within each quality rating further highlighted "
        f"the importance of build quality, with top-tier properties showing "
        f"both higher median prices and a narrower range of sale prices. \n\n"
        f"**Conclusion:**  "
        f"The hypothesis that build quality has a substantial impact on sale"
        f"price is strongly supported by the analysis. Both statistical "
        f"methods and visualizations confirm that higher build quality "
        f"consistently correlates with higher property value."

    )
    st.write("---")
    st.success(

        f"**Hypothesis 4: Property Age and Sale Price**  \n"
        f"Newer properties tend to attract higher sale prices, reflecting a "
        f"preference for newer construction.\n\n"
        f"**Validation:** "
        f"The scatterplot for Year Built showed a positive, steady "
        f"correlation with sale price. While the correlation was not as "
        f"steep as observed for other features, the data formed a strong "
        f"linear cluster, suggesting a significant relationship. "
        f"Even outliers followed the general trend, with much newer houses "
        f"corresponding to notably higher sale prices. "
        f"The Spearman method ranked Year Built as the 4th highest feature "
        f"correlated with sale price, highlighting its importance. "
        f"The Pearson method placed Year Built among the top 7 features "
        f" out of 22, further supporting its influence. \n\n"
        f"**Conclusion:**  "
        f"The hypothesis that newer properties attract higher sale prices is "
        f"supported by both statistical and visual analyses. While the "
        f"correlation is not as strong as some other features, the results "
        f"demonstrate a clear trend, emphasizing the value of modern "
        f"construction in the housing market"
    )
    st.write("---")
    st.info(
        f"**Additional factors/ Limitations**  \n\n"
        f"I acknowledge that neighbourhood area is not included in this "
        f"dataset. I hypothesise that neighbourhood characteristics play a "
        f"significant role in determining sale price and should be "
        f"considered as an important factor by the client alongside the "
        f"results provided in this report. "
        f"It is important to note, however, that measuring neighbourhood "
        f"desirability can be a complex task. This factor often requires "
        f"subjective judgment or external data inputs, "
        f"such as socio-economic indicators, proximity to amenities, or crime "
        f"rates, which are not readily available in the current dataset. "
        f"As such, the absence of this variable may limit the "
        f"comprehensiveness of the analysis. "
        f"Future studies could incorporate external data sources or proxy "
        f"variables to better account for the influence of neighbourhood on "
        f"property values."
    )
