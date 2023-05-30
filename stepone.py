#!/usr/bin/env python3

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

line = 'What color is the undoubtedly beautify sky?'

model_name = 'google/flan-t5-base'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
input_embeddings = model.get_input_embeddings()

tokens = tokenizer.tokenize(line, return_tensors="pt")
print(tokens)
token_ids = tokens['input_ids'][0]
our_embeddings = input_embeddings(token_ids)

print(our_embeddings)
print(our_embeddings.size)
