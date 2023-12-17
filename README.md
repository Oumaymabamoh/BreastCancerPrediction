# Breast Cancer Prediction Project

## Overview
This project focuses on the development of an interpretable machine learning model for predicting breast cancer malignancy. Leveraging a dataset rich in cell nuclei characteristics, we aim to create a model that not only achieves high accuracy but also provides insights into the decision-making process.

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
- `notebooks`: Includes Jupyter notebooks for data exploration, modeling, and analysis.
- `src`: Consists of source code, such as Python scripts, for model training, evaluation, and GUI development.

## Data
The dataset (`data.csv`) comprises various features related to cell nuclei characteristics. Explore the dataset to understand the input variables and target labels.

## Modeling
The `notebooks/modeling.ipynb` notebook showcases the process of model development. We experimented with different algorithms, prioritizing accuracy and interpretability. Cross-validation results and model evaluations are presented.

## GUI
To enhance usability, a graphical user interface (GUI) is proposed for easy interaction with the predictive model. The `src/gui` folder contains code for the GUI.

## Requirements
Ensure you have the required dependencies installed. Use the following command:
```bash
pip install -r requirements.txt