#!pip install -U git+https://github.com/huggingface/transformers.git trl flash-attn peft datasets accelerate unsloth cudatoolkit-dev
# !pip install -i https://pypi.org/simple/ bitsandbytes
import os

import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the GG model - this is the local one, update it to the one on the Hub
model_id = "NusretOzates/function-calling-model"

os.environ['HF_TOKEN'] = "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"

@st.cache_resource
def load_model():

    model = AutoModelForCausalLM.from_pretrained(model_id, device_map='auto', torch_dtype=torch.bfloat16)
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    #model.generation_config.update(eos_token_id=1)
    #tokenizer.eos_token_id = 1
    #print(tokenizer("<eos>", return_tensors='pt'))
    #print(model.generation_config)

    return model, tokenizer

def generate_text(text: str, system_text, tokenizer):

    text = tokenizer.apply_chat_template(
        [
            {"role": "system", "content": system_text},
            {"role": "user", "content": text}
        ], tokenize=False, add_generation_prompt=True
    )
    input_ids = tokenizer(text, padding="longest",max_length=1024,truncation=True,return_tensors="pt").to("cuda")

    try:
        outputs = model.generate(**input_ids, max_new_tokens=300, do_sample=True, temperature=0.3, top_p=0.9, use_cache=True,stop_strings = [tokenizer.eos_token,"<|eot_id|>"],tokenizer=tokenizer)
    except Exception as e:
        print("Exception")
        print(e)
        print(model.generation_config)

    return tokenizer.decode(outputs[0])

model, tokenizer = load_model()

text = st.text_area(label="Bir metin giriniz.")
system_text = st.text_area(label="Sistem metnini giriniz")
if text:
    response = generate_text(text,system_text, tokenizer).split("<|start_header_id|>assistant<|end_header_id|>")[1]
    st.write(response)


