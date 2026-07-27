from flask import Blueprint

ticket_bp = Blueprint(
    "tickets",
    __name__,
    url_prefix="/tickets"
)