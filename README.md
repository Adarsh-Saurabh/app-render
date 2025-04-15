# Sign Language Detection Web Application

This is a Flask web application that uses computer vision and machine learning to detect and classify sign language gestures in real-time.

## Features

- Real-time sign language detection using your webcam
- Support for A-Z alphabet signs and common phrases
- Modern web interface with confidence scores
- Deployable on a server

## Requirements

- Python 3.8+
- Webcam
- Dependencies listed in `requirements.txt`

## Installation

1. Clone this repository:
```
git clone <repository-url>
cd <repository-directory>
```

2. Create a virtual environment and activate it:
```
python -m venv env
# On Windows
env\Scripts\activate
# On macOS/Linux
source env/bin/activate
```

3. Install the required packages:
```
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```
python app.py
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

3. Allow camera access when prompted by your browser.

4. Position your hand in front of the camera and make sign language gestures.

5. The application will display the detected sign and confidence score in real-time.

## Deployment

To deploy this application on a server:

1. Make sure all dependencies are installed on the server.

2. Run the application with:
```
python app.py
```

3. For production deployment, consider using a WSGI server like Gunicorn:
```
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

4. Set up a reverse proxy (like Nginx) to handle incoming requests.

## Troubleshooting

- If the camera doesn't work, make sure it's properly connected and not being used by another application.
- For server deployment, ensure that the server has access to a camera or configure the application to use a different video source.

## License

[MIT License](LICENSE) 