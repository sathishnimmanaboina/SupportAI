from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired


class TicketForm(FlaskForm):

    title = StringField(
        "Title",
        validators=[DataRequired()]
    )

    description = TextAreaField(
        "Description",
        validators=[DataRequired()]
    )

    category = SelectField(
        "Category",
        choices=[
            ("General", "General"),
            ("Technical", "Technical"),
            ("Billing", "Billing"),
            ("Account", "Account")
        ]
    )

    priority = SelectField(
        "Priority",
        choices=[
            ("Low", "Low"),
            ("Medium", "Medium"),
            ("High", "High")
        ]
    )

    submit = SubmitField("Create Ticket")