import torch
from transformers import BertTokenizer
from models.deep_model import BERTClassifier

def predict(text):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BERTClassifier()
    model.load_state_dict(torch.load('models/bert_model.pt'))
    model.eval()

    encoding = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        outputs = model(encoding['input_ids'], encoding['attention_mask'])
        prediction = torch.argmax(outputs, dim=1).item()

    return 'Spam' if prediction == 1 else 'Ham'

# Example
print(predict("Congratulations! You've won a free iPhone!"))
