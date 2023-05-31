import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from todo_app.models import Task, Tag


class Command(BaseCommand):
    help = 'Generates fake data for the Todo List app.'

    TAGS = ['Work', 'Personal', 'Shopping', 'Health', 'Fitness']
    STATUSES = ['OPEN', 'WORKING', 'DONE', 'OVERDUE']

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of fake tasks to create')

    def handle(self, *args, **options):
        fake = Faker()
        count = options['count']
        for _ in range(count):
            title = fake.sentence(nb_words=4)
            description = fake.paragraph(nb_sentences=2)
            due_date = fake.date_between(start_date='-30d', end_date='+30d')
            status = random.choice(self.STATUSES)
            task = Task.objects.create(title=title, description=description, due_date=due_date, status=status)
            self.assign_random_tags(task)

    def assign_random_tags(self, task):
        tags = random.sample(self.TAGS, random.randint(1, len(self.TAGS)))
        for tag_name in tags:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            task.tags.add(tag)
        task.save()


