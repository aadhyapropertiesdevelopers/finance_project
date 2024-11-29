# run.py
from app import create_app

app = create_app()

# app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)