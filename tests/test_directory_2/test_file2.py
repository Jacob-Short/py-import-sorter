from .models import User
from django import forms
from django.db import models
from django.forms import widgets
from django.utils import timezone

import argparse
import black
import pandas
import sys
import time

from .forms import (
    CreateProfileForm,
    LoginForm,
    RegisterForm,
)


class Message(models.Model):

    message = models.TextField(max_length=500)
    creator = models.ForeignKey(
        User, related_name="%(class)s_author", null=True, on_delete=models.CASCADE
    )
    recipient = models.ForeignKey(
        User, related_name="%(class)s_recipient", null=True, on_delete=models.CASCADE
    )
    time_created = models.DateTimeField(default=timezone.now)
    isNew = models.BooleanField(default=True)

    def __str__(self):
        return self.message
