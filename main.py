import os
from flask import Flask, request, jsonify, abort
from reminder_json_helper import read_reminder_json, create_reminder_json, write_json_reminder
import uuid

app = Flask(__name__)
