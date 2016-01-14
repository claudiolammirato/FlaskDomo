from flask import render_template, redirect, url_for, request, send_file
from flask.ext.login import login_required, login_user, logout_user
from ..models import User
from . import main
from .forms import LoginForm, SettingsForm
from ..python.importfile import importdatalog
from ..python.graph import plot
from ..python.serialports import serial_ports
from cStringIO import StringIO


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.verify_password(form.password.data):
            return redirect(url_for('main.login', **request.args))
        login_user(user, form.remember_me.data)
        return redirect(request.args.get('next') or url_for('main.index'))
    return render_template('login.html', form=form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/image.png')
def image_png():
    image = StringIO()
    plot(image)
    image.seek(0)
    return send_file(image,
                     attachment_filename="image.png",
                     as_attachment=True)

@main.route('/temperature')
@login_required
def temperature():
    #importdatalog() levare # per importare da Arduino

    return render_template('temperature.html')


@main.route('/lights')
@login_required
def lights():
    return render_template('lights.html')


@main.route('/garden')
@login_required
def garden():
    return render_template('garden.html')


@main.route('/alarm')
@login_required
def alarm():
    return render_template('alarm.html')

@main.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    form1 = SettingsForm()
    portresults = serial_ports()
    #print(portresults[0])
    form1.serialport.choices=[('cpp', portresults[i]) for i in range(len(portresults))]
    return render_template('settings.html', form=form1)
