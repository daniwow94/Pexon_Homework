#################
#### imports ####
#################

from tkinter.tix import Form
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user, login_required, logout_user

from . import users_blueprint
from .forms import CertificateForm, RegisterForm, LoginForm
from project.models import User, Certificate
from project import db


################
#### routes ####
################

@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    # If the User is already logged in, don't allow them to try to register
    if current_user.is_authenticated:
        flash('Already registered!  Redirecting to your User Profile page...')
        return redirect(url_for('users.login'))
        

    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_user = User(form.email.data, form.password.data, form.username.data, form.first_name.data, form.last_name.data)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash('Thanks for registering, {}!'.format(new_user.username))
        return redirect(url_for('users.certificate'))
    return render_template('users/register.html', form=form)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    # If the User is already logged in, don't allow them to try to log in again
    if current_user.is_authenticated:
        flash('Already logged in!  Redirecting to your Certificate page...')
        return redirect(url_for('users.certificate'))

    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.is_password_correct(form.password.data):
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=form.remember_me.data)
                flash('Thanks for logging in, {}!'.format(current_user.username))
                return redirect(url_for('users.index'))

        flash('ERROR! Incorrect login credentials.')
    return render_template('users/login.html', form=form)


@users_blueprint.route('/certificate', methods=['GET', 'POST'])
@login_required
def certificate():

    form = CertificateForm()

    if request.method == "POST":
        new_certificate = Certificate(form.certificate_name.data, owner=current_user.username)

        try:
            db.session.add(new_certificate)
            db.session.commit()
            return redirect(url_for('users.certificate'))
        except:
            return "There was an error adding your Certificate"
    
    certificate = Certificate.query.order_by(Certificate.registered_on)
    return render_template("users/certificate.html", certificate=certificate, form=form)


@users_blueprint.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    certificate_to_update = Certificate.query.get_or_404(id)
    if request.method == "POST":
        certificate_to_update.certificate_name = request.form['certificate_name']
        try:
            db.session.commit()
            return redirect(url_for('users.certificate'))
        except:
            return "There was an error updating your Certificate"
    else:
        return render_template("users/update.html", certificate_to_update=certificate_to_update)


@users_blueprint.route('/delete/<int:id>')
def delete(id):
    certificate_to_delete = Certificate.query.get_or_404(id)
    try:
        db.session.delete(certificate_to_delete)
        db.session.commit()
        return redirect(url_for('users.certificate'))
    except:
        return "There was an error deleting your Certificate"


@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Goodbye!')
    return redirect(url_for('users.login'))

@users_blueprint.route('/profile')
@login_required
def profile():
    form = CertificateForm()
    certificate = Certificate.query.order_by(Certificate.registered_on)
    return render_template('users/profile.html', certificate=certificate, form=form)