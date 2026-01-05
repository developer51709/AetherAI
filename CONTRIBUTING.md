# Contributing to AetherAI

Thank you for your interest in contributing to **AetherAI**!  
This project is built around the idea that adaptive, device‑aware AI should be open, accessible, and community‑driven. Your contributions—big or small—help move that vision forward.

This document explains how to contribute, what we expect, and how to get started.

---

## 🧭 Ways to Contribute

There are many ways to help improve AetherAI:

- **Code contributions**
- **Bug reports**
- **Feature requests**
- **Documentation improvements**
- **Model backend integrations**
- **Cloud provider adapters**
- **Hardware detection modules**
- **Routing strategies**
- **Testing and QA**

If you’re unsure where to start, check the **Issues** tab for items labeled `good first issue` or `help wanted`.

---

## 🛠️ Development Setup

### 1. Fork the repository
Click the **Fork** button at the top of the GitHub page.

### 2. Clone your fork
```bash
git clone https://github.com/<your-username>/AetherAI.git
cd AetherAI
```

### 3. Create a new branch
```bash
git checkout -b feature/my-new-feature
```

### 4. Install dependencies
(Instructions will be added once the project reaches its first working milestone.)

### 5. Make your changes
Follow the coding guidelines below.

### 6. Commit your work
Use clear, descriptive commit messages:

```bash
git commit -m "Add GPU detection module"
```

### 7. Push your branch
```bash
git push origin feature/my-new-feature
```

### 8. Open a Pull Request
Go to your fork on GitHub and click **New Pull Request**.

---

## 📏 Code Guidelines
To keep the project consistent and maintainable:

### Style
- Use clear, readable Python.

- Follow PEP 8 where practical.

- Keep functions small and focused.

- Add comments where logic may be unclear.

### Structure
Place new code in the appropriate module:

```Code
aetherai/
  runtime/      # Routing engine, decision logic
  models/       # Local model loaders, cloud adapters
  storage/      # Model manager, downloads, upgrades
  net/          # Connectivity detection
  api/          # Unified interface for apps
  utils/        # Shared helpers
```

If you’re unsure where something belongs, open an issue or ask in the PR.

### Testing
- Add tests for new features when possible.

- Ensure existing tests pass before submitting a PR.

---

🐛 Reporting Bugs
If you find a bug, please open an issue and include:

- A clear description of the problem

- Steps to reproduce

- Expected behavior

- Actual behavior

- System information (OS, hardware, Python version)

Screenshots or logs are helpful when relevant.

---

## 💡 Suggesting Features
We welcome ideas!
When opening a feature request, please include:

- What problem the feature solves

- Why it’s useful

- How it might work

- Any alternatives you’ve considered

This helps us evaluate and plan features effectively.

---

🔌 Adding New Model Backends
AetherAI is designed to be modular.
To add a new backend:

1. Create a new module under `aetherai/models/`

2. Implement the required interface (docs coming soon)

3. Add detection logic if needed

4. Add routing rules if applicable

5. Include tests and documentation

---

🌐 Adding Cloud Providers
Cloud adapters live in `aetherai/models/cloud/`.

Each provider should include:

- Authentication handling

- Model invocation logic

- Error handling

- A configuration entry for the routing engine

---

## 🤝 Pull Request Guidelines
To help us review your PR smoothly:

- Keep PRs focused on a single change or feature.

- Update documentation if your change affects usage.

- Reference related issues in the PR description.

- Be open to feedback—reviews help maintain quality.

We aim to review PRs promptly, but please be patient during busy periods.

---

## 📜 Code of Conduct
AetherAI follows a simple principle:

**Be respectful, constructive, and collaborative.**

Harassment, discrimination, or hostile behavior will not be tolerated.

---

## ⭐ Thank You
Your contributions help shape AetherAI into a powerful, flexible, and accessible AI runtime.
We’re excited to build this with you.

If you enjoy the project, consider starring the repository to support its growth.
