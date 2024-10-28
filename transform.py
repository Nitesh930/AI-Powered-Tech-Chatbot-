from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import load_dataset

# Load GPT-2 model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Add pad_token to the tokenizer (GPT-2 doesn't have one by default)
tokenizer.pad_token = tokenizer.eos_token

# Load and tokenize dataset
dataset = load_dataset('text', data_files={'train': 'tech_news.txt'})

def tokenize_function(examples):
    return tokenizer(examples['text'], 
                     padding='max_length',  
                     truncation=True,       
                     max_length=128)       

# Tokenize dataset and format it
tokenized_datasets = dataset.map(tokenize_function, batched=True, remove_columns=["text"])
tokenized_datasets.set_format(type='torch', columns=['input_ids', 'attention_mask'])

# Data collator to handle dynamic padding
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# Define training arguments with 'eval_strategy' instead of 'evaluation_strategy'
training_args = TrainingArguments(
    output_dir='./results',
    eval_strategy="no",  # Disable evaluation
    learning_rate=2e-5,
    per_device_train_batch_size=2,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir='./logs',
)


# Trainer setup
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    data_collator=data_collator,
)

# Start training
trainer.train()

# Save model and tokenizer
model.save_pretrained('./fine_tuned_gpt2')
tokenizer.save_pretrained('./fine_tuned_gpt2')

print("Model training complete and saved to './fine_tuned_gpt2'")
