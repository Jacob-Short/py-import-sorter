from django.db.models.fields import TextField
import os
from django.forms.fields import EmailField
import black
from django.forms import widgets
import time 
from django import forms
import pandas
import sys
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
import argparse

from user_account.forms import (
RegisterForm,
LoginForm,
CreateProfileForm,
)



def does_nothing():
    '''this is a useless function to make sure these
    lines are not sorted
    '''
    pass


