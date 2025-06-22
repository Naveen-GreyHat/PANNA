import subprocess
import ollama
import re
import os
import tempfile
import keyboard
import threading
import sys
import platform

def listen_for_ctrl_x():
    keyboard.wait('ctrl+x')
    print("\n👋 Detected Ctrl+X — Force exiting PANNA.")
    os._exit(0)

def clean_triple_backticks(text):
    return text.replace("```\n```", "```")

def extract_code_blocks(text):
    text = clean_triple_backticks(text)
    return re.findall(r"```(?:python)?\n(.*?)```", text, re.DOTALL)

def detect_block_type(code):
    if 'import ' in code or 'def ' in code or 'print(' in code:
        return 'python'
    return 'unknown'

def is_interactive(code):
    triggers = ['input(', 'while True', 'Enter your choice', 'getpass(', 'raw_input(', 'break']
    return any(trigger in code for trigger in triggers)

def run_in_new_terminal(file_path):
    system = platform.system()
    try:
        if system == "Windows":
            subprocess.Popen(f'start cmd /k python "{file_path}"', shell=True)
        elif system == "Linux":
            subprocess.Popen(['gnome-terminal', '--', 'python3', file_path])
        elif system == "Darwin":  # macOS
            subprocess.Popen(['open', '-a', 'Terminal.app', file_path])
        else:
            print("❌ Unsupported OS for terminal execution.")
    except Exception as e:
        print(f"❌ Failed to launch terminal: {e}")

def execute_code_block(code):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode='w', encoding='utf-8') as tmp:
            tmp.write(code)
            tmp_path = tmp.name
        print(f"\n🚀 Running Python code: {tmp_path}")
        result = subprocess.check_output(["python", tmp_path], stderr=subprocess.STDOUT, text=True)
        os.remove(tmp_path)
        return result
    except subprocess.CalledProcessError as e:
        return f"\n❌ Execution error:\n{e.output}"

def sanitize_filename(prompt):
    return re.sub(r'[^\w\-_. ]', '_', prompt.strip().replace(' ', '_'))[:50]

def run_loop():
    print("\n🧠 Welcome to PANNA made by Naveen – Chat + Python Mode")
    print("⚡ Tip: Press Ctrl+X anytime to force exit.\n")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_dir = os.path.join(base_dir, "savedoc")
    os.makedirs(save_dir, exist_ok=True)

    threading.Thread(target=listen_for_ctrl_x, daemon=True).start()

    try:
        while True:
            task_prompt = input("💬 You:\n> ").strip()
            if task_prompt.lower() in ["exit", "quit", "bye"]:
                print("👋 Exiting PANNA made by Naveen. Goodbye!")
                break

            print("\n🤖 PANNA (powered by llama3 Greyhat127)...\n")
            res = ollama.chat(model='llama3', messages=[
                {"role": "user", "content": task_prompt}
            ])
            ai_response = res['message']['content']
            print("🤖 Response:\n" + ai_response + "\n")

            blocks = [b for b in extract_code_blocks(ai_response) if detect_block_type(b) == 'python']

            if not blocks:
                continue  # Normal response, no code block

            auto_run = any(word in task_prompt.lower() for word in ["run", "execute", "launch", "start", "perform"])

            for i, block in enumerate(blocks):
                print(f"\n💬 Python Code Block {i+1}:\n{'-'*40}\n{block}\n{'-'*40}")
                file_name = sanitize_filename(task_prompt) + '.py'
                file_path = os.path.join(save_dir, file_name)

                try:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(block)
                    print(f"✅ Saved to: {file_path}")
                except Exception as e:
                    print(f"❌ Error saving file: {e}")

                if is_interactive(block):
                    print("🛑 Detected interactive code. Skipping execution.")
                elif auto_run:
                    print("⚡ Detected keyword like 'run'. Launching script in a new terminal...")
                    run_in_new_terminal(file_path)
                else:
                    print("⚡ Executing non-interactive Python code...")
                    output = execute_code_block(block)
                    print("📤 Output:\n" + output)

    except KeyboardInterrupt:
        print("\n👋 Ctrl+C detected. Exiting PANNA safely.")

if __name__ == "__main__":
    run_loop()
