from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from werkzeug.utils import secure_filename
from models import db, User, Bug
from forms import LoginForm, RegisterForm, BugForm
import os
from config import Config

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return redirect(url_for('main.login'))

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            session['user_id'] = user.id
            session['role'] = user.role
            return redirect(url_for('main.dashboard'))
        flash('Invalid credentials')
    return render_template('login.html', form=form)

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data, role=form.role.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))
    user = User.query.get(session['user_id'])
    bugs = Bug.query.all()
    if user.role == 'Tester':
        bugs = Bug.query.filter_by(reporter_id=user.id).all()
    elif user.role == 'Developer':
        bugs = Bug.query.filter_by(assigned_to_id=user.id).all()
    return render_template('dashboard.html', bugs=bugs, role=user.role)

@main_bp.route('/report_bug', methods=['GET', 'POST'])
def report_bug():
    form = BugForm()
    if form.validate_on_submit():
        filename = None
        if form.file.data:
            filename = secure_filename(form.file.data.filename)
            form.file.data.save(os.path.join(Config.UPLOAD_FOLDER, filename))
        bug = Bug(
            title=form.title.data,
            description=form.description.data,
            project=form.project.data,
            priority=form.priority.data,
            severity=form.severity.data,
            file=filename,
            reporter_id=session['user_id']
        )
        db.session.add(bug)
        db.session.commit()
        flash('Bug reported successfully')
        return redirect(url_for('main.dashboard'))
    return render_template('bug_report.html', form=form)