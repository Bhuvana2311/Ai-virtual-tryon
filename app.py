from flask import Flask, render_template, request, redirect, url_for
import replicate
import os
from werkzeug.utils import secure_filename

from dotenv import load_dotenv
load_dotenv()  # Load REPLICATE_API_TOKEN from .env

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# AI Try-On page
@app.route('/tryon', methods=['GET', 'POST'])
def tryon():
    result_image = None
    if request.method == 'POST':
        # Get uploaded file
        user_file = request.files['user_image']
        dress_file = request.files['dress_image']

        # Save files
        user_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(user_file.filename))
        dress_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(dress_file.filename))
        user_file.save(user_path)
        dress_file.save(dress_path)

        # Call Replicate AI model (example, replace with correct model)
        model = replicate.models.get("virtual-try-on/model-name")  # replace with real model
        output_url = model.predict(user_image=user_path, dress_image=dress_path)

        result_image = output_url  # This URL will show in the template

    return render_template('tryon.html', result_image=result_image)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')
@app.route('/tryon')
def tryon():
    return render_template('shop.html')  # or tryon.html if different
