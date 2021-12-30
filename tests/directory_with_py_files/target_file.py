from django import forms
from django.forms import widgets

from django.db.models.fields import TextField
import sys
import black
import os
from django.forms.fields import EmailField

from .forms import (
    CreateProfileForm,
    LoginForm,
    RegisterForm,
)
import pandas
import argparse
import time


def does_nothing():
    """this is a useless function to make sure these
    lines are not sorted
    """
    pass


