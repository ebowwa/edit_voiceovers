def log_response(response_text, log_file):
    with open(log_file, 'a') as file:
        file.write(response_text + '\n')
    print(f"Response logged in {log_file}")