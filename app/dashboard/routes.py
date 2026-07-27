from flask import Blueprint

dashboard_bp = Blueprint(
    "dashboard",
    __name__
)


@dashboard_bp.route("/")
def home():

    return "<h1>Welcome to SupportAI 🚀</h1>"