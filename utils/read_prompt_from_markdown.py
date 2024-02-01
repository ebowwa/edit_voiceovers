def read_prompt_from_markdown(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()
