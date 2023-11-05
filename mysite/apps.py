from django.apps import AppConfig
from flask import Flask, render_template, request
import sqlite3

class MysiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mysite'

from django.shortcuts import render


