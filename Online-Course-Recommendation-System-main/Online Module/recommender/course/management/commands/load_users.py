import csv
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from course.models import Profile  # Ensure this matches the location of your Profile model

class Command(BaseCommand):
    help = 'Load users from Users.csv'

    def handle(self, *args, **kwargs):
        users_csv = r'C:\newfol3\Online-Course-Recommendation-System-main\Dataset\Users.csv'  # Update with the correct path
        with open(users_csv, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                username = row['name']
                field_of_interest = row['field_of_interest']
                
                if not User.objects.filter(username=username).exists():
                    user = User.objects.create_user(username=username)
                    Profile.objects.create(user=user, field_of_interest=field_of_interest)
                    self.stdout.write(f"Created User: {username}")
                else:
                    self.stdout.write(f"User {username} already exists.")

