from flask import render_template, redirect, url_for, flash, request
from app.auth import bp

@bp.route('/login', methods=['GET', 'POST'])
def login():
    return "login success"


@bp.route('/logout')
def logout():
    return "logout success"

