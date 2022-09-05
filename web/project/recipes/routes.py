#################
#### imports ####
#################

from flask import redirect, render_template, request, url_for
from project import db
from flask_login import current_user, login_required

from project.models import Certificate
from project.users.forms import CertificateForm
from . import recipes_blueprint
from project.users import users_blueprint



################
#### routes ####
################

@users_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = CertificateForm()

    if request.method == "POST":
        new_certificate = Certificate(form.certificate_name.data, owner=current_user.username)
        try:
            db.session.add(new_certificate)
            db.session.commit()
            return redirect(url_for('users.index'))
        except:
            return "There was an error adding your Certificate"

    certificate = Certificate.query.order_by(Certificate.registered_on)
    return render_template("recipes/index.html", certificate=certificate, form=form)


