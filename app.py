from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route (URL endpoint)
@app.route("/")
def home():
    return {"message": "BJJ Academy API is running!"}

# Run the app if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)
