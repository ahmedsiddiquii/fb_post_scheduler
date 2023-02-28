from django.utils import timezone
import pytz
from datetime import datetime
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
from polls.models import *
import geoip2.database
from tzlocal import get_localzone

obj=list(PostModel.objects.filter(id=23).values())[0]
print(obj)
user_time = obj['time']  # Assuming user entered 4pm
user_time = datetime.combine(datetime.today(), user_time)

# Create a timezone object for the user's timezone
user_timezone = pytz.timezone('Asia/Karachi')

# Convert the UTC time to the user's timezone
user_time = user_time.replace(tzinfo=pytz.utc).astimezone(user_timezone)
print(user_time)