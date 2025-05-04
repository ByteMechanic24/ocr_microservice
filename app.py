import os
import pytesseract
from PIL import Image
from flask import Flask, request, send_file, jsonify
from io import BytesIO

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    try:
        image = Image.open(image_file)
        text = pytesseract.image_to_string(image)

        # Create a .txt file in memory
        buffer = BytesIO()
        buffer.write(text.encode('utf-8'))
        buffer.seek(0)

        return send_file(
            buffer,
            as_attachment=True,
            download_name='extracted_text.txt',
            mimetype='text/plain'
        )

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def home():
    return 'OCR Microservice is running!'

if __name__ == '__main__':
    app.run(debug=True)
