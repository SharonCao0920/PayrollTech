from flask import Flask, request, jsonify, render_template
from app import app
from user.models import User

@app.route('/user/signup/', methods=['POST'])
def signup():
    return User().signup()