# First you need to red the REDME file and set up your dataset in the correct way.

import pandas as pd
from joblib import load

# Define the path to the user's Excel file
path_to_excel_file = 'path/to/your/dataset.xlsx'

# Define the path to the saved pipeline
pipeline_file_path = 'Path/to/stroke_prediction_pipeline.joblib'

# Load the data
df = pd.read_excel(path_to_excel_file)

# Load the entire pipeline
pipeline = load(pipeline_file_path)

# Use the pipeline to make predictions
# Note: You might need to drop or handle columns that are not used in the model
predictions = pipeline.predict(df)

# Impute the predictions into the DataFrame
df['Predicted_Outcome'] = predictions

# Define the path for the new Excel file with predictions
path_to_new_excel_file = '/Users/berghelland/Documents/Gisle/Forskning/Egne_artikler/Ph.D.-Artikler/LesionVolume_Work/scripts/new_data_with_predictions.xlsx'

# Save the DataFrame with predictions back to an Excel file
df.to_excel(path_to_new_excel_file, index=False)

print("Predictions have been added to the Excel file and saved.")
