from flask import Flask, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'received_files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/print', methods=['POST'])

  

   




   
def receive_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file received"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400

    # Save file locally
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # TODO: Add your printing logic here (e.g., lpr or cups)
    # Example for Linux print command:
    # os.system(f"lp {filepath}")

    return jsonify({"message": f"File {file.filename} received and saved successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

