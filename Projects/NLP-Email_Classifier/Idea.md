## The General Idea

The goal is to classify incoming emails into the following categories:

- Personal  
- Work  
- Spam  
- Promotions  
- Important (e.g., high-priority emails not strictly related to work or personal matters)

---

## Dataset

The dataset will be constructed from personal email data and may include the following fields:

- Email body  
- Subject  
- Sender  
- Timestamp (optional but could be useful for modeling temporal patterns)

---

## Pipeline Overview

### Preprocessing

- Clean the email text (remove signatures, HTML tags, etc.)
- Tokenize, lowercase, remove stopwords (optional)
- Convert text to numerical features using embeddings such as TF-IDF, Word2Vec, or BERT

### Model Options

- **Traditional Machine Learning**: TF-IDF features with Naive Bayes or Support Vector Machines (SVM)
- **Deep Learning**: BiLSTM or BERT-based models
- **Active Learning**: Implement a user-in-the-loop strategy to label uncertain predictions and improve model performance with minimal labeled data

### Training and Evaluation

- Split data into training, validation, and test sets
- Use metrics such as accuracy, precision, recall, and F1-score to evaluate model performance

### Deployment

- Develop a simple CLI or GUI-based application
- Load and classify new incoming emails using the trained model

---

## Project Structure

```bash
email_classifier/
├── data/
│   └── emails.csv              # Labeled email data
├── models/
│   ├── traditional_model.py    # Naive Bayes / SVM
│   └── deep_model.py           # LSTM / Transformer
├── utils/
│   ├── preprocessing.py        # Text preprocessing
│   └── dataloader.py           # PyTorch Dataset & Dataloader
├── train.py                    # Training loop
├── evaluate.py                 # Evaluation scripts
├── predict.py                  # Load model and predict new email
├── app.py                      # Simple interface (CLI or Streamlit)
├── config.py                   # Configuration settings
└── idea.md                     # Dependencies
```

---
## The part from here is just my notes to further knowlegde

## Model Plan (Deep Learning - LSTM/BERT)

### Use BERT tokenizer and embeddings (from HuggingFace)
- **What it is**: The BERT tokenizer breaks down input text into subword tokens and maps them to numerical IDs. HuggingFace provides pre-trained versions of these tokenizers and models.
- **Purpose**: Generates high-quality, context-aware embeddings for each token in the input text.
- **Hugging Face**: A Python library for working with transformer-based models. It provides:

  - Pre-trained NLP models (e.g., BERT, GPT, RoBERTa, etc.)
  - Tokenizers to convert raw text into numerical input
  - Easy-to-use APIs for tasks like text classification, summarization, translation, and question answering


### Feed into a BiLSTM (optional if not using full Transformer)
- **What it is**: A Bidirectional Long Short-Term Memory (BiLSTM) network processes sequences in both forward and backward directions.
- **Purpose**: Captures context from both past and future tokens, enriching the representation of each token beyond what static embeddings provide.

### Classifier head (Linear + Softmax)
- **What it is**: A fully connected (linear) layer followed by a softmax activation.
- **Purpose**: Maps the final representation of the email to class probabilities (e.g., personal, work, spam).

### Optionally switch to full BERT classifier later
- **What it is**: Use the entire pre-trained BERT model with its classification head instead of using BERT just for embeddings.
- **Purpose**: Leverages BERT’s full power for fine-tuned email classification, potentially improving accuracy.

