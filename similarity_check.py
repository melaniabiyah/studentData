import json
import pandas as pd
import torch
from transformers import BertTokenizer, BertModel
from scipy.spatial.distance import cosine

# Load LaBSE model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-uncased')
model = BertModel.from_pretrained('bert-base-multilingual-uncased')

def get_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

def compute_similarity(embedding1, embedding2):
    return 1 - cosine(embedding1, embedding2)

# Load data
df_males = pd.read_excel('Data/Male_Students.xlsx')
df_females = pd.read_excel('Data/Female_Students.xlsx')

# Extract names
male_names = df_males['Student Name'].tolist()
female_names = df_females['Student Name'].tolist()

# Compute embeddings
male_embeddings = {name: get_embedding(name) for name in male_names}
female_embeddings = {name: get_embedding(name) for name in female_names}

# Compute similarity matrix and filter results
results = []
for male_name, male_embedding in male_embeddings.items():
    for female_name, female_embedding in female_embeddings.items():
        similarity = compute_similarity(male_embedding, female_embedding)
        if similarity >= 0.5:  # 50% similarity
            results.append({
                'male_name': male_name,
                'female_name': female_name,
                'similarity': similarity
            })

# Save results to JSON file
output_file_path = 'Data/similarity_results.json'
with open(output_file_path, 'w') as f:
    json.dump(results, f, indent=4)

print(f"Similarity results saved to: {output_file_path}")
