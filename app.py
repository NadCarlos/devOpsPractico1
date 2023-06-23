import requests
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static')
