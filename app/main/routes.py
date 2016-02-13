from flask import render_template, redirect, url_for, request, send_file, Response
from flask.ext.login import login_required, login_user, logout_user, current_user
from ..models import User, Settings
from . import main
from .forms import LoginForm, SettingsForm
from ..python.serialports import serial_ports
from ..python.gettemp import get_temp_json
from ..python.command import sendcommand
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

#@main.route('/image.png')
#def image_png():
#    image = StringIO()
#    plot(image)
#    image.seek(0)
#    return send_file(image,
#                     attachment_filename="image.png",
#                     as_attachment=True)

@main.route('/temperature')
@login_required
def temperature():
    return render_template('temperature.html')

@main.route('/gettempdata')
@login_required
def gettempdata():
    response = get_temp_json()
    return response


@main.route('/lights', methods=['GET', 'POST'])
@login_required
def lights():
    if request.method == 'POST':
        if request.form['submit'] == 'LUCE1':
            print "LUCE1"
            sendcommand()
            pass # do something
        elif request.form['submit'] == 'LUCE2':
            print "LUCE2"
            pass # do something else
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
    form1.serialport.choices=[(portresults[i], portresults[i]) for i in range(len(portresults))]
    return render_template('settings.html', form=form1)

@main.route('/savesettings', methods=['GET', 'POST'])
@login_required
def savesettings():
    settings = Settings()
    form1 = SettingsForm()
    port = form1.serialport.data
    #print(port)
    #print(current_user.username)
    settings.savedb(current_user.username, port)
    return redirect(url_for('main.settings'))
