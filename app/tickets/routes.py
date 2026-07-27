import json

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from app.extensions import db
from app.models import Ticket
from app.tickets.forms import TicketForm
from app.ai.service import analyze_ticket

ticket_bp = Blueprint(
    "tickets",
    __name__,
    url_prefix="/tickets"
)


@ticket_bp.route("/")
@login_required
def list_tickets():

    tickets = Ticket.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Ticket.created_at.desc()
    ).all()

    return render_template(
        "tickets.html",
        tickets=tickets
    )


@ticket_bp.route("/create", methods=["GET", "POST"])
@login_required
def create_ticket():

    form = TicketForm()

    if form.validate_on_submit():

        summary = ""
        category = form.category.data
        priority = form.priority.data
        reply = ""

        try:

            ai_result = analyze_ticket(
                form.title.data,
                form.description.data
            )

            # Remove markdown if Gemini returns it
            ai_result = (
                ai_result
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )

            data = json.loads(ai_result)

            summary = data.get("summary", "")
            category = data.get("category", category)
            priority = data.get("priority", priority)
            reply = data.get("reply", "")

        except Exception as e:
            print("AI Error:", e)

        ticket = Ticket(
            title=form.title.data,
            description=form.description.data,
            category=category,
            priority=priority,
            ai_summary=summary,
            ai_reply=reply,
            user_id=current_user.id
        )

        db.session.add(ticket)
        db.session.commit()

        flash("Ticket created successfully!", "success")

        return redirect(url_for("tickets.list_tickets"))

    return render_template(
        "create_ticket.html",
        form=form
    )