import os
from django.core.management.base import BaseCommand
from main.models import Chapter  # Adjust this import according to your app structure

class Command(BaseCommand):
    help = 'Load chapters from course_chapter file'

    def handle(self, *args, **kwargs):
        file_path = 'path_to_your_course_chapter_file'  # Update this to the path of your course_chapter file

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
            return

        with open(file_path, 'r') as file:
            for line in file:
                # Split the line by the delimiter '|'
                parts = line.strip().split('|')
                if len(parts) >= 4:  # Ensure there are enough parts to unpack
                    chapter_id = parts[0]
                    chapter_name = parts[1]
                    youtube_link = parts[2]
                    course_id = parts[3]

                    # Create and save the CourseChapter instance
                    chapter = Chapter(
                        chapter_id=chapter_id,  # Ensure you have the correct fields in your model
                        chapter_name=chapter_name,
                        youtube_link=youtube_link,
                        course_id=course_id
                    )
                    chapter.save()

        self.stdout.write(self.style.SUCCESS('Chapters loaded successfully!'))

