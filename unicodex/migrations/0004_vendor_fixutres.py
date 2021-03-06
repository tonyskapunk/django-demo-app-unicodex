#!/usr/bin/python
#
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by Django 2.2.4 on 2019-08-15 03:12


import django.apps
from django.core.management import call_command
from django.db import migrations

# https://docs.djangoproject.com/en/2.2/topics/migrations/#data-migrations

class Migration(migrations.Migration):

    dependencies = [
        ('unicodex', '0003_auto_20190814_0505'),
    ]

    operations = [
#        call_command('loaddata', 'vendor.yaml')
# This breaks: AttributeError: 'NoneType' object has no attribute 'state_forwards'
# Potentially a bug, probably user error

    ]
