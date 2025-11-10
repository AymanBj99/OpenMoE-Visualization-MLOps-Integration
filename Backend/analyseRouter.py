import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch.nn.functional as F
import pandas as pd
import os

# Charger modèle
model_name = "google/switch-base-8"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to("cuda" if torch.cuda.is_available() else "cpu")

text = "Mixture of Experts routes tokens to specialized MLPs efficiently."
inputs = tokenizer(text, return_tensors="pt").to(model.device)

router_outputs = {}

def make_router_hook(tag):
    def hook(module, inp, out):
        logits = out[0] if isinstance(out, (tuple, list)) else out
        probs = torch.softmax(logits, dim=-1)
        router_outputs[tag] = {
            "logits": logits.detach().cpu(),
            "probs": probs.detach().cpu()
        }
    return hook

for name, module in model.named_modules():
    if "router" in name.lower() and "classifier" not in name.lower():
        module.register_forward_hook(make_router_hook(name))

with torch.no_grad():
    _ = model.encoder(**{k: v for k, v in inputs.items() if k in ["input_ids", "attention_mask"]})

rows = []
for layer_name, values in router_outputs.items():
    logits = values["logits"][0]
    probs = values["probs"][0]
    for t in range(logits.shape[0]):
        for e in range(logits.shape[1]):
            rows.append({
                "layer_name": layer_name,
                "token_index": t,
                "expert_index": e,
                "logit": float(logits[t, e]),
                "probability": float(probs[t, e])
            })

os.makedirs("data", exist_ok=True)
df = pd.DataFrame(rows)
df.to_csv("data/router_analysis.csv", index=False)

print("Fichier exporté : data/router_analysis.csv")
