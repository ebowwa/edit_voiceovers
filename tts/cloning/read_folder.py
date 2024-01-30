# resemble-clone-voice-recording/main.py

# -- snipped --
def read_folder(folder_path):
    data_list = []

    # Iterate through files in the folder
    for filename in os.listdir(folder_path):
        # for each wav file
        if filename.endswith(".wav"):
            # Check if there is a corresponding .txt file
            txt_filename = filename.replace(".wav", ".txt")
            txt_filepath = os.path.join(folder_path, txt_filename)

            # if the pair exists use it
            if os.path.exists(txt_filepath):
                # Read the text content from the .txt file
                with open(txt_filepath, 'r') as txt_file:
                    text_content = txt_file.read()

                # Create a dictionary and append to the list
                file_dict = {
                         'file': os.path.join(folder_path, filename),
                         'text': text_content,
                         'recording_name': txt_filename
                } ①

                data_list.append(file_dict)
            else:
                print(f"WARN: Unable to find corresponding transcript txt file for {filename} - SKIPPING")

    return data_list

# -- snipped --
