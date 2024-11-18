import pandas as pd
from django.core.management.base import BaseCommand
from course.models import Course

class Command(BaseCommand):
    help = 'Load courses from CSV'

    def handle(self, *args, **kwargs):
        courses_csv = r'C:\newfol3\Online-Course-Recommendation-System-main\Dataset\Courses.csv'
        
        # Load CSV
        data = pd.read_csv(courses_csv)

        # Loop through each row and create a Course object
        for index, row in data.iterrows():
            Course.objects.update_or_create(
                name=row['title'],  # Assuming the title column corresponds to the name
                topics=row['category']  # Assuming the category corresponds to the topics
            )
        self.stdout.write(self.style.SUCCESS('Successfully loaded courses!'))

