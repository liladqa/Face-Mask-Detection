import base64
import numpy as np
from flask import Flask, request, render_template, jsonify
import cv2
import image_processing
from PIL import Image
import os , io , sys

app = Flask(__name__)


# main pagge
@app.route('/')
def main():
    return render_template('main.html')

@app.route('/about.html')
def about():
    return render_template('about.html')


# detection
@app.route('/detection.html', methods=['POST', 'GET'])
def detection():
    if request.method == 'POST':
        # uploaded_file = request.files['formFile']
        # if not uploaded_file:
        #     return "No file uploaded", 400
        # im_b64 = base64.b64encode(uploaded_file.read())
        # im_bytes = base64.b64decode(im_b64)
        # im_arr = np.frombuffer(im_bytes, dtype=np.uint8)  # im_arr is one-dim Numpy array
        # img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
        file = request.files['image']  ## byte file
        if not file:
            return "No file uploaded", 400
        im_b64 = base64.b64encode(file.read())
        im_bytes = base64.b64decode(im_b64)
        im_arr = np.frombuffer(im_bytes, dtype=np.uint8)  # im_arr is one-dim Numpy array
        img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)

        #procesing image
        img = image_processing.show(img)

        # send image
        # retval, buffer = cv2.imencode('.png', img)
        # response = make_response(buffer.tobytes())
        # response.headers['Content-Type'] = 'image/png'
        #
        # return response
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img.astype("uint8"))
        rawBytes = io.BytesIO()
        img.save(rawBytes, "JPEG")
        rawBytes.seek(0)
        img_base64 = base64.b64encode(rawBytes.read())
        return jsonify({'status': str(img_base64)})
    else:
        return render_template('detection.html')


@app.after_request
def after_request(response):
    print("log: setting cors" , file = sys.stderr)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


# start our application
if __name__ == "__main__":
    app.run(debug=True)
