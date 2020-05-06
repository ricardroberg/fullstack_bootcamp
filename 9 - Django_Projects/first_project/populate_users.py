import os
import sys
sys.path.append("..")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

## FAKE POP SCRIPT

import random
from first_app.models import Users
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):

        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.email()

        user = Users.objects.get_or_create(first_name=fake_fname, last_name=fake_lname, email=fake_email)[0]


if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('Populating complete!')