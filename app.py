from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for flash messages

@app.route("/")
def home():
    return redirect(url_for('auth'))

@app.route("/auth", methods=["GET", "POST"])
def auth():
    if request.method == "POST":
        action = request.form.get("action")
        if action == "Sign In":
            username = request.form.get("username")
            password = request.form.get("password")
            # Add authentication logic here
            flash("Signed in successfully!", "success")
            return redirect(url_for("auth"))
        elif action == "Sign Up":
            username = request.form.get("username")
            email = request.form.get("email")
            password = request.form.get("password")
            confirm_password = request.form.get("confirm_password")
            # Add sign-up logic here
            flash("Account created successfully!", "success")
            return redirect(url_for("auth"))
        elif action == "Forgot Password":
            email = request.form.get("email")
            # Add password reset logic here
            flash("Password reset email sent!", "info")
            return redirect(url_for("auth"))

    return render_template("auth.html")

if __name__ == "__main__":
    app.run(debug=True)
