import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        res = subprocess.run(
            ["python", abs_file_path],
            cwd=abs_working_dir,
            capture_output=True,
            timeout=30
            )
        
        output = f'STDOUT:, {res.stdout}\n'
        output += f'STDERR: {res.stderr}\n'
        if res.returncode != 0:
            output += f'Process exited with code {res.returncode}'
        return output
    except Exception as e:
        return f'Error: executing Python file: {e}'


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run given python file, constrained to the working directory. No arguments needed.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to the Python script to be run, relative to the working directory."
            ),
        },
    ),
)