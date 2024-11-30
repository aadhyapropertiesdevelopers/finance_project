
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the Dashboard page
@app.route('/')
def dashboard():
    return render_template('dashboard.html')  # Serve the main dashboard page
#Route for submitting the payment form
@app.route('/submit_payment', methods=['POST'])
def submit_payment():
    # Process the form data here (e.g., save to database)
    print("Form Submitted")
    return redirect(url_for('dashboard'))  # Redirect to dashboard after submission

if __name__ == '__main__':
    app.run(debug=True)
