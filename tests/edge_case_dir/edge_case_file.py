from django import forms
from django.forms import widgets

import argparse
import black
import pandas
import sys
import time

from ..directory_with_py_files.forms import (
    CreateProfileForm,
    LoginForm,
    RegisterForm,
)
