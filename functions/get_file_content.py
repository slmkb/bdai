import os
from google.genai import types


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        file_size = os.path.getsize(abs_file_path)
        with open(abs_file_path, "rb") as f:
            file_content = f.read(10000)
        if file_size > len(file_content):
            return f'{file_content.decode()}[...File "{file_path}" truncated at 10000 characters]'
        return file_content.decode()
    except Exception as e:
        return f'Error: unexpected error {e}'
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get file content in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to retrive the content from, relative to the working directory.",
            ),
        },
    ),
    )