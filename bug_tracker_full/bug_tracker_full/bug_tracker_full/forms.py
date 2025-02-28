from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, FileField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    role = SelectField('Role', choices=[('Tester', 'Tester'), ('Developer', 'Developer'), ('Admin', 'Admin')])
    submit = SubmitField('Register')

class BugForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    project = StringField('Project Name', validators=[DataRequired()])
    priority = SelectField('Priority', choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')])
    severity = SelectField('Severity', choices=[('Critical', 'Critical'), ('Major', 'Major'), ('Minor', 'Minor')])
    file = FileField('Attach File')
    submit = SubmitField('Report Bug')