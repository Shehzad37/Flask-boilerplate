from Model import app
from views import endpoints



if __name__ == '__main__':
    app.run(debug=True, port=8000)