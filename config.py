from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)

app.config["SECRET_KEY"] = "random string"
