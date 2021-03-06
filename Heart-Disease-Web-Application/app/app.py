import streamlit as st
import pandas as pd
from src.utils.data import data
from src.utils.home import home
from src.utils.visualizations import visualizations
from src.utils.predictor import predictor

pd.options.mode.chained_assignment = None

# Dictionary that calls function objects for each website page:
PAGE_DICT = {"Home": home,
             "Data": data,
             "Visualizations": visualizations,
             "Heart Disease Predictor": predictor
            }

def clean_data(df):
    """
    Function will be used to clean the dataset.

    Parameters
    ----------
    df: DataFrame
        A dataframe containing the the heart disease data.
    
    Returns
    -------
    df: DataFrame
        A dataframe containing the cleansed heart disease data.
    """
    df['sex'][df['sex'] == 0] = 'female'
    df['sex'][df['sex'] == 1] = 'male'

    df['chest_pain_type'][df['chest_pain_type'] == 0] = 'typical angina'
    df['chest_pain_type'][df['chest_pain_type'] == 1] = 'atypical angina'
    df['chest_pain_type'][df['chest_pain_type'] == 2] = 'non-anginal pain'
    df['chest_pain_type'][df['chest_pain_type'] == 3] = 'asymptomatic'

    df['fasting_blood_sugar'][df['fasting_blood_sugar'] == 0] = 'lower than 120mg/ml'
    df['fasting_blood_sugar'][df['fasting_blood_sugar'] == 1] = 'greater than 120mg/ml'

    df['rest_ecg'][df['rest_ecg'] == 0] = 'normal'
    df['rest_ecg'][df['rest_ecg'] == 1] = 'ST-T wave abnormality'
    df['rest_ecg'][df['rest_ecg'] == 2] = 'left ventricular hypertrophy'

    df['exercise_induced_angina'][df['exercise_induced_angina'] == 0] = 'no'
    df['exercise_induced_angina'][df['exercise_induced_angina'] == 1] = 'yes'

    df['st_slope'][df['st_slope'] == 0] = 'upsloping'
    df['st_slope'][df['st_slope'] == 1] = 'flat'
    df['st_slope'][df['st_slope'] == 2] = 'downsloping'

    df['thalassemia'][df['thalassemia'] == 0] = 'normal'
    df['thalassemia'][df['thalassemia'] == 1] = 'fixed defect'
    df['thalassemia'][df['thalassemia'] == 2] = 'reversable defect'
    df['thalassemia'][df['thalassemia'] == 3] = 'reversable defect'

    return df

def change_dtypes(df):
    """
    Function will be used to convert features to appropriate type.

    Parameters
    ----------
    df: DataFrame
        A dataframe containing the heart disease data.

    Returns
    -------
    df: DataFrame
        A dataframe containing the cleansed heart disease data.
    """
    df['sex'] = df['sex'].astype('object')
    df['chest_pain_type'] = df['chest_pain_type'].astype('object')
    df['fasting_blood_sugar'] = df['fasting_blood_sugar'].astype('object')
    df['rest_ecg'] = df['rest_ecg'].astype('object')
    df['exercise_induced_angina'] = df['exercise_induced_angina'].astype('object')
    df['st_slope'] = df['st_slope'].astype('object')
    df['thalassemia'] = df['thalassemia'].astype('object')
    
    return df

def main():
    """Main function"""
    st.title("?????? Heart Disease Application ??????")
    df = open(input("heart.csv"))
    st.sidebar.title("Menu")

    # Creating radio buttons to choose menu options:
    option = st.sidebar.radio(label="Select", 
                             options=["Home", 
                                     "Data", 
                                     "Visualizations", 
                                     "Heart Disease Predictor"])
    # Column name changes:
    df.columns = ['age', 'sex', 'chest_pain_type', 
                  'resting_blood_pressure', 'cholesterol', 'fasting_blood_sugar', 
                  'rest_ecg', 'max_heart_rate_achieved', 'exercise_induced_angina', 
                  'st_depression', 'st_slope', 'num_major_vessels', 
                  'thalassemia', 'target']
    
    # Calling cleaning data functions:
    df = clean_data(df)
    df = change_dtypes(df)

    # Calling appropriate function object for pages:
    PAGE_DICT[option](df)



if __name__ == "__main__":
    main()
