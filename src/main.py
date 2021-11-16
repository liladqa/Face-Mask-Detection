import base64
import numpy as np
from flask import Flask, request, render_template
import cv2
import  imshowtest

app = Flask(__name__)


# main pagge
@app.route('/')
def main():
    return render_template('main.html')


# detection
@app.route('/detection', methods=['POST', 'GET'])
def detection():
    if request.method == 'POST':
        uploaded_file = request.files['formFile']
        if not uploaded_file:
            return "No file uploaded", 400
        im_b64 = base64.b64encode(uploaded_file.read())
        im_bytes = base64.b64decode(im_b64)
        im_arr = np.frombuffer(im_bytes, dtype=np.uint8)  # im_arr is one-dim Numpy array
        img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
        imshowtest.show(img)

        return render_template('detection.html')
    else:
        return render_template('detection.html')


# start our application
if __name__ == "__main__":
    app.run(debug=True)
