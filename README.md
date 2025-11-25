## 📊 Model Resource Comparison (1B vs 3B)

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

---

### 📝 **Comment**  
**The 1B model is significantly lighter and faster to train, whereas the 3B model requires more computation cost.**

## 🤖 Inference Output Comparison

### **Inference 1: Fibonacci Continuation**

| Prompt | Llama 1B Output | Llama 3B Output |
|--------|------------------|------------------|
| **"Continue the Fibonacci sequence: 1, 1, 2, 3, 5, 8,"** | Continuing the Fibonacci sequence after the given numbers (1, 1, 2, 3, 5, 8) is a logical process as each number is the sum of the two preceding ones...<br><br>1, 1, 2, 3, 5, 8, **13, 21, 34, 55, 89,...**<br> *Ends with unnecessary commentary: “It seems to take more numbers.”* | The next two terms in the Fibonacci sequence would be **13** and **21**.<br><br>1, 1, 2, 3, 5, 8, **13, 21, 34, 55, 89, 144, 233, 377** |

---

### **Inference 2: “Describe a tall tower in the capital of France.”**

| Prompt | Llama 1B Output | Llama 3B Output |
|--------|------------------|------------------|
| **"Describe a tall tower in the capital of France."** | Produces a fictional **modern white-glass skyscraper**, not aligned with Paris landmarks. Descriptions are overly long, poetic, but inaccurate. | Describes a **historical landmark-style tower**, closer to Parisian aesthetics (limestone, carvings, cultural heritage). Still not Eiffel Tower, but more coherent and relevant. |

---

### 📝 **Inference Summary (One Sentence)**  
**The 3B model provides more focused, relevant, and instruction-following outputs, while the 1B model tends to be verbose, less precise, and more prone to drifting away from the prompt.**


