# Import the app_create functions 
from website import create_app

# Run create app function as main

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
    