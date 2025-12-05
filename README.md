# Task 1 ： Model Training with checkpoint and comparision 

## 0， Checkpoint

```python

trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    ...
        # checkpoint
        save_strategy = "steps",
        save_steps = 300,
        save_total_limit = 3,          # save latest 3 cp
        # -----------------------------------------------------------------
        ...
    ),
)

trainer_stats = trainer.train(resume_from_checkpoint=True)
```
* 📝 **Comment** : By enabling checkpoints, we can resume training from the most recent saved checkpoint instead of starting from scratch. 


##  1， Model Resource Comparison (1B vs 3B)

We trained both the 1B and 3B models for 1 epoch using a Colab Pro A100 GPU.

| Metric | Llama 1B | Llama 3B |
|--------|----------|-----------|
| **Total Training Time** | 3 h 09 min | 5 h 38 min |
| **Training Time (seconds)** | 1010.27 s | 9548.47 s |
| **Training Time (minutes)** | 16.84 min | 159.14 min |
| **Peak Reserved Memory** | 2.408 GB | 3.736 GB |
| **Peak Reserved Memory (Training Only)** | 1.205 GB | 0.666 GB |
| **Peak Reserved Memory % of Max** | 6.087 % | 9.445 % |
| **Training Memory % of Max** | 3.046 % | 1.684 % |
| **HF GGUF File Size** | **808 MB** | **2.02 GB** |



* 📝 **Comment** : The **1B model is significantly lighter and faster** to train, whereas the 3B model requires more computation cost.


##  2， Inference Output Comparison



| Prompt | Llama 1B Output | Llama 3B Output |
|--------|------------------|------------------|
| **"Continue the Fibonacci sequence: 1, 1, 2, 3, 5, 8,"** | Continuing the Fibonacci sequence after the given numbers (1, 1, 2, 3, 5, 8) is a logical process as each number is the sum of the two preceding ones...<br><br>1, 1, 2, 3, 5, 8, **13, 21, 34, 55, 89,...**<br> *Ends with unnecessary commentary: “It seems to take more numbers.”* | The next two terms in the Fibonacci sequence would be **13** and **21**.<br><br>1, 1, 2, 3, 5, 8, **13, 21, 34, 55, 89, 144, 233, 377** |
| **"Describe a tall tower in the capital of France."** | In the heart of Paris, France, I envision a towering structure that commands admiration from the city's residents and visitors alike. The tall tower in question stands at an impressive height of over 150 meters, making it one of the tallest buildings in the European capital.The tower's *sleek, modern design is a striking blend of art deco and contemporary architecture*. Its exterior is clad in *gleaming white glass panels, creating a sparkling, reflective surface that seems to ripple and shift in the light*. At dusk, the tower's facade is transformed into a kaleidoscope of colors, as if it's being set ablaze from within.As one | *A tall tower can be described as a grand structure that stands proudly in the capital of France. This tower is situated in the heart of the city and serves as a landmark for locals and visitors alike*. It is tall and slender, with each successive tier rising above the last until the tower reaches the sky.The tower itself is constructed with fine white limestone that reflects the sunlight and catches the eye of everyone passing by. The sides of the tower are adorned with intricate carvings of historical scenes, depicting the nation's glorious past and its cultural heritage.The tower has a large glass roof on the top floor, providing breathtaking views of the city|


* 📝 **Comment** : The **3B model provides more focused, relevant, and instruction-following outputs**, while the 1B model tends to be verbose, less precise, and more prone to drifting away from the prompt.


## ✅ Our Choice

Although the 1B model is smaller (808 MB), faster to train, and more resource-efficient,  **the 3B model consistently delivers superior inference quality**, with clearer reasoning, better instruction following, and more coherent descriptions.

**Therefore, we conclude that the 3B fine-tuned model is the better choice for deployment in our Gradio UI**, offering a significantly better user experience while remaining lightweight enough for CPU-based inference through GGUF quantization.

URL for notebooks

1B  https://colab.research.google.com/drive/1GdtsuX4bBkIAAi_owXPmCkscrmNfJAZw

3B  https://colab.research.google.com/drive/1yDOP3cQiEOq4vUgi1m9dwDtdR_LvTQ_b#scrollTo=FqfebeAdT073

---


# Task 2: UI Demonstration

## 1. Ways to Improve Model Performance

### **(a) Model-Centric Approach (improving the model itself)**

Model-centric improvements adjust **training settings, hyperparameters, or architecture** to make the model perform better using the same data.

Examples:

* **Increase training epochs** to allow deeper task learning.
* **Tune the learning rate / scheduler** for more stable optimization.
* **Adjust LoRA parameters** (e.g., higher rank or different α) for better adaptation.
* **Use a stronger base model** (e.g., 3B instead of 1B, or switch to Mistral/Gemma/Qwen).
* **Optimize batch size / gradient accumulation** to smooth gradient updates.

**In short:** improve the model by changing how it is trained or structured.

---

### **(b) Data-Centric Approach (improving the training data)**

Data-centric improvements enhance **data quality, diversity, and task relevance**, often yielding large gains for small models.

Examples:

* **Clean the dataset** by removing duplicates, noisy samples, or inconsistent formatting.
* **Add domain-specific data** (e.g., technical Q&A, customer support, finance, etc.).
* **Include more diverse instruction datasets** like Alpaca, ShareGPT, or Hermes.
* **Apply data quality analysis** (e.g., FineTome-style filtering) to keep only high-quality samples.

**In short:** improve model performance by improving the data it learns from.

---

## 2. UI URL

*https://huggingface.co/spaces/Datangtang/iris*

We tried with different prompt and we see that:
1) Llama-3 3B produces more detailed, human-like explanations with richer vocabulary and clearer logical flow.
2) Llama-3 1B outputs shorter, more formulaic text that is correct but less nuanced.
This aligns with expectations: larger models typically exhibit stronger reasoning, elaboration, and stylistic variation.
3) There is no big difference in time cost between these two models when running in our UI, so

### Our Best Choice is Llama 3B



