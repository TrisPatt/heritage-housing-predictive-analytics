# Predict Sale Price
<img width="946" alt="screenshot" src="assets/imgs/Screenshot 2024-11-27 164059.png">


Link to the project dashboard is [HERE](https://hh-predictive-analytics-p5-ab08303eeb0a.herokuapp.com/)

## Table of Contents
- [Introduction](#Introduction)
- [Business Requirements](#business-requirements)
- [Dataset Content](#dataset-content)
- [Hypotheses and how to validate?](#hypotheses-and-how-to-validate)
- [The rationale to map the business requirements to the Data Visualisations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
- [Business Requirement 1: Correlation Analysis](#business-Requirement-1-Correlation-Analysis)
- [Business Requirement 2: Predict Sale Price](#business-Requirement-2-Predict-Sale-Price)
- [ML Business Case](#ml-business-case)
- [User stories and Epics](#User-stories-and-Epics)
- [Dashboard Design](#dashboard-design)
- [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
- [Validation](#Validation)
- [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
  * [Heroku](#heroku)
- [Credits and Acknowledgements](#credits-and-acknowledgements)
- [Content](#content)


## Introduction

The objective of this project is to develop a machine learning application capable of predicting property values based on a provided dataset and its associated features. The client in this scenario is a fictional character, and the dataset used for this project has been sourced from Kaggle.co.uk.

## Business Requirements

The client has inherited four properties from her late great-grandfather, located in Ames, Iowa, USA. Originally from Belgium, the client has a strong understanding of property prices in her home country. However, she recognizes that the factors influencing property value in Belgium may not align with those in Ames, leaving her uncertain about accurately appraising the inherited properties.

**Client's Goals**
- Accurate Property Valuation
The client is aware of the significant financial implications of mispricing these properties. She seeks data-driven insights to ensure her pricing strategy aligns with the realities of the Iowan housing market, thereby maximizing the potential sale price of the four properties.

- Future Market Predictability
Beyond these immediate sales, the client is interested in developing a predictive model to estimate the sale price of any house in Ames. This capability would enable her to make informed decisions for future investments or sales in the area.


**Data Practitioner’s Role**
- To achieve these goals, the client has enlisted the help of a data practitioner. My role is to leverage data analytics and machine learning to provide actionable insights and reliable tools. This involves analyzing historical property data from Ames, identifying key factors that influence house prices, and creating a predictive model tailored to the Iowan housing market. By doing so, I aim to empower the client to confidently make pricing decisions and prepare her for potential future property dealings in the region.


**Business Requirements**

1. The client is keen to understand how various house attributes correlate with sale prices. As part of this, she expects data visualizations that clearly illustrate the relationships between key variables and sale prices.

2. The client wants to predict the sale prices for her four inherited houses and any other property in Ames, Iowa.


**Proposed Solution**<br>

To meet the client’s expectations, we will build an interactive Application Dashboard. This dashboard will:

* Provide an interface for the client to explore how house attributes correlate with sale prices through clear and insightful data visualizations.
* Predict the sale price of the four inherited houses and any individual house based on their features.
By delivering this application, we aim to address the client’s immediate concerns while equipping her with tools to navigate future property transactions confidently.

[Back to top](#table-of-contents)

## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

[Back to top](#table-of-contents)

## Hypotheses and how to validate?

**Hypothesis 1: Living Space and Sale Price**<br>

Hypothesis:
The amount of living space significantly impacts sale price. Larger living areas on the ground floor, first floor, and second floor will correlate with higher property values.

Validation Plan:
Analyze the relationship between sale price and living space variables (GroundLivingArea, FirstFloorSF, SecondFloorSF) using scatterplots.
Compute correlation coefficients to quantify the strength of the relationships.


**Hypothesis 2: Amenities and Sale Price**<br>

Hypothesis:
The presence and size of amenities, such as garages and basements, positively influence sale price. Properties with larger, well-finished amenities are expected to command higher values.

Validation Plan:
Use scatterplots to explore the correlation between sale price and quantitative variables (BasementSF, GarageArea).
Create boxplots to examine the relationship between sale price and categorical features (BasementFinish, GarageFinish), showing how different finish levels influence property value.


**Hypothesis 3: Build Quality and Sale Price**<br>

Hypothesis:
The quality of a property’s construction directly impacts its value, with higher-quality builds commanding higher sale prices.

Validation Plan:
Use boxplots to analyze the relationship between sale price and categorical variables (OverallQuality, KitchenQuality).
Compute summary statistics for sale price across quality levels to highlight the differences.


**Hypothesis 4: Property Age and Sale Price**<br>

Hypothesis:
Newer properties tend to attract higher sale prices, reflecting a preference for newer construction.

Validation Plan:
Use scatterplots to visualize the relationship between sale price and YearBuilt.
Compute correlation coefficients to assess the strength and direction of the relationship.
Group properties by decade and calculate average sale prices to observe trends over time.


**Additional factors/ Limitations**

I acknowledge that neighborhood area is not included in this dataset. I hypothesize that neighborhood characteristics play a significant role in determining sale price and should be considered as an important factor by the client alongside the results provided in this report.

It is important to note, however, that measuring neighborhood desirability can be a complex task. This factor often requires subjective judgment or external data inputs, such as socio-economic indicators, proximity to amenities, or crime rates, which are not readily available in the current dataset. As such, the absence of this variable may limit the comprehensiveness of the analysis.

Future studies could incorporate external data sources or proxy variables to better account for the influence of neighborhood on property values.

[Back to top](#table-of-contents)

## The rationale to map the business requirements to the Data Visualisations and ML tasks

### Business Requirement 1: Correlation Analysis

The client aims to understand how various house attributes correlate with sale prices. This requires both a statistical and visual analysis of the dataset to identify meaningful patterns. The following steps and their associated rationale are proposed to achieve this:

1.  Data exploration- Pandas profiling<br>
Rationale:
Before diving into correlation analysis, it is essential to explore and understand the dataset comprehensively. Pandas Profiling provides an automated summary of the dataset, highlighting key statistics such as missing values, distribution of features, and initial correlations. This step helps identify potential issues (e.g., outliers, skewed distributions, or missing data) that may influence subsequent analysis.

2. Encode categorical data<br>
Rationale:
Categorical variables, such as kitchen quality or basement exposure, must be encoded into numerical representations for meaningful correlation analysis. Encoding allows these variables to be included in both statistical methods (Pearson, Spearman) and visualizations. For ordinal data (e.g., quality ratings), ordinal encoding preserves the inherent order.

2. Conduct a Check Using Spearman and Pearson Methods and Predictive Power Score(PPS)<br>
Rationale:
Spearman and Pearson correlation methods are widely used for identifying relationships between variables. Pearson focuses on linear relationships, while Spearman captures monotonic relationships. Using both methods ensures a comprehensive analysis of correlations, even if the relationships are non-linear. PPS can be used to determine relationships between features.

3. Identify highest correlated features<br>
Rationale:
Using Pearson and Spearman correlation coefficients alongside PPS analysis, we will identify the features most strongly associated with sale price to prioritize them for further modeling and analysis

4. Visualize Relationships Between Sale Price and Key Features<br>
Rationale:
Data visualizations, such as scatterplots, boxplots, and heatmaps, provide an intuitive way to communicate insights to the client. Highlighting the highest correlated features (e.g., living space, build quality, amenities) with sale price will directly address the client’s goal of understanding feature impact.

This analysis will be conducted as part of the **Data Visualization, Cleaning, and Preparation** epic (refer to Epics & User Stories for details).

[Back to top](#table-of-contents)

### Business Requirement 2: Predict Sale Price

The goal is to provide an ML-driven solution that accurately forecasts the combined sales price of the client’s four inherited houses while also enabling exploration of the relationship between house characteristics and sale price through data visualizations. The following steps outline the approach and rationale:

1. Develop a Machine Learning (ML) Model to Predict Sale Prices<br>
Objective:
Build a regression model to predict the sale prices of the inherited properties and other houses in Ames, Iowa.<br>
Approach:
Use conventional ML techniques, such as linear regression, decision trees, or ensemble models (e.g., Random Forest, Gradient Boosting), depending on the dataset’s characteristics.
Train and validate the model using historical property data, optimizing for accuracy and generalizability.
Evaluate model performance using metrics such as R² (coefficient of determination), Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE).<br>
Rationale:
Regression models are well-suited for understanding the relationships between variables (e.g., living space, build quality, amenities) and the target (sale price). By leveraging a robust model, we ensure the client receives reliable price forecasts for the inherited houses.

This process will be undertaken as part of the **Model Training, Optimization, and Validation** epic (refer to Epics & User Stories for further details).

2. Map Relationships Between Features and Sale Price<br>
Objective:
Use the regression model to analyze and quantify the impact of individual house attributes on sale price.<br>
Approach:
Leverage feature importance metrics from the regression model to determine which variables contribute most to sale price predictions.
Use feature importance to illustrate the marginal effects of specific features (e.g., living area, build quality) on sale price.<br>
Rationale:
Mapping these relationships provides actionable insights into the driving factors behind property values, enabling the client to make informed decisions.

3. Incorporate Data Visualizations into an Interactive Streamlit Dashboard<br>
Objective:
Create a user-friendly dashboard for the client to explore how house attributes influence sale price and to view predictions for the inherited properties.<br>
Approach:
Integrate visualizations (e.g., scatterplots, box plots, heatmaps etc.) into the dashboard to represent feature correlations and model predictions.
Allow dynamic interaction by filtering selected house attributes and visualizing predicted sale prices based on custom input.
Show the predicted sale price of the 4 inherited houses along with total price.
Include explanations of the visualizations to enhance interpretability for the client.<br>
Rationale:
An interactive dashboard enables the client to:<br>
Explore relationships between attributes and sale price intuitively.
Simulate price predictions for properties beyond the inherited houses. This functionality empowers the client with a deeper understanding of the results.

This process will be undertaken as part of the **Dashboard Planning, Designing, and Development** epic (refer to Epics & User Stories for further details).

[Back to top](#table-of-contents)

## ML Business Case

### The CRISP-DM (Cross Industry Standard Process for Data Mining)

By following the CRISP-DM methodology, we ensure a systematic and client-focused approach. The project not only meets the clients immediate need to predict the sale prices of her inherited properties but also equips her with tools for future data-driven decisions.

This framework provides clarity, aligns the ML tasks with business objectives, and demonstrates a methodical plan to deliver actionable results.

1. Business Understanding
Objective:
The client wants to predict the combined sale price of four inherited properties in Ames, Iowa, while also gaining insights into how house attributes correlate with sale prices. This helps her set competitive prices for her properties and make data-driven decisions for future investments.

Key Questions:
What is the predicted combined sale price of the inherited houses?
Which house attributes (e.g., living space, build quality, amenities) have the most significant impact on sale prices?
How can the client interact with these insights and predictions to explore correlations and test scenarios?

Success Criteria:
A regression model with high predictive accuracy for house sale prices. The agreed metrics are 0.75 on R2 score for both Train and Test sets.
An interactive dashboard enabling the client to visualize correlations and predict sale prices for her properties and other houses in Ames.

2. Data Understanding
Data Sources:
A dataset from Ames, Iowa, including features such as living space, build quality, amenities, and sale prices.

Initial Exploration:
Assess data quality, completeness, and relevance to the clients goals.
Analyze relationships between variables and sale price through exploratory data analysis (EDA).

3. Data Preparation
Preprocessing Steps:
Handle missing values and outliers.
Encode categorical variables using methods such as ordinal encoding.
Split data into training and testing sets for model validation.

Feature Selection:
Use correlation analysis and feature importance metrics to identify the most influential variables for sale price prediction.

4. Modeling
Model Selection:
Choose regression algorithms based on dataset characteristics:
Linear Regression for simplicity and interpretability.
Advanced models like Random Forest or Gradient Boosting for improved accuracy.
Train the model using historical data and evaluate it using appropriate metrics.

Model Validation:
Evaluate model performance with R², MAE, and RMSE on test data.
Fine-tune hyperparameters to optimize accuracy.

5. Evaluation
Predictions:
Generate sale price predictions for the four inherited houses.
Provide the combined predicted value for all properties.

6. Deployment
Interactive Dashboard:
Deploy an application that integrates:
* Predictions for inherited properties.
* Data visualizations (scatterplots, heatmaps) showing correlations between features and sale prices.
* Simulations allowing the client to input custom property features and view predicted sale prices.

Business Impact:
The client gains the ability to confidently price her inherited properties.
She can use the dashboard as a tool for future investments or sales in the Ames property market.

[Back to top](#table-of-contents)

## Epics and User stories 

**Epic 1: Information Gathering and Data Collection**<br>
Description: Gather relevant data to understand the problem domain and prepare it for analysis and modeling.

**User Stories:**<br>

Data Practitioner’s Perspective:<br>
* As a data practitioner, I want to obtain a public dataset of house attributes and sale prices in Ames, Iowa, so that I can analyze and model the relationship between attributes and prices.
* As a data practitioner, I want to understand the client’s specific goals and requirements, so that I can tailor the analysis and predictions to their needs.<br>

Client’s Perspective:<br>
* As the client, I want to provide my specific requirements and goals for the analysis, so that the outputs align with my needs.
* As the client, I want to ensure that the data collected reflects real-world house attributes and prices, so that the predictions are relevant and actionable.
* As the client, I want to be informed about the sources of data used, so that I can trust the integrity of the analysis.
---

**Epic 2: Data Visualization, Cleaning, and Preparation**<br>
Description: Analyze, visualize, and prepare the dataset to extract meaningful insights and ensure it is ready for modeling.

**User Stories:**<br>

Data Practitioner’s Perspective:<br>
* As a data practitioner, I want to clean the dataset by handling missing values and outliers, so that the analysis and model training are not biased.
* As a data practitioner, I want to encode categorical variables, so that they can be used effectively in the regression model.
* As a data practitioner, I want to create visualizations (e.g., scatterplots, heatmaps, boxplots) of correlated variables against sale price, so that the client can understand the relationships between house attributes and sale price.*(Business requirement 1)*
* As a data practitioner, I want to compute correlation coefficients (Pearson, Spearman) and PPS scores, so that I can identify the most relevant variables for sale price prediction.*(Business Requirement 1)*
* As a data practitioner, I want to perform feature engineering on the required features to enhance the quality and predictive power of the dataset, ensuring the model is optimally prepared for training.

Client’s Perspective:<br>
* As a user, I want to see clear visualizations of the relationships between house attributes and sale price, so that I can understand the factors driving property values *(Business requirement 1)*.
* As a user, I want the dataset to be properly cleaned and prepared, so that the predictions I receive are reliable.
* As a user, I want to know which variables are most important for sale price predictions, so that I can make informed decisions about property improvements.*(Business requiremnt 1)*
---

**Epic 3: Model Training, Optimization, and Validation**<br>
Description: Build, train, and validate a regression model to predict house sale prices with acceptable performance metrics.

**User Stories:**<br>

Data Practitioner’s Perspective:<br>
* As a data practitioner, I want to train a regression model using house attribute data, so that I can predict sale prices for the client’s inherited properties *(Business Requirement 2)*.
* As a data practitioner, I want to optimize the model’s hyperparameters, so that the model achieves a minimum R² score of 0.75 on both the training and test sets. *(Business requirement 2)*. 
* As a data practitioner, I want to evaluate the model using metrics such as MAE, RMSE, and R², so that I can ensure its accuracy and reliability.

Client’s Perspective:<br>
* As a user, I want the model to provide accurate predictions for my four inherited properties, so that I can set competitive sale prices. *(Business Requirement 2)*
* As a user, I want assurance that the model has been thoroughly tested, so that I can trust its recommendations.
* As a user, I want the model’s performance metrics (e.g., R², MAE) to meet the agreed-upon standards, so that I know the predictions are reliable.
---

**Epic 4: Dashboard Planning, Design, and Development**<br>
Description: Create an interactive dashboard to display the analysis results and allow the client to explore data and predictions.

**User Stories:**<br>

Data Practitioner’s Perspective:<br>
* As a data practitioner, I want to design a dashboard interface that is user-friendly, so that the client can intuitively interact with the visualizations and predictions.
* As a data practitioner, I want to include visualizations of correlations and feature importance in the dashboard, so that the client can understand the drivers of sale price *(Business Requirement 1)*.
* As a data practitioner, I want to build a functionality in the dashboard to predict sale prices for the client’s four inherited properties, so that the client can make informed pricing decisions *(business Requirement 2)*.
* As a data practitioner, I want to allow the client to input house attributes into the dashboard and receive sale price predictions for other properties in Ames, so that the dashboard can serve as a future planning tool *(business Requirement 2)*.

Client’s Perspective:<br>
* As a user, I want the dashboard to be intuitive and easy to navigate, so that I can use it without technical expertise.
* As a user, I want to view a project summary that outlines the project’s purpose, dataset, and business requirements, so that I can quickly understand the scope and goals at a glance.
* As a user, I want to review the project hypotheses and their validations, so that I can assess what the project aimed to achieve and evaluate its success.
* As a user, I want to explore visualizations of how house attributes affect sale price, so that I can make data-driven decisions about property improvements *(Business Requirement 1)*.
* As a user, I want to input house attributes into the dashboard and receive sale price predictions, so that I can evaluate potential future investments in Ames, Iowa *(business Requirement 2)*.
* As a user, I want to see the value of each of my 4 inherited houses in Ames, Iowa and the total value for all *(business Requirement 2)*.
* As a user, I want the dashboard to provide an overview of the model performance and see statistics related to the model *(business Requirement 2)*.
---

**Epic 5: Dashboard Deployment and Release**<br>
Description: Deploy the completed dashboard for the client to use and ensure proper functionality.

**User Stories:**<br>

Data Practitioner’s Perspective:<br>
* As a data practitioner, I want to host and deploy the dashboard on a secure platform, so that the client can access it easily.
* As a data practitioner, I want to test the dashboard for usability and performance, so that it meets the client’s requirements without technical issues.

Client’s Perspective:<br>
* As a user, I want the dashboard to be hosted on a secure and accessible platform, so that I can use it whenever needed.
* As a user, I want to be supplied with a thorough Readme so that I can deploy the project myself if needed.

[Back to top](#table-of-contents)

## Dashboard Design

### Page 1: Project Summary
* Introduction to the project
* Dataset description
* Link to README.md file for further information on the dataset
* Business requirements

### Page 2: Hypotheses and Validation
* State each hypothesis
* How it was validated
* The Conclusion of each hypothesis

### Page 3: HH Correlation Study
* State business requirement 1
* Show first 10 lines of dataset
* State the key features used in the study
* Analysis summary
* Checkbox: display the scatterplots showing features correlation with the target variable
* Checkbox: display boxplot showing the median and quartile ranges of SalePrice vs overall quality across different quality levels
* Checkbox: Display heat map showing the combined Pearson/ Spearman correlation

### Page 4: Predict Sale Price
* State business requirement 2
* Key with features and their min/max values
* Set of widgets inputs
* "Predict sale price for single house"
*  Checkbox: Display predicted prices for each of the 4 inherited properties and show combined value


### Page 5: Technical analysis
* Present ML pipeline steps
* Model success metrics
* Test and Train performance on the model
* Evaluation scatterplots on Test and Train
* Feature importance 


### Page 6: Project Conclusions
* Considerations and conclusions after the pipeline is trained
* Project outcomes

[Back to top](#table-of-contents)

## Technologies Used
The technologies used throughout the development are listed below:

### Languages

* [Python](https://www.python.org/)

### Main Data Analysis and Machine Learning Libraries

* [Pandas](https://pandas.pydata.org/docs/index.html) - Data analysis and manipulation tool
* [Numpy](https://numpy.org/doc/stable/index.html) - The fundamental package for scientific computing with Python
* [YData Profiling](https://docs.profiling.ydata.ai/latest/) - For data profiling and exploratory data analysis
* [Matplotlib](https://matplotlib.org/) - Comprehensive library for creating static, animated and interactive visualisations
* [Seaborn](https://seaborn.pydata.org/) - Data visualisation library for drawing attractive and informative statistical graphics
* [Feature-engine](https://feature-engine.trainindata.com/en/latest/) - Transformers to engineer and select features for machine learning models
* [ppscore](https://pypi.org/project/ppscore/) - Data-type-agnostic score that can detect linear or non-linear relationships between two columns
* [scikit-learn](https://scikit-learn.org/stable/) - Machine learning library for training the ML model
* [Joblib](https://joblib.readthedocs.io/en/stable/) - Tool for dumping pipeline to pickle files
* [Kaggle](https://pypi.org/project/kaggle/) - Kaggle API functionalit
* [Streamlit](https://streamlit.io/) - Build the web app.

### Other Technologies

* [Git](https://git-scm.com/) - For version control
* [GitHub](https://github.com/) - Code repository
* [Heroku](https://heroku.com) - For application deployment
* [Gitpod](https://www.gitpod.io/) - Cloud IDE used for development
* [Jupyter Notebook](https://jupyter.org/) - Interactive Python
* [CI Python Linter](https://pep8ci.herokuapp.com/) - Style guide for python

[Back to top](#table-of-contents)

## Testing
### Manual Testing

#### User Story Testing

*As a user, I want to view a project summary that outlines the project’s purpose, dataset, and business requirements, so that I can quickly understand the scope and goals at a glance.*

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Project summary page |Open app. View summary page | Page is displayed, can scroll between sections on page | Functions as intended |

---

*As a user, I want to review the project hypotheses and their validations, so that I can assess what the project aimed to achieve and evaluate its success.*

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Project hypotheses page | Click on radio button on left navbar to navigate to Hypotheses page | Navigates to correct page. Can scroll through hypotheses | Functions as intended |

---
* As a user, I want to see clear visualizations of the relationships between house attributes and sale price, so that I can understand the factors driving property values *(Business requirement 1)*.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Correlation study page | Click on radio button on left navbar to Correlation study page | Navigates to correct page | Functions as intended |
| Correlation study page- Inpect Data | Click on "inspect dataset" | displays first 10 rows of dataset | Functions as intended |
| Correlation study page- Scatterplots | Click on radio "Scatterplots" | displays selected scatterplots | Functions as intended |
| Correlation study page- Boxplot | Click on radio "Boxplot" | displays selected Boxplot | Functions as intended |
| Correlation study page- Heat map | Click on radio "Heatmap" | displays selected heatmap | Functions as intended |

---

*As a user, I want to input house attributes into the dashboard and receive sale price predictions, so that I can evaluate potential future investments in Ames, Iowa *(business Requirement 2)*.*

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| ML- Predict sale price page | Click on radio button on left navbar to ML- Predict sale price page | Navigates to correct page | Functions as intended |
| ML- Predict sale price page- plus/ minus | Click on a value for each feature using plus/minus buttons| changes according to the plus/minus input | Functions as intended |
| ML- Predict sale price page- Enter value in range | Click on a value for each feature by clicking on the value and manually entering a value between those listed in the key| changes according to the input. | Functions as intended |
| ML- Predict sale price page- Enter value out of range | Click on a value for each feature by clicking on the value and manually entering a value out of the range form those listed in the key| Displays error message | Functions as intended |
| ML- Predict sale price page- Enter values for prediction | select values from features within selected range| Once values are selected, they are replicated in "Input Features for Prediction"| Functions as intended |
| ML- Predict sale price page- predict price | click "Predict Sale Price for Single House"| A value is returned and displayed on the page | Functions as intended |

---

* As a user, I want to see the value of each of my 4 inherited houses in Ames, Iowa and the total value for all *(business Requirement 2)*.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| ML- Predict sale price page- Inherited houses | Click on "Predict Prices for Inherited Houses" | Shows each feature, its corresponding value and overall price. Shows total price | Functions as intended |

---

* As a user, I want the dashboard to provide an overview of the model performance and see statistics related to the model *(business Requirement 2)*.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| ML pipeline and technical analysis | Navigate to page using radio button | Displays ML pipeline page | Functions as intended |
| ML Pipeline | View page | ML Pipelines used for this project are displayed | Functions as intended |
| Success metrics | View page | Success metrics outlined in business case are displayed | Functions as intended |
| Model Performance | View page | Metrics for train and test sets and evaluation plots are displayed | Functions as intended |
| Feature Importance | View page | Most important features are plotted and displayed | Functions as intended |

---

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Conclusions and considerations | Navigate to page using radio button | Displays conclusions and considerations | Functions as intended |


[Back to top](#table-of-contents)

## Validation

All python files were passed through the CI PEP8 Linter in order to validate the code to adhere to PEP8 standards. All files passed with no errors. 

[Back to top](#table-of-contents)

## Fixed bugs

* Initially, the predict sale price function did not impose restrictions on the input ranges for various features. This allowed users to input values significantly deviating from the realistic ranges observed in the dataset. Such discrepancies could lead to inaccurate predictions, as the model was not trained on data far outside the dataset's original scope.

To address this, I implemented realistic input ranges aligned with the dataset's values. These ranges were carefully selected to:

* Reflect the actual distribution of the dataset, ensuring predictions are relevant and accurate.
* Provide some flexibility to account for scenarios beyond the dataset, such as properties built in the future or with slightly larger or smaller attributes than those observed in the data.<br>

For example:<br>
* Overall Quality: Previously, values greater than 10 (the maximum quality score) could be selected. This has been restricted to the realistic range of 1–10.
* Features like YearBuilt: The range was extended slightly to allow for future construction dates while maintaining realistic bounds.
* Size Features (e.g., TotalBsmtSF, GarageArea): The ranges were adjusted to accommodate slightly larger or smaller properties, without allowing values that are illogical (e.g., negative square footage).

## Unfixed Bugs

* No known unfixed bugs

[Back to top](#table-of-contents)

## Deployment

### Heroku

The project was deployed to Heroku using the following steps:

1. Within your working directory, ensure there is a setup.sh file containing the following:
```
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```
2. Within your working directory, ensure there is a runtime.txt file containing a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack supported version of Python.
```
python-3.8.18
```
3. Within your working directory, ensure there is a Procfile file containing the following:
```
web: sh setup.sh && streamlit run main.py
```
4. Ensure your requirements.txt file contains all the packages necessary to run the streamlit dashboard.
5. Update your .gitignore and .slugignore files with any files/directories that you do not want uploading to GitHub or are unnecessary for deployment.
6. Log in to [Heroku](https://id.heroku.com/login) or create an account if you do not already have one.
7. Click the **New** button on the dashboard and from the dropdown menu select "Create new app".
8. Enter a suitable app name and select your region, then click the **Create app** button.
9. Once the app has been created, navigate to the Deploy tab.
10. At the Deploy tab, in the Deployment method section select **GitHub**.
11. Enter your repository name and click **Search**. Once it is found, click **Connect**.
12. Navigate to the bottom of the Deploy page to the Manual deploy section and select main from the branch dropdown menu.
13. Click the **Deploy Branch** button to begin deployment.
14. The deployment process should happen smoothly if all deployment files are fully functional. Click the button **Open App** at the top of the page to access your App.
15. If the build fails, check the build log carefully to troubleshoot what went wrong.

[Back to top](#table-of-contents)

## Forking and Cloning
If you wish to fork or clone this repository, please follow the instructions below:

### Forking
1. In the top right of the main repository page, click the **Fork** button.
2. Under **Owner**, select the desired owner from the dropdown menu.
3. **OPTIONAL:** Change the default name of the repository in order to distinguish it.
4. **OPTIONAL:** In the **Description** field, enter a description for the forked repository.
5. Ensure the 'Copy the main branch only' checkbox is selected.
6. Click the **Create fork** button.

### Cloning
1. On the main repository page, click the **Code** button.
2. Copy the HTTPS URL from the resulting dropdown menu.
3. In your IDE terminal, navigate to the directory you want the cloned repository to be created.
4. In your IDE terminal, type ```git clone``` and paste the copied URL.
5. Hit Enter to create the cloned repository.

### Installing Requirements
**WARNING:** The packages listed in the requirements.txt file are limited to those necessary for the deployment of the dashboard to Heroku, due to the limit on the slug size.

In order to ensure all the correct dependencies are installed in your local environment, run the following command in the terminal:

    pip install -r full-requirements.txt

[Back to top](#table-of-contents)

## Credits and Acknowledgements

* This project utilized the repository template from the Heritage Housing idea provided by Code Institute (CI).
* The dataset was sourced from Kaggle, as referenced above.
* The custom class for hyperparameter optimization was adapted from the Predict Tenure Notebook (CI).
* Guidance and inspiration were drawn from the CI Data Analytics Program, including the Walkthrough Project 2 - Churnometer.
* Additional research and insights were gathered from resources such as Google, YouTube, Stack Overflow, Slack, and GeeksforGeeks, which provided valuable explanations across various topics.  \n
* A special thanks to my mentor, Mo Shami, for his invaluable guidance and support throughout this project.

[Back to top](#table-of-contents)

