import os
import json
from sentence_transformers import SentenceTransformer, util
import pandas as pd

# Load LaBSE model
model = SentenceTransformer('sentence-transformers/LaBSE')

# Assuming the .xlsx file is in a 'Data' folder within your project directory
file_path = os.path.join('Data', 'Test Files.xlsx')

# Read the Excel file using pandas
df = pd.read_excel(file_path)

# Separate male and female students
if 'Student Name' in df.columns and 'Gender' in df.columns:
    males = df[df['Gender'].str.upper() == 'M']['Student Name'].tolist()
    females = df[df['Gender'].str.upper() == 'F']['Student Name'].tolist()

    # Generate embeddings for male and female names
    male_embeddings = model.encode(males, convert_to_tensor=True)
    female_embeddings = model.encode(females, convert_to_tensor=True)

    # Compute similarity matrix
    similarity_matrix = util.pytorch_cos_sim(male_embeddings, female_embeddings)

    # Filter results with at least 50% similarity
    threshold = 0.5
    similarity_results = []
    for i, male_name in enumerate(males):
        for j, female_name in enumerate(females):
            if similarity_matrix[i][j] >= threshold:
                similarity_results.append({
                    'male_name': male_name,
                    'female_name': female_name,
                    'similarity': float(similarity_matrix[i][j])
                })

    # Save results to JSON file
    output_json_path = os.path.join('Data', 'Name_Similarity_Results.json')
    with open(output_json_path, 'w') as f:
        json.dump(similarity_results, f, indent=4)

    print(f"\nSimilarity results saved to: {output_json_path}")
else:
    print("The required columns 'Student Name' or 'Gender' are missing from the file.")
