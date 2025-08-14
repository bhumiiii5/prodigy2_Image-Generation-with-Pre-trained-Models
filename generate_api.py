import requests

# === 1) Put your Hugging Face token here ===
HF_TOKEN = "hf_MFadfTiLSauImdTwlQhLbJAbA0XryoNqt0"  # replace with yours

# === 2) Model to use ===
MODEL_ID = "stabilityai/stable-diffusion-2-1"

API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

# === 3) Write your prompt ===
prompt = "a fantasy castle on a hill during sunset, highly detailed, 4k"

params = {
    "inputs": prompt,
    "options": {"wait_for_model": True},
    "parameters": {
        "num_inference_steps": 30,
        "guidance_scale": 7.5
    }
}

print("Generating... please wait.")
resp = requests.post(API_URL, headers=HEADERS, json=params, timeout=600)

# Error handling
if resp.status_code != 200 or "image" not in resp.headers.get("content-type", ""):
    print("Error:", resp.status_code, resp.text[:500])
    raise SystemExit

# Save the result
out_path = "output.png"
with open(out_path, "wb") as f:
    f.write(resp.content)

print(f"Done! Saved as {out_path}")
