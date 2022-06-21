"""
This module contains a setup to run the application with ease
"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
