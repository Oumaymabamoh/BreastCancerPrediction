# Breast Cancer Prediction Project

## Overview
This project focuses on the development of an interpretable machine learning model for predicting breast cancer malignancy. Leveraging a dataset rich in cell nuclei characteristics, we aim to create a model that not only achieves high accuracy but also provides insights into the decision-making process. The primary mission is to craft a classification model capable of predicting tumor malignancy with exceptional accuracy (F1 score > 0.95). More crucially, the model is designed to be interpretable, unraveling the complexities of its decision-making process. This transparency is not just a technical pursuit but a strategic endeavor to instill trust among non-experts and foster broader acceptance of technology in the medical domain

## Table of Contents
- [Project Structure](#project-structure)
- [Data](#data)
- [Modeling](#modeling)
- [GUI](#gui)
- [Requirements](#requirements)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Structure
The project is organized following the CRISP-DM methodology. Key folders include:
- `data`: Contains the dataset (`data.csv`) and any additional data-related files.
- `src`: Consists of source code, for data exploration, modeling, and analysis.
- data_exploration: Contains scripts or notebooks dedicated to exploring and understanding the dataset. Visualizations, statistical analyses, and any preprocessing steps are conducted here.
-modeling: This section encompasses the code for building, training, and evaluating machine learning models. It includes the development of the interpretable breast cancer prediction model, hyperparameter tuning, and cross-validation.
-analysis: Holds scripts or notebooks focused on in-depth analysis of model results, feature importance, and error analysis. This phase is crucial for extracting meaningful insights from the developed model.
- `README.md`:The README file serves as the project's central documentation hub. It provides an overview of the project, instructions on setting up the environment, running the code.
- `requirements.txt`:  This file enumerates the project's dependencies and required packages. It ensures a consistent environment across different systems and facilitates easy setup by running pip install -r requirements.txt.

## Data
The dataset (`data.csv`) comprises various features related to cell nuclei characteristics. Explore the dataset to understand the input variables and target labels.
<img width="660" alt="Screen Shot 2023-12-15 at 14 03 38" src="https://github.com/Oumaymabamoh/BreastCancerPrediction/assets/134213098/711d961c-41e7-49d5-8ac7-cb6db23afb5e">

## Modeling
The `src/modeling.ipynb` notebook showcases the process of model development. We experimented with different algorithms, prioritizing accuracy and interpretability. Cross-validation results and model evaluations are presented.
<img width="670" alt="Screen Shot 2023-12-17 at 21 49 08" src="https://github.com/Oumaymabamoh/BreastCancerPrediction/assets/134213098/353b8b0e-3170-4161-a9b2-fc9cb7bc60b8">

## GUI
To enhance usability, a graphical user interface (GUI) is proposed for easy interaction with the predictive model.
![Blank diagram - Page 2](https://github.com/Oumaymabamoh/BreastCancerPrediction/assets/134213098/a12f322f-032a-4cd1-8b35-e68ee19779d9)

## Requirements
Ensure you have the required dependencies installed. Use the following command:
```bash
pip install -r requirements.txt
