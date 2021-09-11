from flask import *
from LoginRadius import LoginRadius as LR

app = Flask(__name__)
app.config["SECRET_KEY"] = "9755c611-707f-4a16-b038-096542939b96"

LR_AUTH_PAGE = "https://friendfundingtest.hub.loginradius.com/auth.aspx?action={}&return_url={}"
LR.API_KEY = "06f206fa-099b-4c10-a6c5-17078886fd12"
LR.API_SECRET = "9755c611-707f-4a16-b038-096542939b96"
loginradius = LR()

@app.route("/")
def index():
    return "Hello World!"


@app.route("/register/")
def register():
    # redirect the user to our LoginRadius register URL
    return redirect(LR_AUTH_PAGE.format("register", request.host_url[:-1] + url_for("login")))

@app.route("/login/")
def login():
    access_token = request.args.get("token")
    if access_token is None:
        # redirect the user to our LoginRadius login URL if no access token is provided
        return redirect(LR_AUTH_PAGE.format("login", request.base_url))

    # return "You have successfully logged in!"
    # fetch the user profile details with their access tokens
    result = loginradius.authentication.get_profile_by_access_token(access_token)

    if result.get("ErrorCode") is not None:
        # redirect the user to our login URL if there was an error
        return redirect(url_for("login"))

    session["user_acccess_token"] = access_token

    return redirect(url_for("dashboard"))

@app.route("/dashboard/")
def dashboard():
    access_token = session.get("user_acccess_token")
    if access_token is None:
        return redirect(url_for("login"))

    # fetch the user profile details with their access tokens
    result = loginradius.authentication.get_profile_by_access_token(access_token)

    if result.get("ErrorCode") is not None:
        # redirect the user to our login URL if there was an error
        return redirect(url_for("login"))

    return jsonify(result)


@app.route("/logout/")
def logout():
    access_token = session.get("user_acccess_token")
    if access_token is None:
        return redirect(url_for("login"))

    # invalidate the access token with LoginRadius API
    loginradius.authentication.auth_in_validate_access_token(access_token)
    session.clear()

    return "You have successfully logged out!"


if __name__ == "__main__":
    app.run(debug=True)