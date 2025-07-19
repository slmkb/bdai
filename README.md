# bdai

**bdai** is a Python project designed as an AI-powered file and code agent. It provides a secure environment for interacting with files, running code, and performing automated file operations within a constrained working directory. The project leverages Google's Gemini API and is organized around modular, testable function calls for file management and Python execution.

## Features

- **Secure File Operations**: List, read, and write files, strictly limited to the working directory for safety.
- **Python Code Execution**: Execute Python files with optional arguments, supporting rapid prototyping and testing within safe bounds.
- **Environment Variable Support**: Uses `.env` files to manage API keys and sensitive configurations.
- **Extensible Function API**: Modular function declarations for file management, making it easy to add new capabilities.
- **Unit Tested**: Core functionalities are covered by unittests for reliability.

## Directory Structure

```
bdai/
├── main.py                 # Entry point: CLI interface to the agent
├── system_prompt.py        # System instructions for the agent
├── call_function.py        # Function dispatcher and tool registry
├── functions/              # Core function modules (file info, content, write, run)
│   ├── get_files_info.py
│   ├── get_file_content.py
│   ├── write_file.py
│   └── run_python_file.py
├── tests.py                # Unittest suite for all core functions
└── calculator/             # Example sub-project
    ├── README.md
    ├── main.py
    ├── pkg/
    │   └── calculator.py
    └── tests.py
```

## Getting Started

### Prerequisites

- Python 3.8+
- [Google's Gemini API Python Client](https://github.com/google/generative-ai-python)
- `python-dotenv`

### Installation

```bash
git clone https://github.com/slmkb/bdai.git
cd bdai
pip install -r requirements.txt
```

*Create a `.env` file in the repo root with your Gemini API key:*

```
GEMINI_API_KEY=your_api_key_here
```

### Usage

Run the main agent with your custom prompt:

```bash
python main.py "List all files in the calculator directory"
```

Add `--verbose` for debug output.

### Running Tests

```bash
python -m unittest tests.py
```

## Security

All file and directory operations are sandboxed to the working directory to prevent unauthorized access to the system.


## Author

[slmkb](https://github.com/slmkb)

---
