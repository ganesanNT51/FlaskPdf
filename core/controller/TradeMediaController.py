from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from core.model.tradeMediaModel import TradeMedia_details
import json

app = Blueprint('tradeMedia', __name__)