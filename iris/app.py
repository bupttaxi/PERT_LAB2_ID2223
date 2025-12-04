import gradio as gr
from llama_cpp import Llama
from huggingface_hub import hf_hub_download
import os

# ----------------------------------------
# Global model cache
# ----------------------------------------
loaded_models = {}   # Cache loaded Llama models
current_model_name = None

MODEL_CONFIGS = {
    "1B Model (Datangtang/GGUF1B)": {
        "repo_id": "Datangtang/GGUF1B",
        "filename": "llama-3.2-1b-instruct.Q4_K_M.gguf"
    },
    "3B Model (Datangtang/GGUF3B)": {
        "repo_id": "Datangtang/GGUF3B",
        "filename": "llama-3.2-3b-instruct.Q4_K_M.gguf"
    }
}


# ----------------------------------------
# Load model function
# ----------------------------------------
def load_model(model_choice):
    global loaded_models, current_model_name

    if model_choice in loaded_models:
        print(f"Reusing already loaded model: {model_choice}")
        current_model_name = model_choice
        return loaded_models[model_choice]

    print(f"Downloading model: {model_choice}")

    cfg = MODEL_CONFIGS[model_choice]

    model_path = hf_hub_download(
        repo_id=cfg["repo_id"],
        filename=cfg["filename"],
        local_dir="./model",
        token=os.environ["HF_TOKEN"]
    )

    print(f"Model downloaded to: {model_path}")
    print("Loading GGUF model into memory...")

    llm = Llama(
        model_path=model_path,
        n_ctx=1024,
        n_threads=6,
        n_batch=512,
        n_gpu_layers=0,
        use_mmap=True,
        use_mlock=True,
        verbose=False,
    )

    loaded_models[model_choice] = llm
    current_model_name = model_choice

    print("Model loaded successfully!")
    return llm


# ----------------------------------------
# Chat function
# ----------------------------------------
def chat(message, history, model_choice):
    llm = load_model(model_choice)

    # System prompt
    conversation = "System: You are a helpful assistant.\n"

    # Convert ChatInterface history (list of dicts) into text prompt
    for msg in history[-3:]:
        # ChatInterface format: {"role": "...", "content": "..."}
        if isinstance(msg, dict):
            role = msg.get("role")
            content = msg.get("content", "")
            if role == "user":
                conversation += f"User: {content}\n"
            elif role == "assistant":
                conversation += f"Assistant: {content}\n"

        # Safety: old tuple format
        elif isinstance(msg, list) or isinstance(msg, tuple):
            human, assistant = msg
            conversation += f"User: {human}\n"
            if assistant:
                conversation += f"Assistant: {assistant}\n"

    # Add current message
    conversation += f"User: {message}\nAssistant:"

    # Generate model response
    response = llm(
        conversation,
        max_tokens=128,
        temperature=0.7,
        top_p=0.9,
        top_k=40,
        repeat_penalty=1.1,
        stop=["User:", "Assistant:"],
        echo=False
    )

    return response["choices"][0]["text"].strip()

# ----------------------------------------
# Gradio UI
# ----------------------------------------
with gr.Blocks() as demo:

    gr.Markdown("# 🦙 Datangtang GGUF Model Demo")
    gr.Markdown("Switch between **1B** and **3B** GGUF models in real-time.")

    model_choice = gr.Dropdown(
        label="Select Model",
        choices=list(MODEL_CONFIGS.keys()),
        value="1B Model (Datangtang/GGUF1B)",
    )

    chat_iface = gr.ChatInterface(
        fn=lambda message, history: chat(message, history, model_choice.value),
        examples=[
            "Explain deep learning in one paragraph.",
            "What is the difference between supervised and unsupervised learning?",
            "Explain what a transformer model is.",
        ],
        cache_examples=False,
    )

    model_choice.change(
        fn=lambda x: f"🔄 Switched to: {x}",
        inputs=[model_choice],
        outputs=[],
    )


if __name__ == "__main__":
    demo.launch()