🌟 PANNA: Python-AI Neural Network Assistant 🌟
Welcome to PANNA, a powerful tool that combines AI-driven conversation with Python code execution! Built by Naveen, PANNA uses the llama3 model (via Ollama) to provide an interactive experience for developers, students, and AI enthusiasts. Whether you're writing Python scripts, exploring AI responses, or automating tasks, PANNA is your ultimate assistant! 🚀

✨ Features

AI-Powered Chat: Interact with PANNA using natural language, powered by llama3.
Python Code Handling: Automatically detects, saves, and executes Python code from AI responses.
Smart Execution: Distinguishes between interactive (e.g., input()) and non-interactive code.
Cross-Platform Support: Launches scripts in new terminals on Windows, Linux, or macOS.
Auto-Run Trigger: Use keywords like "run" or "execute" to launch code automatically.
Safe Exit: Exit with Ctrl+X (force), Ctrl+C (safe), or commands like exit.
Code Saving: Stores generated Python scripts in the savedoc folder.
Robust Error Handling: Gracefully manages execution and file-saving errors.


🛠️ Installation
Follow these steps to set up PANNA on your system.
Prerequisites

Python 3.7+ installed.
A terminal emulator:
Windows: cmd or PowerShell.
Linux: gnome-terminal or equivalent.
macOS: Terminal.app.


Internet connection for installing dependencies and Ollama.

Step-by-Step Setup

Clone or Download the Project:
git clone https://github.com/your-username/panna.git
cd panna


Install Python Dependencies:Create a virtual environment (optional but recommended) and install the required packages:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


Install Ollama:

Windows/Linux/macOS:
Visit ollama.ai and download the installer for your OS.
Follow the installation instructions provided on the website.
Verify Ollama is installed by running:ollama --version




Note: On Linux, you may need to run sudo systemctl start ollama to start the Ollama service.


Pull the llama3 Model:After installing Ollama, download the llama3 model:
ollama pull llama3


This command downloads the model (~4-8 GB, depending on the version).
Ensure Ollama is running in the background (ollama run llama3 or as a service).


Run PANNA:Start the application:
python panna.py




🚀 Using PANNA

Launch PANNA:Run python panna.py to see the welcome message:
🧠 Welcome to PANNA made by Naveen – Chat + Python Mode
⚡ Tip: Press Ctrl+X anytime to force exit.


Interact:

Enter a prompt at the >  prompt, e.g., Write a Python script to reverse a string.
PANNA responds with text and, if relevant, Python code blocks.


Code Execution:

Python code in responses is saved to the savedoc folder.
Non-interactive code runs inline unless keywords like run or execute are used.
Interactive code (e.g., with input()) opens in a new terminal.
Example output:💬 Python Code Block 1:
----------------------------------------
text = input("Enter a string: ")
print(text[::-1])
----------------------------------------
✅ Saved to: savedoc/Write_a_Python_script_to_reverse_a_string.py
🛑 Detected interactive code. Skipping execution.




Exit:

Type exit, quit, or bye to exit gracefully.
Press Ctrl+X to force exit.
Press Ctrl+C to exit safely.




📂 Project Structure
panna/
├── panna.py          # Main script
├── requirements.txt  # Python dependencies
├── savedoc/         # Folder for saved Python scripts
└── README.md        # This file


🔧 Troubleshooting

Ollama Not Found:Ensure Ollama is installed and running. Run ollama run llama3 in a separate terminal.
Keyboard Module Permission:Run the script with admin privileges: sudo python panna.py (Linux/macOS) or open the terminal as Administrator (Windows).
Terminal Not Opening:Verify your terminal emulator is installed and accessible.
Python Errors:Check the saved script in savedoc for syntax issues or missing dependencies.


🤝 Contributing
Want to improve PANNA? Here's how:

Fork the repository.
Create a branch: git checkout -b feature/your-feature.
Commit changes: git commit -m 'Add your feature'.
Push: git push origin feature/your-feature.
Open a Pull Request.


📜 License
MIT License. See LICENSE for details.

🙌 Acknowledgments

Created by Naveen with passion! ❤️
Powered by Ollama and llama3 (Greyhat127).
Thanks to the open-source community for inspiring innovation!

🌟 PANNA: Code, chat, create! 🌟