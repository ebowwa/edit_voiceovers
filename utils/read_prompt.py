# read_prompt.py

def read_prompt_from_markdown(file_path):
    """
    Read and return the content of a markdown file.
    
    Parameters:
    - file_path: Path to the markdown file.
    
    Returns:
    - The content of the file.
    """
    with open(file_path, 'r') as file:
        return file.read().strip()
