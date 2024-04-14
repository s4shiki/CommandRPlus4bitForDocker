import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import gradio as gr

# モデルとトークナイザのロード
model_id = "CohereForAI/c4ai-command-r-plus-4bit"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

#torch.cuda.set_device(1)  # USE GPU 1

model = torch.nn.DataParallel(model)
model.to('cuda') 

def generate_response(input_text):
    start_token = "<BOS_TOKEN><|START_OF_TURN_TOKEN|><|USER_TOKEN|>"
    end_token = "<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>"
    prompt = start_token + input_text + end_token
    inputs = tokenizer(prompt, return_tensors="pt").to('cuda')  # 入力をCUDAに移動
    output = model.generate(**inputs, max_new_tokens=100, do_sample=True, temperature=0.3)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

# Gradioインターフェースの設定
gr.Interface(fn=generate_response, inputs="text", outputs="text").launch(server_name="0.0.0.0")
