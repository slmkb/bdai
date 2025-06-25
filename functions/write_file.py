import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_path, file_path))
    if not abs_file_path.startswith(abs_working_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        with open(abs_file_path, "w") as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: Unhandled error "{e}"'


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write given content to a file in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to write the content to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written into the given file.",
            )
        },
    ),
)