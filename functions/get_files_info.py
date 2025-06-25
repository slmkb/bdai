import os
from google.genai import types


def get_files_info(working_directory, directory=None):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir
    
    if directory:
        target_dir = os.path.abspath(os.path.join(abs_working_dir, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    directory_listing = ""
    
    for item in os.listdir(target_dir):
        try:
            item_path = os.path.join(target_dir, item)
            item_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            directory_listing += f'- {item}: file_size={item_size} bytes, is_dir={is_dir}\n'
        except Exception as e:
            return f'Error: unexpected error {e}'
    return directory_listing


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)