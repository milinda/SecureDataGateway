# -*- coding: utf-8 -*-
"""
    DCv2
    ~~~~
    HTRC Data Capsules v2 written on top of libvirt.

    :author Milinda Pathirage, Samitha Liyanage
    :maintainer Milinda Pathirage, Samitha Liyanage
    :license LGPLv2+
"""
from __future__ import print_function
import sys
import os
import libvirt
import logging
import logging.config
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, jsonify
from flask_bootstrap import Bootstrap
from models import db, user_datastore
from flask.ext.security import Security, SQLAlchemyUserDatastore, login_required

app = Flask(__name__, instance_relative_config=True)
app.config.update(dict(
    DEBUG=True,
    VM_HOST='192.168.1.16:16509',
    API_HOST='192.168.1.14'))
app.config['SECRET_KEY'] = 'super-secret'
#app.config.from_pyfile('config.py')
app.config.from_envvar('DCV2_SETTINGS', silent=True)
db.init_app(app)
Bootstrap(app)
security = Security(app, user_datastore)

try:
    with app.open_instance_resource('logging.conf') as f:
        logging.config.fileConfig(f.name)
except:
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        level=logging.INFO)
    logging.warning('Couldn\'t find logging configuration (logging.conf)' +
                    ' file in instance directory.')

@app.before_first_request
def create_user():
    db.create_all()
    user_datastore.create_user(email='matt@nobien.net', password='password')
    db.session.commit()

@app.route('/')
@login_required
def version():
    return render_template('index.html')


@app.route('/capsules', methods=['GET'])
def get_capsules():
    return "{}"


@app.route('/capsules', methods=['POST'])
def create_capsule():
    return "{}"
