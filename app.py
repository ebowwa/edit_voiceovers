from VideoSpeechProcessor_refactored import VideoSpeechProcessor
import os
from flask import Flask, request, send_from_directory, jsonify
from werkzeug.utils import secure_filename

# Assuming the VideoSpeechProcessor is correctly imported and set up

app = Flask(__name__)

# Use directories within the current project folder or a user's home directory
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))  # Gets the directory where the script runs
UPLOAD_FOLDER = os.path.join(PROJECT_ROOT, 'uploads')  # Creates a 'uploads' subdirectory in the script's directory
OUTPUT_FOLDER = os.path.join(PROJECT_ROOT, 'outputs')  # Creates a 'outputs' subdirectory in the script's directory

ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Ensure the upload and output directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Process the video and generate speech
        # Modify the paths according to your requirements
        processor = VideoSpeechProcessor(
            video_file_path=file_path,
            target_frame_rate=30,  # Example value
            prompt_path = 'prompts/narrations/tik5.md',
            project_uuid = '0448305f',
            voice_uuid = 'd3e61caf'
        )



        # Process the video and generate the speech
        audio_files, total_text_length, total_audio_duration, video_duration = processor.process_video_and_generate_speech()

        # Generate output file paths dynamically based on the uploaded video's filename
        base_name = os.path.splitext(filename)[0]
        output_audio_path = os.path.join(app.config['OUTPUT_FOLDER'], f"{base_name}_output_audio.wav")
        output_video_path = os.path.join(app.config['OUTPUT_FOLDER'], f"{base_name}_processed_video.mp4")

        # Concatenate and overlay the audio
        VideoSpeechProcessor.concatenate_audio_files(audio_files, output_audio_path)
        VideoSpeechProcessor.overlay_audio(file_path, output_audio_path, output_video_path)

        # Assuming the client will handle downloading via a static route or similar
        return jsonify({
            'message': 'Video processed successfully',
            'output_video_path': output_video_path
        })

    return jsonify({'error': 'File extension not allowed'}), 400

if __name__ == "__main__":
    app.run(debug=True)
