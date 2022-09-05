from project import create_app
import os

# Call the application factory function to construct a Flask application
# instance using the development configuration
app = create_app('flask.cfg')

# Run this command to run the application in DEBUG mode
# docker run -p 5000:5000 -e DEBUG=1 <image-name>
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=os.environ.get('DEBUG') == '1')
