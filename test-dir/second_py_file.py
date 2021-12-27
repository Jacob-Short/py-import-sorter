from django import forms
from django.db.models.fields import TextField
from django.forms import widgets
from django.forms.fields import EmailField

import argparse
import black
import os
import pandas
import sys
import time 

from user_account.forms import (
CreateProfileForm,
LoginForm,
RegisterForm,
)

def does_nothing():
    '''this is a useless function to make sure these
    lines are not sorted
    '''
    pass
