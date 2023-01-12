# Employee-Perfromance-Estimator-Using-Classification-model
# Project goal and introduction

Project related to Employee performance prediction. This app predict performance of employee considering different features when working from home. By evaluating employees performance, we can suggest them to take a appropriate action and make changes in their strategies for individual and  organization growth.
Scope of this project is to motivate, enhance employees skills set both psychological and technical so that they can  increase their productivity and perform effectively towards organization goals.

# About data
Data is pulled from the SQL database where employee data is stored. It has 5100 records and 28 fields.7 numerical and 21 categorical features
Target variable - Performance Rating. It is a categorical with output good, bad and neutral

# Model building
As output variable is categorical, regression models are trained. Decision tree, Random forest, k- Nearest Neighbour,Multilinear regression and Decision tree model with 96% accuracy is selected for model building

Deployment
Streamlit framework is used for app building.Streamlit cloud platform is used for cloud deployment. User is allowed to input the features related to employee to predict perfromance and clicking on predict button displays perfromance of employee.

App Link:https://99vismaya-employee-perfromance-estimator-using-class-app-v8j2z9.streamlit.app/
