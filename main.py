import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.project_summary import project_summary_body
from app_pages.HH_correlation_study import HH_correlation_study_body
from app_pages.predict_sale_price import predict_sale_price_body
from app_pages.hypothesis import hypothesis_body
from app_pages.technical_analysis import technical_analysis_body
from app_pages.conclusion import conclusion_body

# Create an instance
app = MultiPage(app_name="Heritage Housing- Predict Sale price")

app.app_page("Project Summary", project_summary_body)
app.app_page("Project Hypotheses and Validation", hypothesis_body)
app.app_page("Correlation Study", HH_correlation_study_body)
app.app_page("ML- Predict Sale Price", predict_sale_price_body)
app.app_page("ML pipeline and Technical Analysis", technical_analysis_body)
app.app_page("Conclusion", conclusion_body)

app.run()