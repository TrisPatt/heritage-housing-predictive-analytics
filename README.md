# Predict Sale Price
<img width="946" alt="Screenshot 2023-08-31 at 09 05 26" src="assets/imgs/Screenshot 2024-11-27 164059.png">


Link to the project dashboard is [HERE](https://hh-predictive-analytics-p5-ab08303eeb0a.herokuapp.com/)

## Table of Contents
- [Business Requirements](#business-requirements)
- [Dataset Content](#dataset-content)
- [Hypotheses for Case Study](#hypotheses-for-case-study)
- [The rationale to map the business requirements to the Data Visualisations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
- [Business Requirement 1:*](#business-requirement-1--)
- [Business Requirement 2:](#business-requirement-2-)
  * [User Stories - Client:](#user-stories---client-)
  * [User Stories - Data Practitioner:](#user-stories---data-practitioner-)
- [ML Business Case](#ml-business-case)
    + [Predict House Prices in Ames, Iowa](#predict-house-prices-in-ames--iowa)
- [Regression model](#regression-model)
- [Dashboard Design](#dashboard-design)
- [Wireframes](#wireframes)
  * [Running the application](#running-the-application)
  * [Answers Business Requirement 1:](#answers-business-requirement-1-)
  * [Answers Business Requirement 2:](#answers-business-requirement-2-)
- [Unfixed Bugs](#unfixed-bugs)
- [Conclusion](#conclusion)
  * [Summary of Findings](#summary-of-findings)
- [Results](#results)
- [Deployment](#deployment)
  * [Heroku](#heroku)
- [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
- [Credits and Acknowledgements](#credits-and-acknowledgements)

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
- Correlation Analysis
1. The client is keen to understand how various house attributes correlate with sale prices. As part of this, she expects data visualizations that clearly illustrate the relationships between key variables and sale prices.

- Sales Price Prediction
2. The client wants to predict the sale prices for her four inherited houses and any other property in Ames, Iowa.


**Proposed Solution**<br>

To meet the client’s expectations, we will build an interactive Application Dashboard. This dashboard will:

* Provide an interface for the client to explore how house attributes correlate with sale prices through clear and insightful data visualizations.
* Predict the sale price of the four inherited houses and any individual house based on their features.
By delivering this application, we aim to address the client’s immediate concerns while equipping her with tools to navigate future property transactions confidently.
  

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


## Hypothesis and how to validate?

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


## The rationale to map the business requirements to the Data Visualisations and ML tasks

### Business Requirement 1: Correlation Analysis

The client aims to understand how various house attributes correlate with sale prices. This requires both a statistical and visual analysis of the dataset to identify meaningful patterns. The following steps and their associated rationale are proposed to achieve this:

1.  Data exploration- Pandas profiling
Rationale:
Before diving into correlation analysis, it is essential to explore and understand the dataset comprehensively. Pandas Profiling provides an automated summary of the dataset, highlighting key statistics such as missing values, distribution of features, and initial correlations. This step helps identify potential issues (e.g., outliers, skewed distributions, or missing data) that may influence subsequent analysis.

2. Encode categorical data
Rationale:
Categorical variables, such as kitchen quality or basement exposure, must be encoded into numerical representations for meaningful correlation analysis. Encoding allows these variables to be included in both statistical methods (Pearson, Spearman) and visualizations. For ordinal data (e.g., quality ratings), ordinal encoding preserves the inherent order, while one-hot encoding may be used for nominal data.

2. Conduct a Check Using Spearman and Pearson Methods
Rationale:
Spearman and Pearson correlation methods are widely used for identifying relationships between variables. Pearson focuses on linear relationships, while Spearman captures monotonic relationships. Using both methods ensures a comprehensive analysis of correlations, even if the relationships are non-linear.

3. Identify highest correlated features
Rationale:
From the data analysis conducted using methods such as Pearson and Spearman correlation coefficients, we will identify the features most strongly associated with the sale price. 

4. Visualize Relationships Between Sale Price and Key Features
Rationale:
Data visualizations, such as scatterplots, boxplots, and heatmaps, provide an intuitive way to communicate insights to the client. Highlighting the highest correlated features (e.g., living space, build quality, amenities) with sale price will directly address the client’s goal of understanding feature impact.


### Business Requirement 2: Predict Sale Price

The goal is to provide an ML-driven solution that accurately forecasts the combined sales price of the client’s four inherited houses while also enabling exploration of the relationship between house characteristics and sale price through data visualizations. The following steps outline the approach and rationale:

1. Develop a Machine Learning (ML) Model to Predict Sale Prices
Objective:
Build a regression model to predict the sale prices of the inherited properties and other houses in Ames, Iowa.
Approach:
Use conventional ML techniques, such as linear regression, decision trees, or ensemble models (e.g., Random Forest, Gradient Boosting), depending on the dataset’s characteristics.
Train and validate the model using historical property data, optimizing for accuracy and generalizability.
Evaluate model performance using metrics such as R² (coefficient of determination), Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE).
Rationale:
Regression models are well-suited for understanding the relationships between variables (e.g., living space, build quality, amenities) and the target (sale price). By leveraging a robust model, we ensure the client receives reliable price forecasts for the inherited houses.

2. Map Relationships Between Features and Sale Price
Objective:
Use the regression model to analyze and quantify the impact of individual house attributes on sale price.
Approach:
Leverage feature importance metrics from the regression model to determine which variables contribute most to sale price predictions.
Use feature importance to illustrate the marginal effects of specific features (e.g., living area, build quality) on sale price.
Rationale:
Mapping these relationships provides actionable insights into the driving factors behind property values, enabling the client to make informed decisions.

3. Incorporate Data Visualizations into an Interactive Streamlit Dashboard
Objective:
Create a user-friendly dashboard for the client to explore how house attributes influence sale price and to view predictions for the inherited properties.
Approach:
Integrate visualizations (e.g., scatterplots, box plots, heatmaps etc.) into the dashboard to represent feature correlations and model predictions.
Allow dynamic interaction by filtering selected house attributes and visualizing predicted sale prices based on custom input.
Show the predicted sale price of the 4 inherited houses along with total price.
Include explanations of the visualizations to enhance interpretability for the client.
Rationale:
An interactive dashboard enables the client to:
Explore relationships between attributes and sale price intuitively.
Simulate price predictions for properties beyond the inherited houses. This functionality empowers the client with a deeper understanding of the results.


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
Encode categorical variables using methods such as ordinal or one-hot encoding.
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

Interpretability:
Use techniques like SHAP values or PDPs to explain the model’s predictions and feature importance.

6. Deployment
Interactive Dashboard:
Deploy an application that integrates:
* Predictions for inherited properties.
* Data visualizations (scatterplots, heatmaps) showing correlations between features and sale prices.
* Simulations allowing the client to input custom property features and view predicted sale prices.

Business Impact:
The client gains the ability to confidently price her inherited properties.
She can use the dashboard as a tool for future investments or sales in the Ames property market.

### User stories and Epics

#### The Practioner
Epic 1: Information Gathering and Data Collection
Description: Gather relevant data to understand the problem domain and prepare it for analysis and modeling.

User Stories:
As a data practitioner, I want to obtain a public dataset of house attributes and sale prices in Ames, Iowa, so that I can analyze and model the relationship between attributes and prices.
As a data practitioner, I want to understand the client’s specific goals and requirements, so that I can tailor the analysis and predictions to their needs.


Epic 2: Data Visualization, Cleaning, and Preparation
Description: Analyze, visualize, and prepare the dataset to extract meaningful insights and ensure it is ready for modeling.

User Stories:
As a data practitioner, I want to clean the dataset by handling missing values and outliers, so that the analysis and model training are not biased.
As a data practitioner, I want to encode categorical variables, so that they can be used effectively in the regression model.
As a data practitioner, I want to create visualizations (e.g., scatterplots, heatmaps, boxplots) of correlated variables against sale price, so that the client can understand the relationships between house attributes and sale price.
As a data practitioner, I want to compute correlation coefficients (Pearson, Spearman) and PPS scores, so that I can identify the most relevant variables for sale price prediction.


Epic 3: Model Training, Optimization, and Validation
Description: Build, train, and validate a regression model to predict house sale prices with acceptable performance metrics.

User Stories:
As a data practitioner, I want to train a regression model using house attribute data, so that I can predict sale prices for the client’s inherited properties.
As a data practitioner, I want to optimize the model’s hyperparameters, so that the model achieves a minimum R² score of 0.75 on both the training and test sets.
As a data practitioner, I want to evaluate the model using metrics such as MAE, RMSE, and R², so that I can ensure its accuracy and reliability.


Epic 4: Dashboard Planning, Design, and Development
Description: Create an interactive dashboard to display the analysis results and allow the client to explore data and predictions.

User Stories:
As a data practitioner, I want to design a dashboard interface that is user-friendly, so that the client can intuitively interact with the visualizations and predictions.
As a data practitioner, I want to include visualizations of correlations and feature importance in the dashboard, so that the client can understand the drivers of sale price.
As a data practitioner, I want to build a functionality in the dashboard to predict sale prices for the client’s four inherited properties, so that the client can make informed pricing decisions.
As a data practitioner, I want to allow the client to input house attributes into the dashboard and receive sale price predictions for other properties in Ames, so that the dashboard can serve as a future planning tool.


Epic 5: Dashboard Deployment and Release
Description: Deploy the completed dashboard for the client to use and ensure proper functionality.

User Stories:
As a data practitioner, I want to host and deploy the dashboard on a secure platform, so that the client can access it easily.
As a data practitioner, I want to test the dashboard for usability and performance, so that it meets the client’s requirements without technical issues.
As a data practitioner, I want to provide the client with a tutorial or user guide, so that they can effectively utilize the dashboard for their property pricing needs.

#### The Client
Epic 1: Understanding the Factors Influencing Sale Prices
Description: As the client, I want to explore how various house attributes affect sale prices so that I can understand what drives property value in Ames, Iowa.

User Stories:
As the client, I want to view clear visualizations of how house attributes (e.g., living space, build quality) correlate with sale prices so that I can identify key factors that influence property value.
As the client, I want to review a report summarizing the most relevant variables impacting sale prices so that I can make informed pricing decisions.
As the client, I want to explore how specific attributes of my four inherited houses compare to the highest-impact features, so that I can estimate their potential market value.


Epic 2: Predicting Sale Prices
Description: As the client, I want to predict the sale prices of my inherited properties and other houses in Ames, Iowa, so that I can confidently set prices and plan for future investments.

User Stories:
As the client, I want to view accurate sale price predictions for my four inherited houses so that I can determine their market value.
As the client, I want to input house attributes into the dashboard to predict sale prices for other properties in Ames, so that I can plan for future property sales or investments.
As the client, I want to understand how the predictions are generated (e.g., which features contributed most), so that I can trust and validate the results.


Epic 3: Using an Interactive Dashboard
Description: As the client, I want to use a dashboard to interact with the data and predictions so that I can explore insights easily and make decisions efficiently.

User Stories:
As the client, I want a user-friendly dashboard that provides easy navigation, so that I can quickly access the insights and tools I need.
As the client, I want to view visualizations on the dashboard (scatterplots, heatmaps, etc.) to see how house attributes relate to sale prices, so that I can explore patterns intuitively.
As the client, I want the dashboard to display the combined sale price of my inherited properties, so that I can understand their total market value.
As the client, I want to simulate how changing specific house attributes (e.g., adding a garage or increasing living space) affects sale prices, so that I can evaluate improvement options for my properties.


Epic 4: Evaluating Project Success
Description: As the client, I want to evaluate the outcomes of the analysis and the dashboard's capabilities to ensure they meet my needs.

User Stories:
As the client, I want to ensure the visualizations clearly show how house attributes correlate with sale prices, so that I can gain actionable insights.
As the client, I want to ensure the sale price predictions meet an agreed level of accuracy (R² ≥ 0.75) so that I can trust the model's outputs.
As the client, I want to provide feedback on the dashboard’s usability and insights, so that any necessary improvements can be made before final deployment.


Epic 5: Leveraging Insights for Business Decisions
Description: As the client, I want to use the insights and tools provided to maximize the value of my inherited properties and plan for future real estate opportunities.

User Stories:
As the client, I want to identify the features that add the most value to houses in Ames, so that I can prioritize improvements to my inherited properties.
As the client, I want to understand trends in the Ames housing market, so that I can make data-driven investment decisions.
As the client, I want to use the dashboard for future sales predictions, so that I can manage property sales efficiently.


## Dashboard Design

* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items that your dashboard library supports.
* Eventually, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type)


## Conclusion
### Summary of results

## Validation

All python files were passed through the CI PEP8 Linter in order to validate the code to adhere to PEP8 standards. All files passed with no errors. 

## Unfixed Bugs

* No known unfixed bugs

## Deployment

### Heroku

* The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.

## Credits

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
* You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

* The text for the Home page was taken from Wikipedia Article A
* Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
* The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

* The photos used on the home and sign-up page are from This Open Source site
* The images used for the gallery page were taken from this other open-source site

## Acknowledgements (optional)


* In case you would like to thank the people that provided support through this project.

