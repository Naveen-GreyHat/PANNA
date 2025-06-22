# 🌟 PANNA: Python-AI Neural Network Assistant 🌟

Welcome to **PANNA**, a powerful tool that combines AI-driven conversation with Python code execution!  
Built by **Naveen**, PANNA uses the `llama3` model (via **Ollama**) to provide an interactive experience for developers, students, and AI enthusiasts.  
Whether you're writing Python scripts, exploring AI responses, or automating tasks, PANNA is your ultimate assistant! 🚀

---

## ✨ Features

- 🤖 **AI-Powered Chat**: Interact with PANNA using natural language, powered by llama3.
- 🧠 **Python Code Handling**: Automatically detects, saves, and executes Python code from AI responses.
- 🛡️ **Smart Execution**: Distinguishes between interactive (e.g., `input()`) and non-interactive code.
- 💻 **Cross-Platform Support**: Launches scripts in new terminals on Windows, Linux, or macOS.
- ⚡ **Auto-Run Trigger**: Use keywords like _"run"_ or _"execute"_ to launch code automatically.
- ⛑️ **Safe Exit**: Exit with `Ctrl+X` (force), `Ctrl+C` (safe), or commands like `exit`.
- 💾 **Code Saving**: Stores generated Python scripts in the `savedoc/` folder.
- 🚧 **Robust Error Handling**: Gracefully manages execution and file-saving errors.

---

## 🖥️ Setup & Usage

### 1. Install Dependencies

```bash
pip install keyboard ollama
````

### 2. Install and Run Ollama

* Download: [https://ollama.com](https://ollama.com)
* Then in terminal:

```bash
ollama run llama3
```

### 3. Run PANNA

```bash
python panna.py
```

---

### 💬 Chat and Run Code

* Type any natural language task.
* If the response contains Python code, it will:

  * ✅ Be saved in `savedoc/`
  * ▶️ Be executed if it's safe (non-interactive)
  * 🚀 Launch in a terminal if prompted by words like "run", "start", etc.

---

## 📂 Project Structure

```
panna/
├── panna.py          # Main script
├── requirements.txt  # Python dependencies
├── savedoc/          # Folder for saved Python scripts
└── README.md         # This file
```

---

## 🔧 Troubleshooting

* **Ollama Not Found**:
  Ensure Ollama is installed and running. Run `ollama run llama3` in a separate terminal.

* **Keyboard Module Permission**:
  Run the script with admin privileges:

  ```bash
  sudo python panna.py      # Linux/macOS
  ```

  Or open terminal as Administrator on **Windows**.

* **Terminal Not Opening**:
  Verify your terminal emulator is installed and accessible.

* **Python Errors**:
  Check the saved script in `savedoc/` for syntax issues or missing dependencies.

---

## 🤝 Contributing

Want to improve PANNA? Here's how:

1. Fork the repository.
2. Create a branch:

   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:

   ```bash
   git commit -m "Add your feature"
   ```
4. Push the branch:

   ```bash
   git push origin feature/your-feature
   ```
5. Open a Pull Request.

---

## 📜 License

**MIT License**. See `LICENSE` for details.

---

## 🙌 Acknowledgments

* Created by **Naveen** with passion! ❤️
* Powered by **Ollama** and **llama3 (Greyhat127)**
* Thanks to the open-source community for inspiring innovation!

---

# 🌟 PANNA: Code, chat, create! 🌟
