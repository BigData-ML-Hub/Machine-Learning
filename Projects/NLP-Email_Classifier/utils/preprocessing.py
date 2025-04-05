import pandas as pd

def load_and_clean_data(path='data/spam.csv'):
    df = pd.read_csv(path, encoding='latin-1')
    df = df[['v1', 'v2']]  # Keep only label and text
    df.columns = ['label', 'text']  # Rename columns
    df['label'] = df['label'].map({'ham': 0, 'spam': 1})  # Convert to binary labels
    return df
