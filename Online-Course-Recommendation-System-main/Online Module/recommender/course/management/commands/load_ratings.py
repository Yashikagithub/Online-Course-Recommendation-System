import csv
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from course.models import Course, Rating

class Command(BaseCommand):
    help = 'Load ratings from Ratings.csv'

    def handle(self, *args, **kwargs):
        ratings_csv = r'C:\newfol3\Online-Course-Recommendation-System-main\Dataset\Ratings.csv'  # Update with the correct path to Ratings.csv
        with open(ratings_csv, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                user_id = row['userId']
                course_id = row['courseId']
                rating_value = int(row['rating'])
                
                user = User.objects.get(id=user_id)
                course = Course.objects.get(id=course_id)
                
                if not Rating.objects.filter(user=user, course=course).exists():
                    Rating.objects.create(user=user, course=course, rating=rating_value)
                    self.stdout.write(f"Created Rating: {user.username} rated {course.name} with {rating_value}")
                else:
                    self.stdout.write(f"Rating for {user.username} on {course.name} already exists.")

