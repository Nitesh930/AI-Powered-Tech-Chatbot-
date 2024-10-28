# backend.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from fastapi.middleware.cors import CORSMiddleware

# Load the fine-tuned model and tokenizer
model = GPT2LMHeadModel.from_pretrained('./fine_tuned_gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('./fine_tuned_gpt2')
tokenizer.pad_token = tokenizer.eos_token
model.config.pad_token_id = tokenizer.pad_token_id

# FastAPI app setup
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify a list of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Request and Response models
class QueryRequest(BaseModel):
    prompt: str

class QueryResponse(BaseModel):
    response: str

# Function to generate text from the model
def generate_text(prompt, max_length=100, temperature=0.7):
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(
        inputs['input_ids'],
        attention_mask=inputs['attention_mask'],
        max_length=max_length,
        temperature=temperature,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        top_k=50,
        top_p=0.95,
        do_sample=True,
        pad_token_id=tokenizer.pad_token_id
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Define a route to handle the query
@app.post("/generate", response_model=QueryResponse)
async def generate(query: QueryRequest):
    response_text = generate_text(query.prompt)
    return QueryResponse(response=response_text)
