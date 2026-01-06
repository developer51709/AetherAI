# Getting Started with AetherAI
Welcome to AetherAI — an adaptive, universal AI runtime designed to work on any device, with any model, under any conditions. This guide will help you install AetherAI, run your first request, and understand the basics of how the system works.

> ⚠️ **Note:** AetherAI is currently in early development.  
> Some features described here may not be fully implemented yet.  
> This page will evolve as the project matures.

---

## 📦 Installation

AetherAI will support multiple installation methods as the project develops.  
For now, contributors can install it from source.

### **1. Clone the repository**
```bash
git clone https://github.com/<your-username>/AetherAI.git
cd AetherAI
```

### 2. Create a virtual environment (recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
# or
.\.venv\Scripts\activate    # Windows
```

### 3. Install dependencies
(Dependencies will be added as modules are implemented.)

```bash
pip install -r requirements.txt
```

If `requirements.txt` does not exist yet, contributors can install modules manually as needed.

---

## 🚀 Quickstart Example
Once the unified API is implemented, using AetherAI will be as simple as:

```python
from aetherai import AetherAI

ai = AetherAI()

response = ai.generate("Explain how AetherAI works.")
print(response)
```

This example demonstrates the core idea:

- You write one line to create the runtime

- You send a request

- AetherAI decides which model to use (local or cloud)

- You get a response without worrying about the backend

This section will be updated as the API stabilizes.

---

## 🧠 How AetherAI Chooses a Model
AetherAI automatically evaluates:

- **Hardware** (CPU/GPU, RAM)

- **Storage** (available space for models)

- **Connectivity** (online/offline, latency)

- **User preferences** (e.g., “prefer local models”)

Based on these factors, it selects the best available model:

- **Local model** (if powerful enough)

- **Cloud model** (if online and allowed)

- **Fallback model** (if resources are limited)

You don’t need to configure anything manually — AetherAI adapts to your environment.

---

## 🧪 Running Tests
As the project grows, tests will be added under:

```Code
tests/
```

To run tests:

```bash
pytest
```

(Testing instructions will expand as modules are implemented.)

---

## 🛠️ Contributing
If you’d like to help build AetherAI, check out:

➡️ `../CONTRIBUTING.md`

You can contribute code, documentation, backends, routing strategies, or ideas.

---

❓ Need Help?
If you run into issues:

- Open a GitHub issue

- Check the FAQ (coming soon)

- Join the discussion in the repository

AetherAI is community‑driven, and your feedback helps shape the project.

---

🌟 What’s Next?
Once you’re familiar with the basics, explore:

- **Architecture Overview → `architecture.md`**

- **Core Components → `components/`**

- **Backends → `backends/`**

These pages explain how AetherAI works internally and how you can extend it.
